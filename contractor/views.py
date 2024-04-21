# contractor/views.py

from django.shortcuts import render, redirect
from .forms import ContractorRegistrationForm
from django.contrib.auth import login


def register_contractor(request):
    if request.method == 'POST':
        form = ContractorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contractor_profile')
    else:
        form = ContractorRegistrationForm()
    return render(request, 'contractor/register.html', {'form': form})


def contractor_profile(request):
    return render(request, 'contractor/profile.html')
