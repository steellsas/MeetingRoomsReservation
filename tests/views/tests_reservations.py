from rest_framework.test import APITestCase
from django.urls import reverse

from django.contrib.auth.models import User
from employees.models import Employee
from rooms.models import MeetingRoom
from reservations.models import RoomBooking


class TestRoomReservationsViews(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='username', password='Password')
        self.user_2 = User.objects.create_user(username='username2', password='Password2')
        self.user_3 = User.objects.create_user(username='username3', password='Password3')
        self.user_4 = User.objects.create_user(username='username4', password='Password4')
        self.user_5 = User.objects.create_user(username='username5', password='Password5')

        self.client.force_authenticate(self.user)

        self.room = MeetingRoom.objects.create(title='Casper')
        self.room2 = MeetingRoom.objects.create(title='Home')

        self.emp1 = Employee.objects.create(first_name='Andrius', last_name='steels', account=self.user)
        self.emp2 = Employee.objects.create(first_name='Tom', last_name='max', account=self.user_2)
        self.emp3 = Employee.objects.create(first_name='Ben', last_name='Beard', account=self.user_3)
        self.emp4 = Employee.objects.create(first_name='Dick', last_name='Dikins', account=self.user_4)
        self.emp5 = Employee.objects.create(first_name='Zero', last_name='one', account=self.user_5)

        self.reservation1 = RoomBooking.objects.create(
            title='Meeting 1', date_from='2021-11-10',date_to='2021-11-12', room=self.room)
        self.reservation1.employees.add(self.emp1)


        self.reservation2 = RoomBooking.objects.create(
            title='Meeting', date_from='2021-10-22', date_to='2021-10-24', room=self.room)
        self.reservation2.employees.add(self.emp1, self.emp5, self.emp4)

        self.reservation3 = RoomBooking.objects.create(
            title='Meeting3', date_from='2021-10-28', date_to='2021-10-29', room=self.room)
        self.reservation3.employees.add(self.emp1, self.emp5, self.emp4)

        self.reservation4 = RoomBooking.objects.create(
            title='Meeting4', date_from='2021-11-28', date_to='2021-11-29', room=self.room2)
        self.reservation4.employees.add(self.emp1, self.emp5, self.emp3)


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
        expected = RoomBooking.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(f'{expected.title}', 'Party Meeting')

    def test_all_reservations(self):
        self.url_name_all=reverse('reservations:reservations-all')
        response = self.client.get(self.url_name_all)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        # [print(item) for item in response.data]

    def test_room_reservations(self):
        self.url_room_reservations=reverse('reservations:room_reservations', kwargs={'room_id': self.room.id})
        response = self.client.get(self.url_room_reservations)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        # [print(item) for item in response.data

    def test_employee_in_room_reservations(self):

        pass

    # def test_blog_text(self):
    #     self.assertEqual(RoomBooking.objects.filter(room__id=1).count(), 1)

    def test_test_employee_crested(self):
        pass


        # self.useris = UserFactory.create()
        # self.employee_1 = EmployeeFactory()
        # self.employee_2 = EmployeeFactory()
        # self.room10 =MeetingRoomFactory()
        # # print(self.employee_1.id)
        # print(vars(self.employee_2))

        # test_reservations = RoomBooking.objects.create(
        #     title='testas', date_from='2021-11-01', date_to='2021-11-02', room=self.room)
        # test_reservations.employees.add(self.employee_1)

        # self.reservation = RoomBookingFactory.create(employees=(1,2,3))
        # self.reservation = RoomBookingFactory()  #employees.set(self.employee_1)
        employees_list = Employee.objects.all()


        # tt = Employee.objects.get(pk=(self.employee_1.id))
        # print(tt)
        # self.reservation.employees.add(Employee.objects.get(pk=(self.employee_1.id)))


        # self.reservation.employees.set(self.employee_1)

        # # print(self.employee_1.first_name)
        # print(self.reservation.date_from, self.reservation.room, self.reservation.employees)

        # def test_ten_rooms(self):
        #     for i in range(10):
        #         data_room =MeetingRoomFactory()

        # response = self.client.get(reverse('room-list'))
        # self.assertEqual(response.status_code,200)
        # print(response.data)
        # self.assertEqual(len(response.data), 10)

