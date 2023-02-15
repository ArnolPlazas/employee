from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Employee

# list all employee
class ListAllEmployee(ListView):
    template_name = 'employee/list_all.html'
    model = Employee
    context_object_name = 'lista'

