from django.db import models

# Create your models here.


class ClientInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=10,unique=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name
