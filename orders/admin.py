from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'first_name', 'last_name', 'phone', 'address', 'postal_code', 'province', 'city', 'paid',
                    'created', 'update']
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]
