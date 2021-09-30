from rest_framework import viewsets
from rooms.models import MeetingRoom
from rooms.serializers import MeetRoomSerializer


class MeetRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetRoomSerializer
    permission_classes = []
