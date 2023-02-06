from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'home/home.html'


class TestListView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'test_list'
    
