from django.db import models
from django.contrib.postgres import fields

from gathering_server.utils.models import BaseModel

from gathering_server.utils.fields import IntegerRangeField


class RefiningModel(BaseModel):

    user = models.EmailField(max_length=255)

    tax = models.IntegerField()
    type_of = models.CharField(max_length=56)

    focus = IntegerRangeField(
        min_value=0, max_value=30000,
        blank=True,
        null=True
    )

    purchased_resources = models.BooleanField(default=False)

    resouces_cost = fields.ArrayField(
        fields.JSONField(),
        blank=False,
        null=False
    )

    resources_to_refining = fields.ArrayField(
        fields.JSONField(),
        blank=False,
        null=False
    )

    refined_total = fields.ArrayField(
        fields.JSONField(),
        blank=False,
        null=False
    )

    refining_prices = fields.ArrayField(
        fields.JSONField(),
        blank=False,
        null=False
    )

