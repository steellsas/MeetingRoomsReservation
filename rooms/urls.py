from django.urls import path
from rooms.views import MeetRoomViewSet

app_name = 'rooms'


urlpatterns  = [
    path('room/all/', MeetRoomViewSet.as_view({"get": "list"}), name='room-list'),
    path('room/add/', MeetRoomViewSet.as_view({'post': 'create'}), name='create-room'),
    path('room/edit/', MeetRoomViewSet.as_view({'get':'retrieve', 'put':'update'}), name='edit-room')
]