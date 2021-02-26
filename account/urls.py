from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("login/", Login.as_view(), name="home"),
    path("register/", Registration.as_view(), name="Registration"),
    path("auth/", LoginAndReg.as_view(), name="LoginAndReg"),
    path("profile/<int:pk>/", Profile.as_view(), name="Profile"),
]
