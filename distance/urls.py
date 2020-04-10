
from django.urls import path
from . import views

app_name = 'distance'

urlpatterns = [
    path('registrering/', views.Register.as_view(), name='register'),
    path('resultater/', views.Results.as_view(), name='results'),
    path('statistikk/', views.Stats.as_view(), name='stats'),
]


# localhost:8000/distanse/registrering
