from rest_framework import serializers
from shop.models import Product, ProductFeature


class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeaturesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'new_price', 'features']
