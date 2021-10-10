from rest_framework import serializers
from rooms.models import MeetingRoom



class MeetRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingRoom
        fields =('id','title')
