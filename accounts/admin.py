# imports
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Permission

from accounts.models import *
# End: imports -----------------------------------------------------------------

# Actions for Admin-site:
def make_normal(modeladmin, request, queryset):
    queryset.update(is_staff=False)
    queryset.update(is_superuser=False)
    make_normal_user.short_description = "Mark selected users as normal users without any permissions"

def make_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=False)
    make_staff.short_description = "Mark selected users as is_staff"

def make_superuser(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=True)
    make_superuser.short_description = "Mark selected users as is_superuser"

class UserAdmin(auth_admin.UserAdmin):
    # User forms
    form = auth_admin.UserChangeForm
    add_form = auth_admin.UserCreationForm # Important!
    change_password_form = auth_admin.AdminPasswordChangeForm

    # Fields shown in user detail: admin/accounts//user/'id'/change
    fieldsets = [
        [None,              {'fields': ['password']}],
        ['Personal info',   {'fields': ['first_name', 'last_name', 'email', 'department' ] }],
        ['Permissions',     {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}],
        ['Important dates', {'fields': ['last_login', 'date_joined']}],
    ]
    # No idea what this is for
    limited_fieldsets = [
        [None,              {'fields':   ['email',]}],
        ['Personal info',   {'fields': ['first_name', 'last_name']}],
        ['Important dates', {'fields': ['last_login', 'date_joined']}],
    ]
    # Not sure what this is for
    add_fieldsets = [
        [None, {
            'classes': ['wide',],
            'fields': ['email', 'first_name', 'last_name', 'password1', 'password2']}
        ],
    ]

    list_display = ['email', 'first_name', 'last_name', 'department', 'sex', 'workout_sum_points', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'department', 'sex']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['email']
    readonly_fields = ['last_login', 'date_joined']
    filter_horizontal = ['groups', 'user_permissions']
    actions = [make_normal, make_staff, make_superuser]


class PermissionCodeAdmin(admin.ModelAdmin):
    list_display = ['group', 'secret']
    list_filter = ['group']
    search_fields = ['group', 'secret']
    ordering = ['-id']
    readonly_fields = []
    filter_horizontal = []
    actions = []


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'member_count', 'workout_sum_km', 'workout_sum_points', 'workout_avg_points']
    list_filter = []
    search_fields = ['name', 'short_name']
    ordering = ['-id']
    readonly_fields = []
    filter_horizontal = []
    actions = []


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(PermissionCode, PermissionCodeAdmin)
admin.site.register(Department, DepartmentAdmin)
