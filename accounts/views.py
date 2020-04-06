# imports
# import spotipy.oauth2 as oauth2

from django.views import View
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test

from accounts import models as account_models
from accounts import forms as account_forms

User = get_user_model()
# End: imports -----------------------------------------------------------------

profile_dec = [
    login_required,
]

@method_decorator(profile_dec, name='dispatch')
class ProfileView(View):
    template = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})



@method_decorator(profile_dec, name='dispatch')
class EditProfileView(View):
    template = "accounts/edit_profile.html"
    form_class = account_forms.EditUserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            return render(request, self.template, {'form': form})

class SignUpView(View):
    template = "accounts/registration_form.html"
    form_class = account_forms.SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('stefan:index')
        else:
            return render(request, self.template, {'form': form})


@method_decorator(profile_dec, name='dispatch')
class DeleteUserView(View):

    def get(self, request, *args, **kwargs):
        request.user.delete()
        logout(request)
        return redirect('home')


class LoginView(View):
    template = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        error = None
        if user is not None:
            login(request, user)
            return redirect('accounts:login')
        else:
            error = "Feil"

        return render(request, self.template, {'error': error})



@method_decorator(profile_dec, name='dispatch')
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


@method_decorator(profile_dec, name='dispatch')
class ChangePasswordView(View):
    template = "accounts/change_password.html"
    form_class = account_forms.CustomPasswordChangeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.user)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect("accounts:profile")
        return render(request, self.template, {'form': form})
