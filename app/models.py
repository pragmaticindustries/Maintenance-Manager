import uuid

from django.db import models


# Create your models here.
class Company(models.Model):
    # compid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    ort = models.CharField(max_length=200)
    plz = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Operator(models.Model):
    # opid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="operator_company")

    def __str__(self):
        return self.name


class Component(models.Model):
    # comid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    wearpart = models.BooleanField()
    sparepart = models.BooleanField()
    cyclecounter = models.IntegerField(default=0)
    maintenanceintervall = models.IntegerField()

    def __str__(self):
        return self.name


class ComponentGroup(models.Model):
    # comgrid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    cyclecounter = models.IntegerField(default=0)
    component = models.ManyToManyField(Component)

    def __str__(self):
        return self.name


class Machine(models.Model):
    # machid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    installation_date = models.DateField('date installed')
    manufacturer = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="manufacturer")
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT, related_name="operator")
    componentgroup = models.ManyToManyField(ComponentGroup)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    # mainid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    maindate = models.DateTimeField()
    maindescpription = models.CharField(max_length=256)
    component = models.ForeignKey(Component, on_delete=models.PROTECT, related_name="maintenance_component")

    def __str__(self):
        return self.name


class PlanedMaintenance(models.Model):
    # plmainid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plmaindate = models.DateTimeField()
    plmaindescription = models.CharField(max_length=256)
    component = models.ForeignKey(Component, on_delete=models.PROTECT, related_name="planedmaintenance_component")


def __str__(self):
    return self.name
