from django.urls import path
from .views import register_customer, customer_profile

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('profile/', customer_profile, name='customer_profile'),
]
