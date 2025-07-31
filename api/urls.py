from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'api'


router = DefaultRouter()
router.register(r'products', views.ProductViewSets)

urlpatterns = [
    # path('products/', views.ProductListAPIView.as_view(), name='products_list_api'),
    # path('product/<pk>/', views.ProductDetailAPIView.as_view(), name='products_detail_api'),
    path('users/', views.UserListAPIView.as_view(), name='user_list_api'),
    path('register/', views.UserRegistrationAPIView.as_view(), name='register_api'),
    path('', include(router.urls)),
    path('orders/', views.OrderListAPIView.as_view(), name='order_list_api'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='order_detail_api'),

]
