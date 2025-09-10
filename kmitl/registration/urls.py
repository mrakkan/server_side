from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("professor/", views.professor, name="professor"),
    path("course/", views.course, name="course"),
    path("faculty/", views.faculty, name="faculty"),
    path("createstudent/", views.createstudent, name="createstudent"),
    path("updatestudent/<int:student_id>/", views.updatestudent, name="updatestudent")
    
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]