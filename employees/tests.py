

from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from employees.models import Employee


class TestEmployeeViews(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='Password')
        self.client.force_authenticate(self.user)
        self.employee_data = {'first_name': 'Tim', 'last_name': 'Rider', 'account': self.user.id}
        self.url_name = reverse('employees:employee_register')

    def test_create_new_employee(self):
        response = self.client.post(self.url_name, self.employee_data, format='json')
        expected = Employee.objects.first()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(f'{expected.first_name} {expected.last_name}', 'Tim Rider')
