from django.db import models
from rest_framework import serializers
from ecomm.models import Product, Category, Marca
from django.db.models import fields

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "nome",
            "descricao_breve",
            "descricao",
            "stock",
            "peso",
            "comprimento",
            "largura",
            "altura",
            "get_image",
            "get_absolute_url",
            "get_price",
            "get_thumbnail"
        )
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "name",
            "get_absolute_url",
            "products"
        )
class MarcaSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Marca
        fields = (
            "name",
            "get_absolute_url",
            "products"
        )