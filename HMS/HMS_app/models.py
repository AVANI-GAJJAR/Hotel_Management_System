from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Table(models.Model):
    #id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.CharField(max_length=40)
    mobile_number=models.CharField(max_length=10)
    designation=models.CharField(max_length=10)
    salary=models.IntegerField()
    leaves=models.IntegerField()