import math
from operator import itemgetter

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

def getIndexOfTuple(l, index, value):
    for pos,t in enumerate(l):
        if t[index] == value:
            return pos

    # Matches behavior of list.index
    return None

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
        department_points = {}

        for department in departments:
            users = department.users.all()
            sum_points = 0
            for user in users:
                sum_points += user.workout_points()
            department_points[department.name] = sum_points


        return render(request, self.template, {
            'department_points': department_points,
        })


stats_dec = [
    login_required,
    permission_required('distance.view_workout', login_url='forbidden'),
]
@method_decorator(results_dec, name='dispatch')
class Stats2(View):
    template = 'distance/stats_emil.html'

    def get(self, request):
        # Expensive computing
        department_points = []
        your_points = None
        rank = None
        diff = None
        facts = None

        for department in account_models.Department.objects.all():
            sum_points = 0
            for user in department.users.all():
                sum_points += user.workout_points()

            if department.users.all().count() != 0:
                avg = round(sum_points / department.users.all().count(), 1)
            else:
                avg = None

            department_points.append( (department, sum_points, avg) )

            if department == request.user.department:
                your_points = (department, sum_points, avg)

        department_points.sort(key=itemgetter(1), reverse=True)
        first = department_points[0]
        second = department_points[1]
        third = department_points[2]

        for x in range(len(department_points)):
            points_behind = round(department_points[0][1] - department_points[x][1], 1)
            department_points[x] = (*department_points[x], points_behind)

        if request.user.department:
            rank = getIndexOfTuple(department_points, 0, request.user.department)

        if rank:
            diff = round(department_points[0][1] - department_points[rank][1], 1)
            facts = [ round(math.ceil(diff/scale), 1) for scale in distance_models.Workout.POINTS.values() if scale != 0 ]

        # avg = [ (department, round( points / department.users.all().count() , 1) ) for department, points in points_list ]


        return render(request, self.template, {
            'department_points': department_points,
            # 'points_list': points_list,
            'first': first,
            'second': second,
            'third': third,
            'your_points': your_points,
            'rank': rank+1, # Because 0-index
            'diff': diff,
            'facts': facts,
            # 'avg': avg,
        })
