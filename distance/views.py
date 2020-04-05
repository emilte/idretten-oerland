from django.views import View
from django.shortcuts import render


# Create your views here.

class Register(View):

    template = 'distance/distance_form.html'

    def get(self, request):
        return render(request, self.template)
