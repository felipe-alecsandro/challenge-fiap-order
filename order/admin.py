from django.contrib import admin
from order.forms import OrderForm
from .models.orders import Order


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ('id','status', 'created_at', 'updated_at')
    list_filter = ('status',)
    list_per_page = 25
    

#admin.site.register(OrderItems, OrderItemsAdmin)
admin.site.register(Order, OrderAdmin)
