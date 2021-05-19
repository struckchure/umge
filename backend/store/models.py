from django.db import models
from django.utils.text import slugify

from store.handlers import store_image_handler, product_image_handler
from umge.utils import generate_slug
from accounts.models import User


class Store(models.Model):

    STORE_PACKAGES = (
        ('BSC', 'Basic'),
        ('STD', 'Standard'),
        ('PRM', 'Premimum')
    )

    store_name = models.CharField(max_length=255, blank=False)
    store_description = models.TextField(max_length=255, blank=True)
    store_package = models.CharField(max_length=10, choices=STORE_PACKAGES, default='STD')
    store_image = models.ImageField(upload_to=store_image_handler, null=True, blank=True)
    store_email = models.EmailField(max_length=50, blank=True)
    store_phone_number = models.CharField(max_length=20, blank=True)
    store_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_owner')
    store_staffs = models.ManyToManyField(User, related_name='store_staffs', blank=True)
    store_slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def save(self, *args, **kwargs):
        if self.store_owner.type != User.Types.STORE_OWNER:
            user = User.objects.get(username=self.store_owner.username)
            user.type = User.Types.STORE_OWNER
            user.save()

        if not self.store_slug:
            store_slug = slugify(self.store_name)
            self.store_slug = store_slug

        super().save(*args, **kwargs)


class ProductOption(models.Model):
    option_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=255, unique=True, blank=False)
    option_price = models.PositiveIntegerField(default=0)
    option_slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option_name

    class Meta:
        verbose_name = 'Product option'
        verbose_name_plural = 'Product options'

    def save(self, *args, **kwargs):
        if not self.option_slug:
            option_slugs = ProductOption.objects.values_list('option_slug', flat=True)
            option_slug = generate_slug(option_slugs)
            self.option_slug = option_slug

        super().save(*args, **kwargs)


class Product(models.Model):

    PRODUCT_TYPE = (
        ('PB', 'Perishable'),
        ('NPB', 'Non-Perishable')
    )

    product_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, blank=False)
    product_image = models.ImageField(upload_to=product_image_handler, null=True)
    product_type = models.CharField(max_length=255, choices=PRODUCT_TYPE, default='PB')
    product_options = models.ManyToManyField(ProductOption, blank=True)
    product_price = models.PositiveIntegerField(blank=False)
    product_slug = models.SlugField(max_length=255, unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if not self.product_slug:
            product_slugs = Product.objects.values_list('product_slug', flat=True)
            product_slug = generate_slug(product_slugs)
            self.product_slug = product_slug

        super().save(*args, **kwargs)

    def get_total_price(self):
        product_options = []

        for option in self.product_options.all():
            product_options.append(option.option_price)

        product_price = self.product_price + sum(product_options)

        return product_price
