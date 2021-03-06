# imports
import json

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


from distance import models as distance_models
# End: imports -----------------------------------------------------------------

class PermissionCode(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    secret = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"PermissionCode ({self.group}:{self.secret})"

class UserManagerOld(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return use

class Department(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False, verbose_name="Avdeling", unique=True)
    short_name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Forkortelse")

    class Meta:
        ordering = ['name']
        verbose_name = "Avdeling"
        verbose_name_plural = "Avdelinger"

    def __str__(self):
        return self.short_name

    def member_count(self):
        return self.users.all().count()

    def workout_sum_km(self):
        km = 0
        for member in self.users.all():
            km += member.workout_sum_km()
        return round(km, 1)

    def workout_sum_points(self):
        points = 0
        for member in self.users.all():
            points += member.workout_sum_points()
        return round(points, 1)

    def workout_avg_points(self):
        try:
            return round(self.workout_sum_km()/self.member_count(), 1)
        except Exception as e:
            return None


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, employee_nr, password=None, **kwargs):
        if not employee_nr:
            raise ValueError('Users must have an employee number')
        user = self.model(employee_nr=employee_nr, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_nr, password, **kwargs):
        user = self.create_user(employee_nr=employee_nr, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return use


class User(AbstractBaseUser, PermissionsMixin):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    SEX_CHOICES = [
        (None, "-----"),
        (MALE, "Mann"),
        (FEMALE, "Kvinne"),
        (OTHER, "Annet"),
    ]
    # email = models.EmailField(max_length=254, unique=True)
    employee_nr = models.PositiveIntegerField(unique=True, verbose_name="Ansatt nummer")
    # first_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="Fornavn")
    # last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Etternavn")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Avdeling", related_name="users")
    nickname = models.CharField(max_length=150, unique=True, null=True, blank=False, verbose_name="Kallenavn")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=None, null=True, blank=True, verbose_name="Kjønn")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, blank=True, editable=False, verbose_name="Opprettet")

    objects = UserManager()

    USERNAME_FIELD = 'employee_nr'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['employee_nr']

    def __str__(self):
        return f"{self.employee_nr} - {self.nickname}"

    def get_full_name(self):
        return "deprecated: get_full_name"

    def get_username(self):
        return self.employee_nr

    def get_short_name(self):
        return "deprecated: get_short_name"

    def workout_sum_km(self):
        km = self.workouts.all().aggregate(result=Sum('distance'))['result'] or 0
        return round(km, 1)

    def workout_sum_points(self):
        points = 0
        for workout in self.workouts.all():
            points += workout.points()
        return round(points, 1)

    def serialize(self):
        jayson = {}
        jayson['id'] = self.id
        # jayson['email'] = self.email
        jayson['nickname'] = self.nickname
        jayson['first_name'] = self.first_name
        jayson['last_name'] = self.last_name
        jayson['department'] = self.department
        jayson['is_staff'] = self.is_staff
        jayson['is_superuser'] = self.is_superuser
        return jayson
