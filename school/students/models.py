from django.db import models

# Create your models here.
class register1(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    std=models.IntegerField()
    division=models.CharField(max_length=30)
