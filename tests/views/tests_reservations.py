from rest_framework.test import APITestCase

from django.urls import reverse
from tests.factories.rooms_model_factory import MeetingRoomFactory
from tests.factories.reservations_model_factory import RoomBookingFactory
from tests.factories.employee_model_factory import EmployeeFactory, UserFactory
from django.contrib.auth.models import User
from employees.models import Employee
from rooms.models import MeetingRoom
from reservations.models import RoomBooking


class TestRoomReservationsViews(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='Password')
        self.user_second = User.objects.create_user(username='username1', password='Password1')
        self.client.force_authenticate(self.user)

        self.room = MeetingRoom.objects.create(title='Casper')
        self.room2 = MeetingRoomFactory()


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
        self.assertEqual(f'{expected.title}', 'Party Meeting')

    def test_room_reservations(self):
        pass

    def test_employee_in_room_reservations(self):

        pass

    # def test_blog_text(self):
    #     self.assertEqual(RoomBooking.objects.filter(room__id=1).count(), 1)

    def test_test_employee_crested(self):
        self.useris = UserFactory.create()
        self.employee_1 = EmployeeFactory()
        self.employee_2 = EmployeeFactory()
        # self.reservation = RoomBookingFactory.create(employees=(1,2,3))
        self.reservation = RoomBookingFactory()  #employees.set(self.employee_1)
        # self.reservation.employees.set(self.employee_1)

        print(self.employee_1.first_name)
        print(self.reservation.date_from, self.reservation.room, self.reservation.employees)

    # def test_ten_rooms(self):
    #     for i in range(10):
    #         data_room =MeetingRoomFactory()
    #         print(data_room)

        # response = self.client.get(reverse('room-list'))
        # self.assertEqual(response.status_code,200)
        # print(response.data)
        # self.assertEqual(len(response.data), 10)

