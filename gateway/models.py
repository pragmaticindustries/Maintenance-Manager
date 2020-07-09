from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=100)
    installation_date = models.DateField('date installed')
    manufacturer = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="manufacturer")
    operator = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="operator")

    def __str__(self):
        return self.name

