from django.views import View
from django.shortcuts import render, redirect
from stefan import forms as stefan_forms

# Create your views here.

class Home(View):

    template = 'main/home.html'

    def get(self, request):
        return render(request, self.template)
