from django.db import models


class TimeStamped(models.Model):
    """
    An abstract base model that adds created_at and updated_at fields to other models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # we indicate that this model will be an abstract base class
        abstract = True
