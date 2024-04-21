# customer/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'contact_info', 'experience', 'email', 'password1', 'password2']
