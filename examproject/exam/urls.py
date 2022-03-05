from django.urls import path
from .views import index, students_page

urlpatterns = [
    path('', index, name='index'),
    path('student', students_page, name='student'),
]