from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import random

from accounts.managers import UserManager, RiderManager
from umge.utils import generate_slug


class User(AbstractBaseUser, PermissionsMixin):

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
        orders = Order.objects.filter(user=reciepient)
        orders_serialized = OrderSerializer(orders, many=True).data

        create_delivery = Delivery.objects.create(
            rider=rider,
            reciepient=reciepient,
            items=orders_serialized
        )
        create_delivery.save()

        if create_delivery:
            status = True

        response = {
            'status': status,
            'delivery': DeliverySerializer(create_delivery).data
        }

        return response


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

        fund_history = FundHistory.objects.create(
            user=self.wallet_user
        )
        fund_history.status = True
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    reference = models.CharField(max_length=20, blank=True, unique=True)
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

        if not self.reference:
            self.reference = self.make_reference()

        super().save(*args, **kwargs)

    def make_slug(self):
        slugs = FundHistory.objects.values_list('slug', flat=True)
        new_slug = generate_slug(slugs)

        return new_slug

    def make_reference(self):
        references = FundHistory.objects.values_list('reference', flat=True)
        new_reference = generate_slug(references, 5)\
            .replace('-', f'{random.randint(0, 9)}')\
            .replace('_', f'{random.randint(0, 9)}')\
            .upper()

        return new_reference

    def get_description(self):
        status = 'failed'

        if self.status:
            status = 'succeeded'

        description = f'Wallet fund with reference {self.reference} {status}'

        return description
