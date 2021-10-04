from rest_framework import viewsets
from rest_framework.response import Response

from reservations.models import RoomBooking
from employees.models import Employee
from reservations.serializers import RoomBookingSerializer


class BookingRoomViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = []


class ReservationsByRoomViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = []

    def retrieve(self, request,*args,**kwargs):
        room_id = kwargs['pk']
        reservations_by_room = RoomBooking.objects.filter(room=room_id)
        serializer = RoomBookingSerializer(reservations_by_room, many=True)
        return Response(serializer.data)


class RoomReservationsByEmployeeViewSet(viewsets.ModelViewSet):
    queryset =RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = []

    def retrieve(self, request,*args,**kwargs):
        employee_id = kwargs['pk']
        room_reservations = RoomBooking.objects.filter(employees__id=employee_id)
        serializer = RoomBookingSerializer(room_reservations, many=True)
        return Response(serializer.data)

# # @api_view(['GET'])
# def get_images_mask_result(request, room_id):
#     queryset = RoomBooking.objects.filter(room__id=room_id).order_by('employees__first_name')
#     message ="test"
#     return Response({'room_reservation': massage})


# group = {'id': 50, 'employee': [{'id': 1}, {'id': 5}]}var(q)
# filter room reservaition where are employee_id
# res_by_emp = RoomBooking.objects.filter(employees__id=3)
# room_reervations3 = RoomBooking.objects.filter(room=3)
