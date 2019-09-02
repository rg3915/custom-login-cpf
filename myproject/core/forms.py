from django import forms


class AccountForm(forms.Form):
    cpf = forms.CharField(label='CPF', max_length=14)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ('cpf', 'password')
