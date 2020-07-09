from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from gateway.models import Company, Machine


def index(request):
    context = {
        'companies': Company.objects.all(),
        'machines': Machine.objects.all()
    }
    return render(request, 'gateway/index.html', context)


def company_detail(request, company_id):
    return HttpResponse("You're looking at company %s." % company_id)


class CompanyDetail(generic.DetailView):
    model = Company
    template_name = 'gateway/company_detail.html'


# Machine


class MachineList(generic.ListView):
    model = Machine


class MachineView(generic.DetailView):
    model = Machine


class MachineCreate(generic.CreateView):
    model = Machine
    fields = ['name', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('gateway:machine_list')


class MachineUpdate(generic.UpdateView):
    model = Machine
    fields = ['name', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('gateway:machine_list')


class MachineDelete(generic.DeleteView):
    model = Machine
    success_url = reverse_lazy('gateway:machine_list')
