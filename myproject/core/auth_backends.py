from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CpfBackend(ModelBackend):
    def authenticate(self, request, username, password=None, **kwargs):
        try:
            user = User.objects.get(profile__cpf=username)
        except User.DoesNotExist:
            User().set_password(password)
        else:
            if (
                user.check_password(password)
                and self.user_can_authenticate(user)
            ):
                return user
