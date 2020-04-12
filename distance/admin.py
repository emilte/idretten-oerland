from django.contrib import admin

from distance import models as distance_models

# Register your models here.

class WorkoutAdmin(admin.ModelAdmin):

    list_display = ['user', 'type', 'distance', 'points']
    list_filter = ['type', 'user__department']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    ordering = ['-id']
    readonly_fields = []
    filter_horizontal = []
    actions = []

admin.site.register(distance_models.Workout, WorkoutAdmin)
