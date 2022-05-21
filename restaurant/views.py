from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


# Create your views here.

class CourseListViews(ListView):
    model = Course
    queryset = Course.objects.order_by('course_type')
    template_name = 'index.html'
