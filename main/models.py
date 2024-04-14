from django.db import models


class Employee(models.Model):
    user_id = models.IntegerField()
    photo = models.ImageField(upload_to='employees_photos', null=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class Case(models.Model):
    case_id = models.IntegerField()
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255*4)

# Create your models here.
