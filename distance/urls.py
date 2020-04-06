
from django.urls import path
from . import views

app_name = 'distance'

urlpatterns = [
    path('registrering/', views.Register.as_view(), name='register'),
]


# localhost:8000/distanse/registrering
