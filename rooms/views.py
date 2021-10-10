from rest_framework import viewsets
from rooms.models import MeetingRoom
from rooms.serializers import MeetRoomSerializer
from rest_framework.permissions import IsAuthenticated
import logging,traceback


class MeetRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    logging.info('Actions with meeting rooms')
    serializer_class = MeetRoomSerializer
    permission_classes = [IsAuthenticated]

