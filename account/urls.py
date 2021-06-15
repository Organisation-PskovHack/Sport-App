from django.urls import path
from .views import *
from account.views import *

app_name = "account"

urlpatterns = [
    path('role/', GetRoleView.as_view(), name='get-role'),
]
