from django.db import models

from cart.models import CartItem, Cart
from umge.utils import generate_slug
from accounts.models import Rider, User


class Order(models.Model):

    class STATUS(models.TextChoices):
        PENDING = "PD", "Pending"
        PROCESSING = "PS", "Processing"
        DONE = "DN", "Done"
        CANCELLED = "CN", "Cancelled"

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(CartItem, on_delete=models.DO_NOTHING)
    transaction_id = models.CharField(max_length=7, blank=True, unique=True)
    status = models.CharField(max_length=20, default=STATUS.PENDING, choices=STATUS.choices)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            transaction_ids = Order.objects\
                .values_list('transaction_id', flat=True)
            transaction_id = generate_slug(transaction_ids, max_length=5)
            self.transaction_id = transaction_id.replace('-', '').upper()

        super().save(*args, **kwargs)


class Delivery(models.Model):

    class STATUS(models.TextChoices):
        PENDING = "PD", "Pending"
        PROCESSING = "PS", "Processing"
        DONE = "DN", "Done"
        CANCELLED = "CN", "Cancelled"

    rider = models.ForeignKey(Rider, on_delete=models.DO_NOTHING, related_name='delievery_rider')
    reciepient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='delivery_recipient')
    items = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=30, default=STATUS.PENDING, choices=STATUS.choices)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rider.username} {self.reciepient.username}'

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    def get_delivery_location(self):
        reciepient_cart = Cart.objects.get(cart_user=self.reciepient)

        return reciepient_cart.get_point()

    def save(self, *args, **kwargs):
        if self.status == Delivery.STATUS.DONE:
            for item in self.items:
                order = Order.objects.get(transaction_id=item['transaction_id'])
                order.status = Order.STATUS.DONE
                order.save()

        if not self.slug:
            delivery_slugs = Delivery.objects\
                .values_list('slug', flat=True)
            self.slug = generate_slug(delivery_slugs, max_length=50)

        super().save(*args, **kwargs)
