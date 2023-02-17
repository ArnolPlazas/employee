from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView)

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

class ListSkillsEmployee(ListView):
    """show employee's skills"""
    template_name = 'employee/skills_employee.html'
    context_object_name = 'skills'
    def get_queryset(self):
        employee = Employee.objects.get(id=1)
        skill = employee.skills.all()
        return skill

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee-detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee of month'
        return context


class SuccessView(TemplateView):
    template_name = 'employee/success.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/add_employee.html"
    fields = ['first_name', 'last_name', 'job', 'department', 'skills']
    # fields = ('__all__')
    success_url= reverse_lazy('employee_app:correct')
    
    def form_valid(self, form):
        employee = form.save(commit=False) # crear una instancia y no guardarlo todavia
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)