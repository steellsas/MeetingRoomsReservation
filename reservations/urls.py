from django.urls import path
from reservations.views import BookingRoomViewSet

app_name = 'reservations'


urlpatterns = [
    path('resevations/create/', BookingRoomViewSet.as_view({'post': 'create'})),
    path('resevations/all/', BookingRoomViewSet.as_view({'get': 'list'})),
    path('resevations/edit/<int:pk>', BookingRoomViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'}))
]