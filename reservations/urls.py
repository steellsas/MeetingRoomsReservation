from django.urls import path
from reservations.views import BookingRoomViewSet, ReservationsByRoomViewSet, RoomReservationsByEmployeeViewSet

app_name = 'reservations'

urlpatterns = [
    path('reservations/create/', BookingRoomViewSet.as_view({'post': 'create'}), name='create_reservation'),
    path('reservations/all/', BookingRoomViewSet.as_view({'get': 'list'}), name='reservations-all'),
    path('reservations/edit/<int:pk>',
         BookingRoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='reservations-edit'),
    path('reservations/room/<int:room_id>',
         ReservationsByRoomViewSet.as_view({'get': 'retrieve'}), name='room_reservations'),
    path('reservations/room/employee/<int:employee>',
         RoomReservationsByEmployeeViewSet.as_view({'get': 'retrieve'}), name='employee_in_room_reservations'),
    path('reservations/cancel/<int:pk>',
         BookingRoomViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='reservations-cancel'),

]
