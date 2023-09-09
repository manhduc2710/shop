from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Tài khoản", max_length=30, widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Enter your username"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={"class": 'form-control form-control-lg', 'placeholder': 'Enter a valid email address'}))
    password1 = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Nhập lại mật Khẩu', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter password again'}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Mật khẩu Không hợp lệ')

    def clean_username(self):
        username = self.cleaned_data["username"]
        #  r'^\w+$' ký tự đặc biệt
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tài khoản có ký tự đặc biệt ')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            # Lỗi username tồn tại
            return username
            # không có lỗi thì trong data đã có user
        raise forms.ValidationError('Tài khoản đã tồn tại')

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password1'])
