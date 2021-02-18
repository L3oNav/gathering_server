# django
from django.db import models
from django.contrib.postgres import fields
# Utilities
from gathering_server.utils.models import BaseModel
from gathering_server.utils import fields as custom_fields


class GatheringModel(BaseModel):

    profession_options = [
        (1, 'Fisherman'),
        (2, 'Ore Miner'),
        (3, 'Lumberjack'),
        (4, 'Animal Skinner'),
        (5, 'Fiber Harvester'),
        (6, 'Quarrier'),
    ]

    user = models.CharField(
        max_length=56
    )

    time_gatheried = custom_fields.IntegerRangeField(
        min_value=0,
        max_value=512,
        blank=False,
        null=False
    )

    profession = custom_fields.IntegerRangeField(blank=False, null=False, min_value=1, max_value=6)

    resources = fields.ArrayField(
        fields.JSONField(),
        size=8,
        blank=False,
        null=False,
    )

    prices = fields.ArrayField(
        fields.JSONField(),
        size=8,
        blank=False,
        null=False,
    )
