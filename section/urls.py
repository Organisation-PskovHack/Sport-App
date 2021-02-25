from django.urls import path
from .views import *

app_name = "section"

urlpatterns = [
    path("", homePage.as_view(), name="home"),
]
