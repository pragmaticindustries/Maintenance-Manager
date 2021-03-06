from django.urls import path

from . import views

app_name = 'gateway'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
    # Machine
    path('machines/', views.MachineList.as_view(), name='machine_list'),
    path('machine/<int:pk>/', views.MachineView.as_view(), name='machine_detail'),
    path('machine/edit/<int:pk>/', views.MachineUpdate.as_view(), name='machine_edit'),
    path('machine/create/', views.MachineCreate.as_view(), name='machine_create'),
    path('machine/delete/<int:pk>/', views.MachineDelete.as_view(), name='machine_delete'),
]
