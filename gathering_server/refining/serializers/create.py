from rest_framework import serializers

from gathering_server.refining.models import RefiningModel

from gathering_server.utils.serializers import ResourceListField, PricesList

from gathering_server.refining.functions import RefiningRocks, RefiningGeneral

class RefiningFormatterSerializer(serializers.ModelField):

    class Meta:
        models = RefiningModel
        fields = '__all__'


class RefiningCalculatorSerializer(serializers.Serializer):

    user = serializers.EmailField(required=True)

    tax = serializers.IntegerField(required=True, max_value=999, min_value=0)

    type_of = serializers.CharField(max_length=56, required=True)

    focus = serializers.IntegerField(min_value=0, max_value=30000, required=True)

    purchased_resources = serializers.BooleanField(default=False)

    return_rate = serializers.FloatField(min_value=0, max_value=100)

    resources_cost = serializers.ListField(
        child=ResourceListField()
    )

    resources_to_refining = serializers.ListField(
        child=ResourceListField()
    )

    refining_prices = serializers.ListField(
        child=PricesList()
    )

    def create(self, data):
        if data['type_of'] == 'rocks':
            refiner = RefiningRocks(data['resources_to_refining'], return_rate=data['return_rate'])
        else:
            refiner = RefiningGeneral(data['resources_to_refining'], return_rate=data['return_rate'])
        return refiner.calculator()
