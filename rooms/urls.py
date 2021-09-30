from django.urls import path
from rooms.views import MeetRoomViewSet

app_name = 'rooms'


urlpatterns  = [
    path('all/', MeetRoomViewSet.as_view({"get": "list"}) ),
    path('add/', MeetRoomViewSet.as_view({'post': 'create'}), name ='create_room' ),
]