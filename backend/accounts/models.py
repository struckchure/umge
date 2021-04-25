from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
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

    def get_stores(self):
        from store.models import Store

        user = User.objects.get(username=self.username)
        stores = Store.objects.filter(store_owner=user)

        if not stores.exists():
            stores = None

        return stores

    def get_wallet(self):
        user = User.objects.get(username=self.username)
        wallet, created = Wallet.objects.get_or_create(wallet_user=user)
        if not created:
            wallet.save()

        return wallet

    def get_cart(self):
        from cart.models import Cart
        user = User.objects.get(username=self.username)
        cart, created = Cart.objects.get_or_create(cart_user=user)
        if not created:
            cart.save()

        return cart


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
