from django.utils.text import slugify
import datetime

STORE_FOLDER = 'stores/'
PRODUCT_FOLDER = 'product/'


def store_image_handler(instance, filename, *args, **kwargs):
    file_extension = filename.split('.')[-1]
    _filename = f'{STORE_FOLDER}{slugify(instance.store_name)}-{datetime.datetime.now()}.{file_extension}'

    return _filename


def product_image_handler(instance, filename, *args, **kwargs):
    file_extension = filename.split('.')[-1]
    _filename = f'{PRODUCT_FOLDER}{slugify(instance.product_name)}-{datetime.datetime.now()}.{file_extension}'

    return _filename
