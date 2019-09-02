from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users'
    )
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return str(self.user)
