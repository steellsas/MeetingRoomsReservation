from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestAccount(APITestCase):

    def setUp(self):
        self.user = User
        self.data = {
            'email': 'email@gmail.com',
            'username': 'pirmasuseris ',
             'password': 'emailemail'
            }
        self.url_name ="accounts:user_register"

    def test_create_account(self):

        url = reverse(self.url_name)
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'email@gmail.com')
        self.assertEqual(User.objects.get().username, 'pirmasuseris')
