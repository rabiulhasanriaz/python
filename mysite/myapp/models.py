from django.db import models
from django.forms import CharField, IntegerField
from django.db import models

# Create your models here.
class First(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    in_no = models.IntegerField()
    class Meta:
        db_table = 'myapp_first'