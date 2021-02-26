from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView

from account.forms import UserRegistrationForm
from account.models import User

import qrcode


def create_qr(uid):
    # имя конечного файла
    filename = f"user{uid}.png"
    # генерируем qr-код
    img = qrcode.make(uid)
    img.save(f"static/{filename}")
    # Привязываем QR код к пользователю
    user = User.objects.get(id=uid)
    user.qr_path = filename
    user.save()


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
        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Ваш аккаунт еще не активировали')
        else:
            return HttpResponse('Invalid data')
        return redirect("/login")


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
            create_qr(new_user.id)
            return redirect("/login")
        else:
            return HttpResponse("Invalid data")


class LoginAndReg(TemplateView):
    template_name = "page/authAndReg.html"


class Profile(DetailView):
    template_name = "page/profile.html"
    model = User
