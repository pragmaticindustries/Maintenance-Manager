from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Machine
from django.urls import reverse_lazy
from django.views import generic

from app.models import Machine, Company, Operator, Component, ComponentGroup, Maintenance, PlanedMaintenance


def home(request):
    return render(request, 'app/home.html')


def homeApp(request):
    return render(request, 'app/home_app.html')


class MachineList(generic.ListView):
    model = Machine


class MachineView(generic.DetailView):
    model = Machine


class MachineCreate(generic.CreateView):
    model = Machine
    fields = ['name', 'description', 'installation_date', 'manufacturer', 'operator', 'componentgroup']
    success_url = reverse_lazy('app:machine_list')


class MachineUpdate(generic.UpdateView):
    model = Machine
    fields = ['name', 'description', 'installation_date', 'manufacturer', 'operator', 'componentgroup']
    success_url = reverse_lazy('app:machine_list')


class MachineDelete(generic.DeleteView):
    model = Machine
    success_url = reverse_lazy('app:machine_list')


class CompanyList(generic.ListView):
    model = Company


class CompanyView(generic.DetailView):
    model = Company


class CompanyCreate(generic.CreateView):
    model = Company
    fields = ['name', 'street', 'ort', 'plz']
    success_url = reverse_lazy('app:company_list')


class CompanyUpdate(generic.UpdateView):
    model = Company
    fields = ['name', 'street', 'ort', 'plz']
    success_url = reverse_lazy('app:company_list')


class CompanyDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('app:company_list')


class OperatorList(generic.ListView):
    model = Operator


class OperatorView(generic.DetailView):
    model = Operator


class OperatorCreate(generic.CreateView):
    model = Operator
    fields = ['name', 'company']
    success_url = reverse_lazy('app:operator_list')


class OperatorUpdate(generic.UpdateView):
    model = Operator
    fields = ['name', 'company']
    success_url = reverse_lazy('app:operator_list')


class OperatorDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('app:operator_list')


class ComponentList(generic.ListView):
    model = Component


class ComponentView(generic.DetailView):
    model = Component


class ComponentCreate(generic.CreateView):
    model = Component
    fields = ['name', 'description', 'wearpart', 'sparepart', 'cyclecounter', 'maintenanceintervall']
    success_url = reverse_lazy('app:component_list')


class ComponentUpdate(generic.UpdateView):
    model = Component
    fields = ['name', 'description', 'wearpart', 'sparepart', 'cyclecounter', 'maintenanceintervall']
    success_url = reverse_lazy('app:component_list')


class ComponentDelete(generic.DeleteView):
    model = Component
    success_url = reverse_lazy('app:component_list')


class ComponentGroupList(generic.ListView):
    model = ComponentGroup


class ComponentGroupView(generic.DetailView):
    model = ComponentGroup


class ComponentGroupCreate(generic.CreateView):
    model = ComponentGroup
    fields = ['name', 'description', 'cyclecounter', 'component']
    success_url = reverse_lazy('app:componentgroup_list')


class ComponentGroupUpdate(generic.UpdateView):
    model = ComponentGroup
    fields = ['name', 'description', 'cyclecounter', 'component']
    success_url = reverse_lazy('app:componentgroup_list')


class ComponentGroupDelete(generic.DeleteView):
    model = ComponentGroup
    success_url = reverse_lazy('app:componentgroup_list')


class MaintenanceList(generic.ListView):
    model = Maintenance


class MaintenanceView(generic.DetailView):
    model = Maintenance


class MaintenanceCreate(generic.CreateView):
    model = Maintenance
    fields = ['maindate', 'maindescription', 'component']
    success_url = reverse_lazy('app:maintenance_list')


class MaintenanceUpdate(generic.UpdateView):
    model = Maintenance
    fields = ['maindate', 'maindescription', 'component']
    success_url = reverse_lazy('app:maintenance_list')


class MaintenanceDelete(generic.DeleteView):
    model = Maintenance
    success_url = reverse_lazy('app:maintenance_list')


class PlanedMaintenanceList(generic.ListView):
    model = PlanedMaintenance


class PlanedMaintenanceView(generic.DetailView):
    model = PlanedMaintenance


class PlanedMaintenanceCreate(generic.CreateView):
    model = PlanedMaintenance
    fields = ['plmaindate', 'plmaindescription', 'component']
    success_url = reverse_lazy('app:planedmaintenance_list')


class PlanedMaintenanceUpdate(generic.UpdateView):
    model = PlanedMaintenance
    fields = ['plmaindate', 'plmaindescription', 'component']
    success_url = reverse_lazy('app:planedmaintenance_list')


class PlanedMaintenanceDelete(generic.DeleteView):
    model = PlanedMaintenance
    success_url = reverse_lazy('app:planedmaintenance_list')
