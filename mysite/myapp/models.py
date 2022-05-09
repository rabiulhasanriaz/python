from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class First(models.Model):
    firstname = CharField(max_length=50)
    lastname = CharField(max_length=50)
    in_no = IntegerField()
    class Meta:
        db_table = 'myapp_first'