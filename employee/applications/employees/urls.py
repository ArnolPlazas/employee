from django.urls import path
from . import views

app_name = 'employee_app'

urlpatterns = [
    path('', views.HomeEmployeesView.as_view(), name='start'),
    path('list-all-employee/', views.ListAllEmployee.as_view(), name='employees_all'),
    path('list-employee-admin/', views.ListAllEmployeeAdmin.as_view(), name='employees_admin'),
    path('list-employee-by-area/<area_name>', views.ListEmployeeByArea.as_view(), name='empleyee_department'),
    path('search-employee', views.ListEmployeeByKeyWord.as_view()),
    path('list-skills-employee', views.ListSkillsEmployee.as_view()),
    path('detail-employee/<pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('add-employee', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('success', views.SuccessView.as_view(), name='correct'),
    path('update/<pk>', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.EmployeeDeleteView.as_view(), name='delete'),
]