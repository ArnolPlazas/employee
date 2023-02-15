from django.urls import path
from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployee.as_view()),
]