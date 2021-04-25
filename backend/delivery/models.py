from django.db import models
from django.contrib.auth import get_user_model

from cart.models import CartItem
from umge.utils import generate_slug


User = get_user_model()


class Order(models.Model):

    STATUS = (
        ('PD', 'PENDING'),
        ('PS', 'PROCESSING'),
        ('DN', 'DONE'),
        ('CN', 'CANCELLED')
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(CartItem, on_delete=models.DO_NOTHING)
    transaction_id = models.CharField(max_length=7, blank=True, unique=True)
    status = models.CharField(max_length=20, default='PD', choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            transaction_ids = Order.objects.values_list('transaction_id', flat=True)
            transaction_id = generate_slug(transaction_ids)
            self.transaction_id = transaction_id.replace('-', '').upper()

        super().save(*args, **kwargs)
