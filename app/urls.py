from django.urls import path

from app import views
urlpatterns = [
    # Machine
    path('machines/', views.Machine.MachineList.as_view(), name='machine_list'),
    path('machine/<int:pk>/', views.MachineView.as_view(), name='machine_detail'),
    path('machine/edit/<int:pk>/', views.MachineUpdate.as_view(), name='machine_edit'),
    path('machine/create/', views.MachineCreate.as_view(), name='machine_create'),
    path('machine/delete/<int:pk>/', views.MachineDelete.as_view(), name='machine_delete')
]