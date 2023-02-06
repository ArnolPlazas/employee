from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Test

class IndexView(TemplateView):
    template_name = 'home/home.html'


class TestListView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'test_list'
    
class ModelListView(ListView):
    model = Test
    template_name = 'home/model_list.html'
    context_object_name = 'model_list'
