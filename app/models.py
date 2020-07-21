from django.db import models


# Create your models here.
class Company(models.Model):
    compid = models.UUIDField()
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    ort = models.CharField(max_length=200)
    plz = models.CharField(max_length=200)


class Operator(models.Model):
    opid = models.UUIDField()
    name = models.CharField(max_length=256)
    company=models.ForeignKey(Company,on_delete=models.PROTECT, related_name="operator_company")


class Component(models.Model):
    comid = models.UUIDField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    wearpart = models.BooleanField()
    sparepart = models.BooleanField()
    cyclecounter = models.IntegerField(default=0)
    maintenanceintervall = models.IntegerField()


class ComponentGroup(models.Model):
    comgrid = models.UUIDField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    cyclecounter = models.IntegerField(default=0)
    component=models.ManyToManyField(Component)


class Machine(models.Model):
    machid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    installation_date = models.DateField('date installed')
    manufacturer = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="manufacturer")
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT, related_name="operator")
    componentgroup = models.ManyToManyField(ComponentGroup)


class Maintenance(models.Model):
    mainid = models.UUIDField()
    maindate = models.DateTimeField()
    maindescpription = models.CharField(max_length=256)
    component = models.ForeignKey(Component,on_delete=models.PROTECT,related_name="maintenance_component")


class PlanedMaintencance(models.Model):
    plmainid = models.UUIDField()
    plmaindate = models.DateTimeField()
    plmaindescription = models.CharField(max_length=256)
    component= models.ForeignKey(Component,on_delete=models.PROTECT,related_name="planedmaintenance_component")
