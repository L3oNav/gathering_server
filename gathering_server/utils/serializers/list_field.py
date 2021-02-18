from rest_framework import serializers


class ValueEnchantField(serializers.Serializer):

    enchant = serializers.IntegerField(min_value=0, max_value=3, required=True)

    value = serializers.IntegerField(min_value=0, max_value=1000000, required=True)

    def validate(self, data):
        return data


class ResourceListField(serializers.Serializer):

    tier = serializers.IntegerField(min_value=1, max_value=8, required=True)

    value = serializers.ListField(
        child=ValueEnchantField(),
        required=True
    )

    def validate(self, data):
        return data
