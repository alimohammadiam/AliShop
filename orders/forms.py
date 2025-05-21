import re
from django import forms
from django.core.exceptions import ValidationError
from account.models import ShopUser
from .models import Order


class PhoneVerificationForm(forms.Form):
    phone = forms.CharField(max_length=11, label='شماره تلفن')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            raise ValidationError("شماره تلفن الزامی است.")

        # حذف همه کاراکترهای غیرعددی به جز +
        phone = re.sub(r'[^0-9+]', '', phone)

        # بررسی طول شماره
        if len(phone) == 11:
            if not phone.startswith('09'):
                raise ValidationError("شماره تلفن باید با 09 شروع شود.")
        elif len(phone) == 13 and phone.startswith('+989'):
            phone = '0' + phone[3:]  # تبدیل +989 به 09
        else:
            raise ValidationError("شماره تلفن معتبر نیست (طول یا پیش‌شماره نادرست).")

        # بررسی تکراری نبودن شماره (اگر نیاز است)
        if ShopUser.objects.filter(phone=phone).exists():
            raise ValidationError("این شماره تلفن قبلاً ثبت شده است.")

        return phone


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'postal_code', 'province',
                  'city']
