from django.views import View
from django.shortcuts import render, redirect
from distance import forms as distance_forms

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
            form.save()
            return redirect('distance:register')

        return render(request, self.template, {'form': form})
