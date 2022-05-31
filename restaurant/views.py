from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


# Create your views here.

class CourseListViews(ListView):
    model = Course
    queryset = Course.objects.order_by('course_type')
    template_name = 'index.html'


def restaurant_view(request):
    return render(request, "our-restaurant.html")


def booking_view(request):
    return render(request, "booking.html")


def menu_list(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, "menu.html", context)


def team_view(request):
    return render(request, "team.html")


def gallery_view(request):
    return render(request, "gallery.html")


def faq_view(request):
    return render(request, "faq.html")


def events_view(request):
    return render(request, "events.html")


def member_view(request):
    return render(request, "member.html")
