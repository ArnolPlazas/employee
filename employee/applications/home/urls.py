from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('list/', views.TestListView.as_view()),
    path('model_list/', views.ModelListView.as_view()),
    path('add/', views.TestCreateView.as_view(), name='test_add'),
    path('review_foundation/', views.ReviewFoundationView.as_view(), name='review_foundation'),
]