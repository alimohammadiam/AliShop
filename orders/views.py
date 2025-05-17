from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneVerificationForm
from account.models import ShopUser
import random
from django.contrib.auth import login
from cart.common.KaveSms import send_sms_with_template

# Create your views here.+


def verify_phone(request):
    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if ShopUser.objects.filter(phone=phone).exists():
                messages.error(request, 'this phone is already registered.')
                return redirect('orders:verify_phone')
            else:
                tokens = {'token': ''.join(random.choices('0123456789', k=6))}
                request.session['verification_code'] = tokens['token']
                request.phone = phone
                print(tokens)
                # send_sms_with_template('09925126890', tokens, 'verify')
                messages.error(request, 'verification code send successfully.')
                return redirect('orders:verify_code')
    else:
        form = PhoneVerificationForm()
    return render(request, 'verify_phone.html', {'form': form})


def verify_code(request):
    pass
