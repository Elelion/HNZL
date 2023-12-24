from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, redirect

from .forms import LoginForm


def index(request):
    # Проверяем, авторизован ли пользователь
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('patients:browse'))

    # Если метод запроса POST, обрабатываем форму входа
    if request.method == 'POST':

        # Создаем экземпляр формы LoginForm и передаем введенные данные из POST-запроса
        form = LoginForm(request.POST)

        if form.is_valid():
            # Получаем введенное имя пользователя и пароль из формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Проверяем данные пользователя с помощью функции authenticate()
            user = authenticate(request, username=username, password=password)

            # Если пользователь существует и данные верны
            if user is not None:
                # Выполняем вход пользователя с помощью функции login()
                # login(request, user)
                auth.login(request, user)

                # return redirect('/patients/')
                return HttpResponseRedirect(reverse('patients:browse'))
            else:
                # добавляем ошибку к полю 'username'
                form.add_error('username', 'Не верный логин или пароль')
    else:
        # Если метод запроса GET, создаем новый экземпляр формы LoginForm
        form = LoginForm()

    # Рендерим шаблон 'login/index.html' с передачей формы в контекст шаблона
    return render(request, 'login/index.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))
