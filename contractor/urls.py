from django.urls import path
from .views import register_contractor, contractor_profile

urlpatterns = [
    path('register/', register_contractor, name='register_contractor'),
    path('profile/', contractor_profile, name='contractor_profile'),
]
