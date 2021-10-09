from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from reservations.models import RoomBooking
from reservations.serializers import RoomBookingSerializer


class BookingRoomViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated]


class ReservationsByRoomViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request,*args,**kwargs):
        room_id = kwargs['room_id']
        reservations_by_room = RoomBooking.objects.filter(room=room_id)
        serializer = RoomBookingSerializer(reservations_by_room, many=True)
        return Response(serializer.data)


class RoomReservationsByEmployeeViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request,*args,**kwargs):
        employee_id = kwargs['pk']
        room_reservations = RoomBooking.objects.filter(employees__id=employee_id)
        serializer = RoomBookingSerializer(room_reservations, many=True)
        return Response(serializer.data)

