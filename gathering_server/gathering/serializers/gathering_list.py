# django REST framework
from rest_framework import serializers
# Serializers
from gathering_server.gathering.serializers import GatheringFormatterSerializer
# Models
from gathering_server.gathering.models import GatheringModel

import json


class GatheringListSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)

    def create(self, data):
        gathering_list = GatheringModel.objects.filter(user=data['user']).values()
        return GatheringFormatterSerializer(gathering_list, many=True).data


class GatheringListByIdSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)
    id = serializers.CharField(required=True)

    def create(self, data):
        gathering_list = GatheringModel.objects.filter(user=data['user'], id=data['id']).values()
        if len(gathering_list) <= 0:
            return False
        return gathering_list[0]
