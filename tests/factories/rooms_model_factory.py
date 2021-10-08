import factory
from rooms.models import MeetingRoom


class MeetingRoomFactory(factory.Factory):
    class Meta:
        model = MeetingRoom
    id = 10
    title = factory.Faker('sentence', nb_words=2)
