from django.urls import path

from app import views
app_name = 'app'
urlpatterns = [
    path('', views.homeApp),
    # Machine
    path('machines/', views.MachineList.as_view(), name='machine_list'),
    path('machine/<int:pk>/', views.MachineView.as_view(), name='machine_detail'),
    path('machine/edit/<int:pk>/', views.MachineUpdate.as_view(), name='machine_edit'),
    path('machine/create/', views.MachineCreate.as_view(), name='machine_create'),
    path('machine/delete/<int:pk>/', views.MachineDelete.as_view(), name='machine_delete'),
    # Company
    path('companys/', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>/', views.CompanyView.as_view(), name='company_detail'),
    path('company/edit/<int:pk>/', views.CompanyUpdate.as_view(), name='company_edit'),
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/delete/<int:pk>/', views.CompanyDelete.as_view(), name='company_delete'),
    # Operator
    path('operators/', views.OperatorList.as_view(), name='operator_list'),
    path('operator/<int:pk>/', views.OperatorView.as_view(), name='operator_detail'),
    path('operator/edit/<int:pk>/', views.OperatorUpdate.as_view(), name='operator_edit'),
    path('operator/create/', views.OperatorCreate.as_view(), name='operator_create'),
    path('operator/delete/<int:pk>/', views.OperatorDelete.as_view(), name='operator_delete'),
    # Component
    path('components/', views.ComponentList.as_view(), name='component_list'),
    path('component/<int:pk>/', views.ComponentView.as_view(), name='component_detail'),
    path('component/edit/<int:pk>/', views.ComponentUpdate.as_view(), name='component_edit'),
    path('component/create/', views.ComponentCreate.as_view(), name='component_create'),
    path('component/delete/<int:pk>/', views.ComponentDelete.as_view(), name='component_delete'),
    # ComponentGroup
    path('componentgroups/', views.ComponentGroupList.as_view(), name='componentgroup_list'),
    path('componentgroup/<int:pk>/', views.ComponentGroupView.as_view(), name='componentgroup_detail'),
    path('componentgroup/edit/<int:pk>/', views.ComponentGroupUpdate.as_view(), name='componentgroup_edit'),
    path('componentgroup/create/', views.ComponentGroupCreate.as_view(), name='componentgroup_create'),
    path('componentgroup/delete/<int:pk>/', views.ComponentGroupDelete.as_view(), name='componentgroup_delete'),
    # Maintenance
    path('maintenances/', views.MaintenanceList.as_view(), name='maintenance_list'),
    path('maintenance/<int:pk>/', views.MaintenanceView.as_view(), name='maintenance_detail'),
    path('maintenance/edit/<int:pk>/', views.MaintenanceUpdate.as_view(), name='maintenance_edit'),
    path('maintenance/create/', views.MaintenanceCreate.as_view(), name='maintenance_create'),
    path('maintenance/delete/<int:pk>/', views.MaintenanceDelete.as_view(), name='maintenance_delete'),
    # PlanedMaintenance
    path('planedmaintenances/', views.PlanedMaintenanceList.as_view(), name='planedmaintenance_list'),
    path('planedmaintenance/<int:pk>/', views.PlanedMaintenanceView.as_view(), name='planedmaintenance_detail'),
    path('planedmaintenance/edit/<int:pk>/', views.PlanedMaintenanceUpdate.as_view(), name='planedmaintenance_edit'),
    path('planedmaintenance/create/', views.PlanedMaintenanceCreate.as_view(), name='planedmaintenance_create'),
    path('planedmaintenance/delete/<int:pk>/', views.PlanedMaintenanceDelete.as_view(), name='planedmaintenance_delete')
]