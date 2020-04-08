# imports
from django import forms
from django.db.models import Q
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model

from accounts.models import *
from accounts import models as account_models

User = get_user_model()

# End: imports -----------------------------------------------------------------

class SignUpForm(UserCreationForm):

    required_css_class = "required font-bold"
    code = forms.CharField(required=False, label="Kode")

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'nickname',
            'code',
        ]

    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['password1'].help_text = 'Your password cant be too similar to your other personal information. Your password must contain atleast 8 characters. Your password cant be a commonly used password and cant be entierly numeric.'

class EditUserForm(forms.ModelForm):

    required_css_class = "required font-bold"

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'nickname',
            'department',
        ]


    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


# Possible to customise login:
class CustomAuthenticationForm(AuthenticationForm): # Not currently in use. Can be passed to login view
    error_messages = dict(AuthenticationForm.error_messages) # Inherit from parent. invalid_login and inactive

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(self.error_messages['inactive'], code='inactive')

        if not user.is_authenticated:
            raise forms.ValidationError(self.error_messages['invalid_login'], code='invalid_login')

class CustomAuthForm(AuthenticationForm):
    # Inherited fields:
    # username
    # password
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))


class CustomPasswordChangeForm(PasswordChangeForm):
    # Inherited fields:
    # old_password
    # new_password1
    # new_password2

    class Meta:
        model = User
        exclude = []
        labels = {
            'old_password': 'Gammelt passord',
            'new_password1': 'Nytt passord',
            'new_password2': 'Nytt passord bekreftelse',
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        super(CustomPasswordChangeForm, self).__init__(request.user, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        # self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        # self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        # self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
