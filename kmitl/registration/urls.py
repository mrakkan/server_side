
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view, name='student'),
    path('professors/', views.professor_view, name='professor'),
    path('courses/', views.course_view, name='course'),
    path('faculties/', views.faculty_view, name='faculty'),
    path('create_student/', views.create_student, name='create'),
]
