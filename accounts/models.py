# imports
import json

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


from emil import models as emil_models
# End: imports -----------------------------------------------------------------

class PermissionCode(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    secret = models.CharField(max_length=200, null=False, blank=False)

class UserManager(BaseUserManager):
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
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="Fornavn")
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Etternavn")
    department = models.CharField(max_length=140, null=True, blank=True, verbose_name="Avdeling")
    nickname = models.CharField(max_length=150, null=True, blank=False, verbose_name="Kallenavn")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, blank=True, editable=False, verbose_name="Opprettet")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['email']

    def __str__(self):
        return self.get_full_name() or self.email

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return None
        else:
            return self.first_name + " " + self.last_name

    def get_username(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def workout_sum_km(self):
        km = emil_models.Workout.objects.filter(user=self).aggregate(result=Sum('distance'))['result'] or 0
        return round(km , 1)

    def workout_points(self):
        p = 0
        for workout in self.workouts.all():
            if workout.type == emil_models.Workout.STRENGTH:
                p += emil_models.Workout.POINTS[workout.type]
            elif workout.distance:
                p += workout.distance * emil_models.Workout.POINTS[workout.type]
        return round(p, 1)
