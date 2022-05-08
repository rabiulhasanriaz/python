from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class First(models.Model):
    name = CharField(max_length=50)
    mobile = IntegerField()