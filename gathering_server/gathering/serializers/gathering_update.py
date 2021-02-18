from rest_framework import serializers
from gathering_server.gathering.models import GatheringModel
from gathering_server.utils.serializers import ResourceListField
import json


class GatheringUpdateSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)

    id = serializers.IntegerField(required=True)

    time_gatheried = serializers.IntegerField(min_value=0, max_value=256)

    profession = serializers.IntegerField(min_value=1, max_value=6, required=True)

    resources = serializers.ListField(
        required=True,
        child=ResourceListField()
    )

    prices = serializers.ListField(
        required=True,
        child=ResourceListField()
    )

    def validate(self, data):
        if data['profession'] not in range(0, 7):
            raise serializers.ValidationError('I need a valid input in profession field')
        return data

    def create(self, data):
        gathering_update = GatheringModel.objects.filter(user=data['user'], id=data['id']).update(**data)
        return gathering_update
