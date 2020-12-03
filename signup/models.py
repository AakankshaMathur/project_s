from django.db import models

# Create your models here.

from django.db import models

class Member(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    def __str__(self):
        return self.email 