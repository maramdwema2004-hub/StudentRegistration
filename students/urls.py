from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('students/', views.student_list, name='student_list'),
]