from rest_framework import serializers

from cart.models import Cart, CartItem
from store.models import ProductOption, Product
from accounts.serializers import UserSerializer


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        exclude = ['id']
        depth = 2


class CartSerializer(serializers.ModelSerializer):

    cart_user = UserSerializer()
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        exclude = ['id']
        depth = 1


class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        exclude = [
            'id',
            'cart_slug'
        ]


class CartItemOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOption
        fields = [
            'option_slug'
        ]


class CartItemUpdateSerializer(serializers.ModelSerializer):

    cart_item = serializers.SlugField()

    class Meta:
        model = CartItem
        fields = [
            'cart_item',
            'cart_item_quantity',
            'cart_item_description',
            'cart_item_options'
        ]

    def validate_cart_item(self, value):
        value = Product.objects.get(product_slug=value)

        return value


class CartUpdateSerializer(serializers.ModelSerializer):

    cart_items = CartItemUpdateSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'cart_items'
        ]
        depth = 1

    def update(self, instance, validated_data):
        for item in validated_data['cart_items']:
            _item = {
                'cart_item': item['cart_item']
            }
            qs_exists = instance.cart_items.filter(**_item).exists()

            if qs_exists:
                cart_item = instance.cart_items.get(**_item)
                if item.get('cart_item_quantity'):
                    cart_item.cart_item_quantity = item.get('cart_item_quantity')
                    cart_item.save()
                else:
                    instance.cart_items.remove(cart_item)
            else:
                cart_item = instance.cart_items.create(**item)
                cart_item.save()
                instance.cart_items.add(cart_item)

        instance.save()

        return instance
