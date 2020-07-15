from django.shortcuts import render

# Create your views here.

# Machine
from django.urls import reverse_lazy
from django.views import generic

from app.models import Machine


class MachineList(generic.ListView):
    model = Machine


class MachineView(generic.DetailView):
    model = Machine


class MachineCreate(generic.CreateView):
    model = Machine
    fields = ['name', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:machine_list')


class MachineUpdate(generic.UpdateView):
    model = Machine
    fields = ['name', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:machine_list')


class MachineDelete(generic.DeleteView):
    model = Machine
    success_url = reverse_lazy('app:machine_list')