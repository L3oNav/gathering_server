
# django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# Models
from gathering_server.gathering.models import SpecGatheringModel


class SpecGathering(serializers.ModelSerializer):

    class Meta:
        model = SpecGatheringModel
        fields = '__all__'


class TierSpecField(serializers.Serializer):

    tier = serializers.IntegerField(required=True, min_value=4, max_value=8)

    value = serializers.IntegerField(min_value=0, max_value=100, required=True)


class ProfessionSpecField(serializers.Serializer):

    profession = serializers.CharField(max_length=56)

    specs = serializers.ListField(
        required=True,
        child=TierSpecField()
    )


class SpecCreateSerializer(serializers.Serializer):

    user = serializers.CharField(
        max_length=56,
        required=True,
        validators=[UniqueValidator(queryset=SpecGatheringModel.objects.all())]
    )

    specs = serializers.ListField(
        required=True,
        child=ProfessionSpecField()
    )

    def create(self, data):
        spec_model = SpecGatheringModel.objects.create(**data)
        return SpecGathering(spec_model).data


class SpecReadSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)

    def create(self, data):
        spec_model = SpecGatheringModel.objects.filter(user=data['user']).values()
        if len(spec_model) <= 0:
            return False
        return spec_model[0]


class SpecUpdateSerializer(serializers.Serializer):

    user = serializers.CharField(required=True)

    specs = serializers.ListField(
        required=True,
        child=ProfessionSpecField()
    )

    def create(self, data):
        spec_model = SpecGatheringModel.objects.filter(user=data['user']).update(**data)
        return spec_model
