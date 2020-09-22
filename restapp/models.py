from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_dec = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
