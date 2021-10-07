from rest_framework.test import APITestCase
from django.urls import reverse

from django.contrib.auth.models import User
from employees.models import Employee
from rooms.models import MeetingRoom
from reservations.models import RoomBooking


class TestRoomReservationsViews(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='Password')
        self.user_second = User.objects.create_user(username='username1', password='Password1')
        self.client.force_authenticate(self.user)
        # self.client.force_authenticate(self.user_second)

        self.room = MeetingRoom.objects.create(title='Casper')

        self.emp1 = Employee.objects.create(first_name='Andrius', last_name='steels', account=self.user)
        self.emp2 = Employee.objects.create(first_name='Tom', last_name='max', account=self.user_second)
    

        self.reservation_data = {
            'title':'Party Meeting',
            'date_from': '2021-11-01',
            'date_to': '2021-11-02',
            'room': self.room.id,
            'employees': [self.emp1.id, self.emp2.id]
        }


        self.url_name = reverse('reservations:create_reservation')

    def test_create_reservation(self):
        response = self.client.post(self.url_name,  self.reservation_data, format='json')
        expected = RoomBooking.objects.first()



        self.assertEqual(response.status_code, 201)
        # self.assertEqual(User.objects.count(), 1)
        self.assertEqual(f'{expected.title}', 'Party Meeting')
