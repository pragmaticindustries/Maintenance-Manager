from django.db import models

# Create your models here.
class Company(models.Model):
    compid=models.UUIDField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Machine(models.Model):
    machid= models.UUIDField()
    name = models.CharField(max_length=64)
    description= models.CharField(max_length=1024)
    installation_date = models.DateField('date installed')
    manufacturer = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="manufacturer")
    operator = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="operator")


class Component(models.Model):
    comid = models.UUIDField()
    name = models.CharField(max_length=32)
    description=models.CharField(max_length=256)
    wearpart= models.BooleanField()
    sparepart=models.BooleanField()
    cyclecounter = models.IntegerField()
    maintenanceintervall=models.IntegerField()



class ComponentGroup(models.Model):
    comgrid = models.UUIDField()
    name = models.CharField(max_length=32)
    description=models.CharField(max_length=256)

class Maintenance(models.Model):
    mainid= models.UUIDField()
    maindate=models.DateTimeField()
    maindescpription=models.CharField(max_length=256)