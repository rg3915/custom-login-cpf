from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import UserProfile
from .forms import AccountForm


def home(request):
    return render(request, 'core/index.html')


def authenticate(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data.get('cpf')
            password = form.cleaned_data.get('password')
            user_profile = UserProfile.objects.filter(cpf=cpf).first()
            if user_profile:
                user = User.objects.filter(username=user_profile).first()
                if user:
                    pwd = user.password
            else:
                messages.error(request, 'CPF não existe.')
                return HttpResponseRedirect(reverse('core:home'))
            cpf_valid = (cpf == user_profile.cpf)
            pwd_valid = check_password(password, pwd)
            if cpf_valid and pwd_valid:
                # Faz login
                auth_login(request, user)
                messages.success(request, 'Usuário autenticado com sucesso.')
                return HttpResponseRedirect(reverse('core:home'))
            else:
                messages.error(request, 'Senha não confere.')
                return HttpResponseRedirect(reverse('core:home'))
    else:
        form = AccountForm()

    context = {'form': form}
    return render(request, 'core/auth.html', context)
