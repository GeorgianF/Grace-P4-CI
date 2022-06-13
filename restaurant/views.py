from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages
# from django.conf import settings
# from django.core.mail import send_mail
from .models import Course, Booking
from .forms import EventBooking, ReservationForm



# Create your views here.

NUMBER_OF_RESERVATIONS_PER_CLIENT = 1


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
    """
    SEND EVENTS FORM
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventBooking(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # receiver = request.POST.get('user_email')
            # send_mail(
            #     'Hello',
            #     'Here is the message.',
            #     settings.EMAIL_HOST_USER,
            #     [receiver],
            #     fail_silently=False,
            #     )
            messages.success(
                request,
                'Your request has been sent succesfully.' +
                ' We will contact you shortly'
                )
            form.save()
            form = EventBooking()
    else:
        form = EventBooking()
    context = {'form': form}
    return render(request, "events.html", context)


def view_booking(request):
    """
    View booking
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                'Your request has been sent succesfully registered'
                )
            form.save()
            form = ReservationForm()
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, "booking.html", context)


# @login_required()
# def create_booking(request):
#     """
#     Create booking
#     """
#     user = get_object_or_404(User, username=request.user)
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation_date = form.cleaned_data['date']
#             reservation_time = form.cleaned_data['arrival_time']
#             reservation_name = form.cleaned_data['booking_name']
#             req_reservation_date = reservation_date.strftime("%A, %d %B %Y")
#             req_reservation_time = reservation_time.strftime("%-I%p")
#             num_reservations = Booking.objects.filter(
#                 date=req_reservation_date,
#                 start_time=req_reservation_time).count()
#             if num_reservations >= NUMBER_OF_RESERVATIONS_PER_CLIENT:
#                 messages.error(
#                     request, 'No appointment is available on '
#                     f'{req_reservation_date} at {req_reservation_time}.')
#                 return redirect('booking.html')
#             else:
#                 form.instance.user = user
#                 form.save()
#                 messages.success(
#                     request,
#                     f'Your appointment for {reservation_name} '
#                     'has been added to our restaurant.')
#                 return redirect('booking.html')
#     form = Booking()
#     context = {
#         'form': form
#     }
#     return render(request, 'booking.html', context)
