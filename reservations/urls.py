from django.urls import path
from reservations.views import BookingRoomViewSet, ReservationsByRoomViewSet, RoomReservationsByEmployeeViewSet

app_name = 'reservations'

urlpatterns = [
    path('reservations/create/', BookingRoomViewSet.as_view({'post': 'create'}), name='create_reservation'),
    path('reservations/all/', BookingRoomViewSet.as_view({'get': 'list'})),
    path('reservations/edit/<int:pk>',
         BookingRoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('reservations/room/<int:pk>',
         ReservationsByRoomViewSet.as_view({'get': 'retrieve'}), name='room_reservations'),
    path('reservations/room/employee/<int:pk>',
         RoomReservationsByEmployeeViewSet.as_view({'get': 'retrieve'}), name='employee_in_room_reservations'),
    path('reservations/cancel/<int:pk>', BookingRoomViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),

]
