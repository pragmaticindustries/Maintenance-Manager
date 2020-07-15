from django.db import models

# Create your models here.

class Machine(models.Model):
    machid= models.UUIDField()
    name = models.CharField(max_length=64)
    description= models.CharField(max_length=1024)
    installation_date = models.DateField('date installed')


class Component(models.Model):
    comid = models.UUIDField()
    name = models.CharField(max_length=32)
    description=models.CharField(max_length=256)
    wearpart= models.BooleanField()
    sparepart=models.BooleanField()
    cyclecounter = models.IntegerField()


class ComponentGroup(models.Model):
    comgrid = models.UUIDField()
    name = models.CharField(max_length=32)
    description=models.CharField(max_length=256)

class Maintenance(models.Model):
    mainid= models.UUIDField()
    maindate=models.DateTimeField()
