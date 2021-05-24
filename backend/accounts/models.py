from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import random

from accounts.managers import UserManager, RiderManager
from umge.utils import generate_slug


class User(AbstractBaseUser, PermissionsMixin):

    MAX_DELIVERY_COUNT = 20

    class Types(models.TextChoices):
        NORMAL = "NORMAL", "Normal"
        RIDER = "RIDER", "Rider"
        STORE_OWNER = "STORE_OWNER", "Store Owner"

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
    type = models.CharField(max_length=20, default=Types.NORMAL, choices=Types.choices)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.get_wallet()
        self.get_cart()

    def get_stores(self):
        from store.models import Store

        user = User.objects.get(username=self.username)
        stores = Store.objects.filter(store_owner=user)

        if not stores.exists():
            stores = None

        return stores

    def get_wallet(self):
        wallet, created = Wallet.objects.get_or_create(wallet_user_id=self.pk)

        if not created:
            wallet.save()

        return wallet

    def get_cart(self):
        from cart.models import Cart

        cart, created = Cart.objects.get_or_create(cart_user_id=self.pk)
        if not created:
            cart.save()

        return cart

    def make_delivery(self, reciepient):
        from delivery.models import Delivery, Order
        from delivery.serializers import DeliverySerializer, OrderSerializer

        status = False
        rider = User.objects.get(pk=self.pk)
        orders = Order.objects.filter(
            user=reciepient,
            status=Order.STATUS.PENDING
        )
        orders_serialized = OrderSerializer(orders, many=True).data

        rider_is_available = Delivery.objects.filter(
            rider=rider,
            status=Delivery.STATUS.PROCESSING
        ).count() <= self.MAX_DELIVERY_COUNT

        if rider_is_available:
            create_delivery = Delivery.objects.create(
                rider=rider,
                reciepient=reciepient,
                items=orders_serialized,
                status=Delivery.STATUS.PROCESSING
            )

            if create_delivery:
                status = True
                self.process_orders(orders)
                create_delivery.save()

            response = {
                'status': status,
                'delivery': DeliverySerializer(create_delivery).data
            }
        else:
            status = False
            message = 'You need to complete existing deliveries before taking another one.'
            response = {
                'status': status,
                'message': message
            }

        return response

    def process_orders(self, orders):
        from delivery.models import Order

        for order in orders:
            order.status = Order.STATUS.PROCESSING
            order.save()


class Rider(User):

    objects = RiderManager()

    class Meta:
        proxy = True


class Wallet(models.Model):
    wallet_user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wallet_user.username

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def fund_wallet(self, amount):
        from umge.payment import PaymentAPI

        payment_api = PaymentAPI()
        recieve_payment = payment_api.recieve(
            email=self.wallet_user.email,
            amount=amount
        )

        if recieve_payment:
            status = True
            message = 'Checkout successful'
        else:
            status = False
            message = 'Request failed'

        if status:
            fund_history = FundHistory.objects.create(
                user=self.wallet_user,
                reference=recieve_payment['data']['reference'],
                access_code=recieve_payment['data']['access_code']
            )

            fund_history.save()

        return (message, status, recieve_payment)


class Activity(models.Model):
    activity_user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity_user.username

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class FundHistory(models.Model):

    class STATUS(models.TextChoices):
        VERIFIED = 'V', 'Verified'
        UNVERIFIED = 'U', 'Unverified'
        DECLINED = 'D', 'Declined'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS.choices, default=STATUS.UNVERIFIED)
    reference = models.CharField(max_length=20, unique=True)
    access_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reference}'

    class Meta:
        verbose_name = 'Fund history'
        verbose_name_plural = 'Fund histories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.make_slug()

        super().save(*args, **kwargs)

    def make_slug(self):
        slugs = FundHistory.objects.values_list('slug', flat=True)
        new_slug = generate_slug(slugs)

        return new_slug

    def get_description(self):
        status = 'failed'

        if self.status:
            status = 'succeeded'

        description = f'Wallet fund with reference {self.reference} {status}'

        return description

    def verify_transaction(self):
        from umge.payment import PaymentAPI

        status = False
        message = 'Transaction Unverified'

        response = {
            'status': status,
            'message': message
        }

        if self.status != FundHistory.STATUS.VERIFIED:
            payment_api = PaymentAPI()
            is_verified = payment_api.verify(self.reference)

            if is_verified['status'] and self.status == FundHistory.STATUS.UNVERIFIED:
                amount = is_verified['data']['amount']

                user_wallet = Wallet.objects.get(wallet_user=self.user)
                user_wallet.wallet_balance += amount

                user_wallet.save()

            response = is_verified

        return response

    def get_amount(self):
        from umge.payment import PaymentAPI

        payment_api = PaymentAPI()
        is_verified = payment_api.verify(self.reference)

        return is_verified['data']['amount']
