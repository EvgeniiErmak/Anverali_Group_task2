# contractor/views.py

from django.contrib.auth.forms import UserCreationForm
from .models import Contractor


class ContractorRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Contractor
        fields = UserCreationForm.Meta.fields + ('contact_info', 'experience', 'email',)
