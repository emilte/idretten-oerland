from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from distance import forms as distance_forms
from distance import models as distance_models

# Create your views here.

Register_dec = [
    login_required,
]
@method_decorator(Register_dec, name='dispatch')
class Register(View):
    form_class = distance_forms.RegistreringForm
    template = 'distance/distance_form.html'

    def get(self, request):
        form = self.form_class() # instans av RegisterForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST) # instans av RegisterForm

        if form.is_valid():
            answer = form.save()
            answer.user = request.user
            answer.save()
            return redirect('stefan:index')

        return render(request, self.template, {'form': form})

Results_dec = [
    login_required,
]
@method_decorator(Results_dec, name='dispatch')
class Results(View):
    template = 'distance/results.html'

    def get(self, request):
        results = distance_models.Registrering.objects.all()
        return render(request, self.template, {'results': results})
