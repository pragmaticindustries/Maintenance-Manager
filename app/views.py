from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Machine
from django.urls import reverse_lazy
from django.views import generic

from app.models import Machine,Company,Operator,Component,ComponentGroup,Maintenance,PlanedMaintencance

def index(request):
    context = {
        'companies': Company.objects.all(),
        'machines': Machine.objects.all()
    }
    return render(request, 'app/index.html', context)

def home(request):
    context = {
        'companies': Company.objects.all(),
        'machines': Machine.objects.all()
    }
    return render(request, 'app/index.html', context)


def company_detail(request, company_id):
    return HttpResponse("You're looking at company %s." % company_id)


class CompanyDetail(generic.DetailView):
    model = Company
    template_name = 'app/company_detail.html'

class MachineList(generic.ListView):
    model = Machine


class MachineView(generic.DetailView):
    model = Machine


class MachineCreate(generic.CreateView):
    model = Machine
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:machine_list')


class MachineUpdate(generic.UpdateView):
    model = Machine
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
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
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class CompanyUpdate(generic.UpdateView):
    model = Company
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
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
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class OperatorUpdate(generic.UpdateView):
    model = Operator
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class OperatorDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('app:company_list')


class ComponentList(generic.ListView):
    model = Component


class ComponentView(generic.DetailView):
    model = Component


class ComponentCreate(generic.CreateView):
    model = Component
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class ComponentUpdate(generic.UpdateView):
    model = Component
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class ComponentDelete(generic.DeleteView):
    model = Component
    success_url = reverse_lazy('app:company_list')


class ComponentGroupList(generic.ListView):
    model = ComponentGroup


class ComponentGroupView(generic.DetailView):
    model = ComponentGroup


class ComponentGroupCreate(generic.CreateView):
    model = ComponentGroup
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class ComponentGroupUpdate(generic.UpdateView):
    model = ComponentGroup
    fields = ['name','description', 'installation_date', 'manufacturer', 'operator']
    success_url = reverse_lazy('app:company_list')


class ComponentGroupDelete(generic.DeleteView):
    model = ComponentGroup
    success_url = reverse_lazy('app:company_list')