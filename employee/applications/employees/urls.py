from django.urls import path
from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployee.as_view()),
    path('list-employee-by-area/', views.ListEmployeeByArea.as_view()),
]