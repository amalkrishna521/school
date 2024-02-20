from django.db import models

# Create your models here.
class register2(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    subject=models.CharField(max_length=30)
