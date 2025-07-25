from django.contrib import admin
from .models import Order, OrderItem
import openpyxl
from django.http import HttpResponse

# Register your models here.


def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='applications/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=orders.xlsx'


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
