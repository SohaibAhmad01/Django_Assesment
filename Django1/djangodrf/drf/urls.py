from django.urls import path
from . import views


urlpatterns = [
    path('', views.Simple, name="simple view"),
]