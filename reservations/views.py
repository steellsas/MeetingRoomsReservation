from rest_framework import viewsets
from rest_framework import serializers
from reservations.models import RoomBooking
from employees.models import Employee
from reservations.serializers import RoomBookingSerializer


class BookingRoomViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = []



# group = {'id': 50, 'employee': [{'id': 1}, {'id': 5}]}
