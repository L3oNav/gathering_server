# django REST framework
from rest_framework import serializers
# Serializers
from gathering_server.utils.serializers import ResourceListField

# Models
from gathering_server.gathering.models import GatheringModel


class GatheringFormatterSerializer(serializers.ModelSerializer):

    class Meta:
        model = GatheringModel
        fields = '__all__'


class GatheringModelSerializer(serializers.Serializer):

    user = serializers.CharField()
    time_gatheried = serializers.IntegerField()
    profession = serializers.IntegerField()
    resources = serializers.ListField(
        child=serializers.JSONField()
    )
    prices = serializers.ListField(
        child=serializers.JSONField()
    )


class GatheringCreateSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)

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
        gathering_model = GatheringModel.objects.create(**data)
        return GatheringFormatterSerializer(gathering_model).data

