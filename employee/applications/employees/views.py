from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Employee


class ListAllEmployee(ListView):
    """list all employee"""
    template_name = 'employee/list_all.html'
    model = Employee
    context_object_name = 'lista' # por defecto es object_list

class ListEmployeeByArea(ListView):
    """list all employee by area"""
    template_name = 'employee/list_employee_by_area.html'
    queryset = Employee.objects.filter(department__name='TECNOLOGIA')