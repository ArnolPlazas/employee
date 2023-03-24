from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView


from applications.employees.models import Employee
from .models import Department

from .forms import NewDepartmentForm


class DepartmentListView(ListView):
    model = Department
    template_name = "departments/list.html"
    context_object_name = 'departments'




class NewDepartmentView(FormView):
    template_name='departments/new_department.html'
    form_class = NewDepartmentForm
    success_url = '/'

    def form_valid(self, form):
        print('************ form valid **************')
        dpt = Department(
            name=  form.cleaned_data['department'],
            short_name= form.cleaned_data['short_name']

        )
        dpt.save()
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        Employee.objects.create(
            first_name= name,
            last_name= last_name,
            job='1',
            department=dpt
        )
        
        return super(NewDepartmentView, self).form_valid(form)