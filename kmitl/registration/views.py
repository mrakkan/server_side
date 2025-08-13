from django.shortcuts import render, redirect
from .models import Student, Professor, Course, Faculty, Section, StudentProfile
from django.db.models.functions import Concat
from django.db.models import Value

def student_view(request):
            keyword = request.GET.get("keyword", "")
            field = request.GET.get("field", "full_name")
            students = Student.objects.all()
            if keyword:
                if field == "email":
                    students = students.filter(studentprofile__email__icontains=keyword)
                elif field == "faculty":
                    students = students.filter(faculty__name__icontains=keyword)
                else:
                    student_full = students.annotate(fullname= Concat("first_name", Value(" "), "last_name"))
                    students = student_full.filter(fullname__icontains=keyword)
            return render(request, "index.html", {"students_list": students, "keyword": keyword, "filter": field})

def professor_view(request):
    keyword = request.GET.get("keyword", "")
    field = request.GET.get("field", "full_name")
    professors = Professor.objects.all()
    if keyword:
        keyword = keyword.lower()
        if field == "faculty":
            professors = professors.filter(faculty__name__icontains=keyword)
        else:
            professors = professors.filter(first_name__icontains=keyword) | professors.filter(last_name__icontains=keyword)
    return render(request, "professor.html", {"professors": professors, "keyword": keyword, "filter": field})

def course_view(request):
    keyword = request.GET.get("keyword", "")
    courses = Course.objects.all()
    if keyword:
        courses = courses.filter(course_name__icontains=keyword.lower())
    return render(request, "course.html", {"courses": courses, "keyword": keyword})

def faculty_view(request):
    keyword = request.GET.get("keyword", "")
    faculties = Faculty.objects.all()
    facultiess = Faculty.objects.all().count()
    if keyword:
        faculties = faculties.filter(name__icontains=keyword.lower())
    return render(request, "faculty.html", {"faculties": faculties, "total": facultiess, "keyword": keyword})

def create_student(request):
     faculties = Faculty.objects.all()
     sections = Section.objects.all()

     if request.method == 'GET':
          return render(
          request,'create_student.html', context = { "faculties": faculties, "sections": sections}
          )
     elif request.method == 'POST':
          student_id = request.POST.get('student_id')
          faculty_id = request.POST.get('faculty_id')
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          email = request.POST.get('email')
          phone_number = request.POST.get('phone_number')
          address = request.POST.get('address')
          section_ids = request.POST.getlist('section_ids')

          fac = Faculty.objects.get(pk=int(faculty_id))

          sec = Student.objects.create(
               student_id = student_id,
               first_name = first_name,
               last_name = last_name,
               faculty = fac
          )
          sec.enrolled_sections.set(section_ids)

          StudentProfile.objects.create(
               student = sec,
               email = email,
               phone_number = phone_number,
               address = address
          )
          return redirect('student')

