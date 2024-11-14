from uuid import uuid4

from django.db import models

# Create your models here.
class Product(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.uuid} - {self.name}'