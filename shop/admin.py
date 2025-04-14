from django.contrib import admin
from .models import Product, Category, Image, ProductFeature

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class FeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory', 'new_price', 'created', 'update']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'update']
    inlines = [ImageInline, FeatureInline]
