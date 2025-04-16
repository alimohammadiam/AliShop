from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=255, verbose_name='نام')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ')
    description = models.TextField(max_length=1200, verbose_name='توضیحات')
    inventory = models.PositiveIntegerField(default=0, verbose_name='تعداد')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت نهایی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    update = models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    value = models.CharField(max_length=255, verbose_name='مقدار')
    product = models.ForeignKey('Product', related_name='features', on_delete=models.CASCADE, verbose_name='محصول')

    def __str__(self):
        return f'{self.name} : {self.value}'


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='image', on_delete=models.CASCADE, verbose_name='محصول')
    file = models.ImageField(upload_to='product_images/%Y%m%d/')
    title = models.CharField(max_length=250, verbose_name='', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'





















