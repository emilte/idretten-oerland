
from django.urls import path
from . import views

app_name = 'emil'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]


# localhost:8000/distanse/registrering
