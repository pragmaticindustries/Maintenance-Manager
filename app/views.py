from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Machine
from django.urls import reverse_lazy
from django.views import generic

from app.models import Machine,Company

def index(request):
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