from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase

from ..models import UserProfile

User = get_user_model()


class TestCpfBackend(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='walison',
            password='10203040'
        )
        UserProfile.objects.create(user=self.user, cpf='25197394013')

    def test_authenticate_with_valid_credentials(self):
        self.assertEqual(
            authenticate(username='25197394013', password='10203040'), self.user
        )

    def test_authenticate_with_invalid_credentials(self):
        self.assertIsNone(authenticate(username='000000000000', password='invalid')
