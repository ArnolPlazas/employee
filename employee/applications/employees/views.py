from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Employee


class ListAllEmployee(ListView):
    """list all employee"""
    template_name = 'employee/list_all.html'
    paginate_by = 2
    ordering='first_name'
    model = Employee
    context_object_name = 'lista' # por defecto es object_list

class ListEmployeeByArea(ListView):
    """list all employee by area"""
    template_name = 'employee/list_employee_by_area.html'
    # queryset = Employee.objects.filter(department__name='TECNOLOGIA')
    
    def get_queryset(self):
        area = self.kwargs['area_name']
        employee_list = Employee.objects.filter(department__name=area)
        return employee_list


class ListEmployeeByKeyWord(ListView):
    """List of employee by key word"""
    template_name = 'employee/list_employee_by_kword.html'
    context_object_name = 'employee'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        employee_list = Employee.objects.filter(first_name=key_word)
        return employee_list
    