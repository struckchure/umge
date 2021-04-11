from django.db import models
from django.contrib.auth import get_user_model

from store.models import Product
from umge.utils import generate_slug

User = get_user_model()


class Cart(models.Model):
    cart_user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(Product, blank=True)
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
        cart_item_amounts = []

        for item in self.cart_items:
            cart_item_amounts.append(item.get_product_price())

        cart_item_total_balance = sum(cart_item_amounts)

        return cart_item_total_balance
