from django.shortcuts import render

from .models import StClass, Group, Gender, Section, ForeignLanguage, Exam, Student


def index(request):
    return render(request, 'exam/index.html')


def students_page(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'exam/students.html', context=context)