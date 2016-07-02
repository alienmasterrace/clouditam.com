from django import forms
from django.contrib.auth import get_user_model


class SignUpForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        exclude = []


class SignInForm(forms.Form):
    username_or_email = forms.CharField(max_length=512)
    passwrd = forms.CharField(max_length=32)
