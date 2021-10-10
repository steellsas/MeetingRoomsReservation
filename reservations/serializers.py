from rest_framework import serializers
from reservations.models import RoomBooking


class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = ('id', 'title', 'date_from', 'date_to', 'room', 'employees')

