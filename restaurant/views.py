from django.shortcuts import render
from django.views.generic import ListView
from .models import Course
from .forms import EventBooking
from django.contrib import messages


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
    starter_list = Course.objects.all().filter(course_type='Starter')
    main_list = Course.objects.all().filter(course_type='Main')
    fish_list = Course.objects.all().filter(course_type='Fish')
    dessert_list = Course.objects.all().filter(course_type='Dessert')
    salads_list = Course.objects.all().filter(course_type='Salads')
    soup_list = Course.objects.all().filter(course_type='Soup')
    context = {
        'starter_list': starter_list,
        'main_list': main_list,
        'fish_list': fish_list,
        'dessert_list': dessert_list,
        'salads_list': salads_list,
        'soup_list': soup_list,
        }
    return render(request, "menu.html", context)


def team_view(request):
    return render(request, "team.html")


def gallery_view(request):
    return render(request, "gallery.html")


def faq_view(request):
    return render(request, "faq.html")


def events_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventBooking(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form = EventBooking()
            messages.success(request, 'The request has been received, we will contact you shortly')
    else:
        form = EventBooking()
    context = {'form': form}
    return render(request, "events.html", context)


def member_view(request):
    return render(request, "member.html")
