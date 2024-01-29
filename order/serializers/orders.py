from django.db.models import fields
from rest_framework import serializers
from order.models.orders import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
