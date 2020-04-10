from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


from distance import forms as distance_forms
from distance import models as distance_models
from accounts import models as account_models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

register_dec = [
    login_required,
    permission_required('distance.add_workout', login_url='forbidden'),
]
@method_decorator(register_dec, name='dispatch')
class Register(View):
    form_class = distance_forms.WorkoutForm
    template = 'distance/workout_form.html'

    def get(self, request):
        form = self.form_class() # instans av RegisterForm
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST) # instans av RegisterForm

        if form.is_valid():
            answer = form.save()
            answer.user = request.user
            answer.save()
            messages.add_message(request, messages.SUCCESS, 'Økten ble lagret')
            return redirect('stefan:index')

        return render(request, self.template, {'form': form})



results_dec = [
    login_required,
    permission_required('distance.view_workout', login_url='forbidden'),
]
@method_decorator(results_dec, name='dispatch')
class Results(View):
    template = 'distance/results.html'

    def get(self, request):
        results = distance_models.Workout.objects.all()
        users = User.objects.all()
        Workout = distance_models.Workout
        return render(request, self.template, {
            'results': results,
            'users': users,
            'Workout': Workout,
        })
stats_dec = [
    login_required,
    permission_required('distance.view_workout', login_url='forbidden'),
]
@method_decorator(results_dec, name='dispatch')
class Stats(View):
    template = 'distance/stats.html'

    def get(self, request):
        departments = account_models.Department.objects.all()
        department_points = {
        }

        for department in departments:
            users = department.users.all()
            sum_points = 0
            for user in users:
                sum_points += user.workout_points()
            department_points[department.name] = sum_points

        return render(request, self.template, {
            'department_points': department_points,
        })
