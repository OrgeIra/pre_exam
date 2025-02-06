from django.urls import path
from users import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('customer-details/', views.custome_details, name='customer-details'),
]