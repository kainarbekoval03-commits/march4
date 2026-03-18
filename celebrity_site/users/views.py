from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import SignInForm, SignUpForm

# Create your views here.

# авторизация - проверка доступа
# аунтентификация - проверка пользователя в базе данных
# регистрация - сохранение в базе данных



def sign_up(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request=request, template_name="users/sign_up.html", context={"form": form})
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Error data")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        return redirect("/users/sign-in/")
    

def sign_in(request):
    if request.method == "GET":
        form = SignInForm()
        return render(request=request, template_name="users/sign_in.html", context={"form": form})
    elif request.method == "POST":
        form = SignInForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Error data")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return redirect("/")
        return HttpResponse("Error")
    
def sign_out(request):
    logout(request)
    return redirect("/")