# django imports
from django.db import models
from django.contrib.postgres import fields
# Utilities
from gathering_server.utils.models import BaseModel


class SpecGatheringModel(BaseModel):

    user = models.CharField(max_length=56, unique=True)

    specs = fields.ArrayField(
        fields.JSONField(),
        size=7,
        blank=False,
        null=False,
    )


