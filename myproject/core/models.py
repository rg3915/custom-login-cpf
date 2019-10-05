from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return str(self.user)
