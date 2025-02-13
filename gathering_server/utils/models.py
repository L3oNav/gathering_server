"""Base Model."""
# ? Django imports
from django.db import models


class BaseModel(models.Model):
    """BaseModel."""

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
