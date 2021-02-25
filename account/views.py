from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView

from account.forms import UserRegistrationForm
from account.models import User


# Авторизация пользователя
class Login(TemplateView):
    template_name = "page/auth.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get("login")
        password = request.POST.get("password")
        print(username, password)
        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid data')
        return redirect("/pizda")


class Registration(TemplateView):
    template_name = "page/register.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Registration, self).get_context_data()
        context["form"] = UserRegistrationForm()
        return context

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect("/login")
        else:
            return HttpResponse("Invalid data")


class LoginAndReg(TemplateView):
    template_name = "page/authAndReg.html"
