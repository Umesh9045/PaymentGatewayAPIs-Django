from django.db import models

# Create your models here.
class Payment_Status(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"ID {self.id} - {self.name}"