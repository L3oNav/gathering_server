# django REST Framework
from rest_framework import serializers

#Models
from gathering_server.gathering.models import GatheringModel


class GatheringDeleteSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)
    id = serializers.IntegerField(required=True)

    def create(self, data):
        gathering_delete = GatheringModel.objects.filter(user=data['user'], id=data['id']).delete()
        if gathering_delete[0] != data['id']:
            return False
        return True
