# from django.views import View
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required, permission_required
#
#
# from emil import forms as emil_forms
# from emil import models as emil_models
#
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# # Create your views here.
# class Index(View):
#
#     template = 'emil/index.html'
#
#     def get(self, request):
#         return render(request, self.template)
#
#
#
# register_dec = [
#     login_required,
#     permission_required('emil.add_workout', login_url='forbidden'),
# ]
# @method_decorator(register_dec, name='dispatch')
# class Register(View):
#     form_class = emil_forms.WorkoutForm
#     template = 'emil/workout_form.html'
#
#     def get(self, request):
#         form = self.form_class() # instans av RegisterForm
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(data=request.POST) # instans av RegisterForm
#
#         if form.is_valid():
#             answer = form.save()
#             answer.user = request.user
#             answer.save()
#             messages.add_message(request, messages.SUCCESS, 'Økten ble lagret')
#             return redirect('stefan:index')
#
#         return render(request, self.template, {'form': form})
#
#
#
# results_dec = [
#     login_required,
#     permission_required('emil.view_workout', login_url='forbidden'),
# ]
# @method_decorator(results_dec, name='dispatch')
# class Results(View):
#     template = 'emil/results.html'
#
#     def get(self, request):
#         results = emil_models.Workout.objects.all()
#         users = User.objects.all()
#         Workout = emil_models.Workout
#         return render(request, self.template, {
#             'results': results,
#             'users': users,
#             'Workout': Workout,
#         })
