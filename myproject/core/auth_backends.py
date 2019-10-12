from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect
from django.urls import reverse

User = get_user_model()


class CpfBackend(ModelBackend):

    def authenticate(self, request, username, password=None, **kwargs):
        try:
            user = User.objects.get(profile__cpf=username)
        except User.DoesNotExist:
            User().set_password(password)
            messages.error(request, 'CPF não existe.')
        else:
            if (
                user.check_password(password)
                and self.user_can_authenticate(user)
            ):
                return user
            else:
                messages.error(request, 'Senha inválida.')
                return
