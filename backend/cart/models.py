from django.db import models
from django.contrib.auth import get_user_model

from umge.utils import generate_slug
from store.models import Product, ProductOption


User = get_user_model()


class CartItem(models.Model):
    cart_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_item_options = models.ManyToManyField(ProductOption, blank=True)
    cart_item_quantity = models.PositiveIntegerField(default=1)
    cart_item_description = models.TextField(blank=True)
    cart_item_slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.cart_item.product_name

    class Meta:
        verbose_name = 'Car item'
        verbose_name_plural = 'Cart items'

    def save(self, *args, **kwargs):
        if not self.cart_item_slug:
            slugs = CartItem.objects.values_list('cart_item_slug', flat=True)
            self.cart_item_slug = generate_slug(slugs)

        super().save(*args, **kwargs)

    def get_total_balance(self):
        balance = self.cart_item.product_price

        for option in self.cart_item_options.all():
            balance += option.option_price

        return balance


class Cart(models.Model):
    cart_user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem, blank=True)
    cart_slug = models.SlugField(max_length=100, blank=True, unique=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_user.username

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def save(self, *args, **kwargs):
        if not self.cart_slug:
            cart_slugs = Cart.objects.values_list('cart_slug', flat=True)
            self.cart_slug = generate_slug(cart_slugs)

        super().save(*args, **kwargs)

    def get_cart_total_balance(self):
        cart_item_total_balance = 0

        for item in self.cart_items.all():
            cart_item_total_balance += item.cart_item.product_price

        return cart_item_total_balance

    def check_out(self):
        from accounts.models import Wallet
        from delivery.models import Order

        user_wallet = Wallet.objects.get(wallet_user=self.cart_user)
        user_balance = user_wallet.wallet_balance

        if user_balance >= self.get_cart_total_balance():
            for cart_item in self.cart_items.all():
                check_out_order = Order.objects.create(
                    user=self.cart_user,
                    item=cart_item
                )
                user_wallet.wallet_balance -= cart_item.get_total_balance()

                check_out_order.save()

            checkout_state = {
                'status': True,
                'message': 'Checkout successful'
            }
        else:
            checkout_state = {
                'status': False,
                'message': 'Insufficient balance'
            }

        user_wallet.save()

        return checkout_state
