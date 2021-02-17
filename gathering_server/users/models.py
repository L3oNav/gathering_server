
# rest_framework imports
from django.contrib.auth.models import AbstractUser
from django.db import models
# models imports
from src_gather.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """Default user for gathering."""

    #: First and last name do not cover name patterns around the globe

    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
            "unique": "username is already in use"
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_verified = models.BooleanField('verified', default=False, help_text=(
        "set to true when the user have verified it\'s email address"
    ))

    def __str__(self):
        return self.username

