from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('new_department/', views.NewDepartmentView.as_view(), name='new_department'),
]