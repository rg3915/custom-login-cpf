from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import UserProfile

User = get_user_model()


class TestLoginView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='walison',
            password='10203040'
        )
        UserProfile.objects.create(user=self.user, cpf='25197394013')

    def test_template(self):
        response = self.client.get('/login/')

        self.assertTemplateUsed(response, 'core/auth.html')

    def test_contains_expected_fields(self):
        response = self.client.get('/login/')

        self.assertContains(response, 'CPF')
        self.assertContains(response, 'Senha')
        self.assertContains(response, 'Login')

    def test_success_login(self):
        valid_credentials = {'username': '25197394013', 'password': '10203040'}
        response = self.client.post('/login/', data=valid_credentials, follow=True)

        user = response.context['user']

        self.assertRedirects(response, '/')
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user, self.user)

    def test_failed_login(self):
        invalid_credentials = {'username': '0000000000', 'password': '10203040'}
        response = self.client.post('/login/', data=invalid_credentials, follow=True)

        user = response.context['user']

        self.assertFalse(user.is_authenticated)
        self.assertNotEqual(user, self.user)
