from django.views import View
from django.shortcuts import render, redirect

from distance import forms as distance_forms
from distance import models as distance_models

# Create your views here.

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


class Results(View):
    template = 'distance/results.html'

    def get(self, request):
        results = distance_models.Registrering.objects.all()
        return render(request, self.template, {'results': results})
