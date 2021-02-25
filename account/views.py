from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView

from account.models import User


# Авторизация пользователя
class Login(TemplateView):
    template_name = "page/auth.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get("login", None)
        password = request.POST.get("password", None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid data')


class Registration(TemplateView):
    template_name = None

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")

    def post(self, request):
        username = request.POST.get("login", None)
        password = request.POST.get("password", None)
        password_again = request.POST.get("password_again", None)
        if username and password and password_again:
            if password == password_again:
                if User.objects.filter(username=username):
                    return HttpResponse('Пользователь с таким именем уже существует.')
                else:
                    user = User()
                    user.username = username
                    user.password = password
                    user.save()
                    return redirect("/login")
            else:
                return HttpResponse("Invalid data")
        else:
            return HttpResponse("Invalid data")

