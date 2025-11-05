from rest_framework import serializers
from models_manager.models import  Cart,CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model:Cart
        fields:'__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model:CartItem
        fields:'__all__'