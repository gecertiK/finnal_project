from django import forms
from django.core.exceptions import ValidationError

from .models import Order


def validate_order_exists(value):
    incident = Order.objects.filter(transaction_id=value)
    if not incident:
        raise ValidationError('No such order')


class OrderForm(forms.Form):
    order_number = forms.CharField(max_length=50, required=True, validators=[validate_order_exists])
