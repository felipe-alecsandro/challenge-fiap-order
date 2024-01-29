from django.db.models import fields
from .models.orders import Order

from django import forms
from django.forms.models import BaseInlineFormSet


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'