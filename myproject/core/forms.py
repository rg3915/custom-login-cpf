from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AccountForm(forms.Form):
    cpf = forms.CharField(label='CPF', max_length=14)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ('cpf', 'password')


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'CPF'
        self.fields['username'].verbose_name = 'CPF'
