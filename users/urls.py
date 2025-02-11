from django.urls import path
from users import views



urlpatterns = [
    path('', views.customer_list, name='customer-list'),
    path('customer-details/', views.customer_detail, name='customer-details'),
    path('customer-create/', views.add_customer, name='add-customer'),
    path('customer-update/<int:pk>/', views.update_customer, name='customer_update'),      
    path('customer-delete/<int:pk>/', views.delete_customer, name='delete_customer'),
]
