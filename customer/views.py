# customer/views.py

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib import messages
from .models import Customer


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(user=user)
            login(request, user)
            return redirect('customer_profile')
        else:
            messages.error(request, 'Пользователь с такими данными уже существует.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form})


def customer_profile(request):
    if not request.user.is_authenticated:
        return redirect('customer_login')
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return render(request, 'errors/no_profile.html')
    return render(request, 'customer/profile.html', {'customer': customer})
