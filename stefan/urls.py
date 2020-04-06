
from django.urls import path
from . import views

app_name = 'stefan'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('registrer/', views.Register.as_view(), name='register'),


]


# localhost:8000/distanse/registrering
