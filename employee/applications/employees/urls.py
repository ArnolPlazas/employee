from django.urls import path
from . import views

urlpatterns = [
    path('list-all-employee/', views.ListAllEmployee.as_view()),
    path('list-employee-by-area/<area_name>', views.ListEmployeeByArea.as_view()),
    path('search-employee', views.ListEmployeeByKeyWord.as_view()),
    path('list-skills-employee', views.ListSkillsEmployee.as_view()),
    path('detail-employee/<pk>', views.EmployeeDetailView.as_view()),
    path('add-employee', views.EmployeeCreateView.as_view()),
]