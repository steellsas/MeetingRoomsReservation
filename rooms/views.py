from rest_framework import viewsets
from rooms.models import MeetingRoom
from rooms.serializers import MeetRoomSerializer
from rest_framework.permissions import IsAuthenticated


class MeetRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetRoomSerializer
    permission_classes = [IsAuthenticated]
