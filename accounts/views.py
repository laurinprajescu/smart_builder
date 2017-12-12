# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, TradesmanRegistrationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import stripe
from django.contrib.auth import get_user
from .models import User

stripe.api_key = settings.STRIPE_SECRET

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']):
                messages.error(request, "This email is already taken")
            else:
                form.save()
                user = auth.authenticate(email=request.POST.get('email'),
                                         password=request.POST.get('password1'))
                if user:
                    auth.login(request, user)
                    messages.success(request, "You have successfully registered!")
                    return redirect(reverse('home'))
                else:
                    messages.error(request, "Unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'register.html', args)

@login_required(login_url='/login/')
def profile(request):
    if request.user.is_tradesman():
        return render(request, 'tradesmanprofile.html')
    else:
        return redirect(reverse('siteuserprofile'))

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised!")
    else:
        form = UserLoginForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect(reverse('home'))

def tradesman_register(request):
    if request.method == 'POST':
        form = TradesmanRegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']):
                messages.error(request, "This email is already taken")
            else:
                try:
                    customer = stripe.Charge.create(
                        amount=1000,
                        currency="GBP",
                        description=form.cleaned_data['email'],
                        card=form.cleaned_data['stripe_id'],
                    )
                    if customer.paid:
                        form.save()
                        user = auth.authenticate(email=request.POST.get('email'),
                                                 password=request.POST.get('password1'))
                        if user:
                            auth.login(request, user)
                            messages.success(request, "You have successfully registered!")
                            return redirect(reverse('home'))
                        else:
                            messages.error(request, "Unable to log you in at this time!")
                    else:
                        messages.error(request, "We were unable to take a payment with that card!")
                except stripe.error.CardError, e:
                    messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = TradesmanRegistrationForm()
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'tradesmanregister.html', args)