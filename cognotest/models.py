from django.db import models

# Create your models here.
class Cogno(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        """A string representation of the model."""
        return self.name