from django.urls import path
from .views import HelloView, CustomToken, HiView

urlpatterns=[
    path('hello/', HelloView.as_view(), name="hello"),
    path('register/',CustomToken.as_view()),
    path('hi/', HiView.as_view()),
]