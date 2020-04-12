# from django.views import View
# from django.shortcuts import render, redirect
# from stefan import forms as stefan_forms
# from stefan import models as stefan_models
#
# # Create your views here.
#
# class Index(View):
#
#     template = 'stefan/index.html'
#
#     def get(self, request):
#         return render(request, self.template)
#
# class Register(View):
#     form_class = stefan_forms.RegistreringForm
#     template = 'stefan/distance_form.html'
#
#     def get(self, request):
#         form = self.form_class() #instans av RegisterForm
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(data=request.POST) #instans av RegisterForm
#
#         if form.is_valid():
#             form.save()
#             return redirect('stefan:index')
#
#         return render(request, self.template, {'form': form})
#
# class Results(View):
#     template = 'stefan/results.html'
#
#     def get(self, request):
#         results = stefan_models.Registrering.objects.all()
#         return render(request, self.template, {'results': results})
