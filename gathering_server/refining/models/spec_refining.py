from django.db import models
from django.contrib.postgres import fields

from gathering_server.utils.models import BaseModel
from gathering_server.utils.fields import IntegerRangeField


class SpecRefiningModel(BaseModel):

    user = models.EmailField(max_length=255)

    specs = fields.ArrayField(
        fields.JSONField(),
        blank=False,
        null=False
    )

