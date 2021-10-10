
from rooms.models import MeetingRoom
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class TestRoomViews(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='Password')
        self.client.force_authenticate(self.user)
        self.room= {'title': 'casperis'}
        self.url_name = reverse("rooms:create-room")

    def test_create0_room(self):
        response = self.client.post(self.url_name, self.room, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(MeetingRoom.objects.get().title, 'casperis')

    def test_can_create_same_titles(self):

        MeetingRoom.objects.create(title=self.room['title'])
        response = self.client.post(self.url_name, self.room, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['title'][0], 'meeting room with this title already exists.')






