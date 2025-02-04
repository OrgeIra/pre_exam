from django.urls import path
from ecommerce import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_detail', views.product_detail, name='product_detail'),
    path('customers', views.customers, name='customers'),
    path('customer-details', views.custome_details, name='customer-details')
]
