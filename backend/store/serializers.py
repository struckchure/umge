from rest_framework import serializers

from store.models import Store, Product, ProductOption


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = ['id']


class StoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        exclude = [
            'id',
            'store_staffs',
            'store_slug'
        ]

    def validate(self, validated_data):

        store_name = validated_data.get('store_name')

        qs = Store.objects.filter(store_name=store_name)

        if qs.exists():
            message = f'Store with name {store_name} already exist'
            raise serializers.ValidationError(message)

        return validated_data


class StoreUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        exclude = [
            'id',
            'store_staffs',
            'store_slug'
        ]


class ProductOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOption
        exclude = [
            'id'
        ]


class ProductOptionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOption
        exclude = [
            'option_slug'
        ]


class ProductSerializer(serializers.ModelSerializer):

    product_price = serializers.SerializerMethodField()
    product_options = ProductOptionSerializer(many=True)
    product_store = StoreSerializer()

    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'product_type',
            'product_image',
            'product_slug',
            'product_options',
            'product_store'
        ]
        # depth = 1

    def get_product_price(self, product):
        return product.get_total_price()


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = [
            'id',
            'product_slug'
        ]
