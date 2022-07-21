from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Course, Booking
from .forms import EventBooking, ReservationForm


# Create your views here.

class CourseListViews(ListView):
    model = Course
    queryset = Course.objects.order_by('course_type')
    template_name = 'index.html'


def restaurant_view(request):
    return render(request, "our-restaurant.html")


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
        form_events = EventBooking(request.POST)
        # check whether it's valid:
        if form_events.is_valid():
            recipient = form_events.cleaned_data.get('user_email')
            date = form_events.cleaned_data.get('event_date')
            subject = 'Event Request has been received'
            message = (
                f"Hey there {recipient}" +
                "\n\n" +
                f"Your request for {date} has been sent succesfully." +
                "\n\nWe will contact you shortly!\n\n" +
                "Grace Team"
                )
            sender = settings.EMAIL_HOST_USER
            send_mail(
                subject,
                message,
                sender,
                [recipient],
                fail_silently=False
                )
            messages.success(
                request,
                'Your request has been sent succesfully.' +
                ' We will contact you shortly'
                )
            form_events.save()
            form_events = EventBooking()
    else:
        form_events = EventBooking()
    context = {'form_events': form_events}
    return render(request, "events.html", context)


NUMBER_MAX_OF_BOOKINGS = 1


@login_required()
def booking_view(request):
    """
    BOOKING FORM
    """
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            requested_date = form.cleaned_data['date']
            requested_time = form.cleaned_data['arrival_time']
            check_for_same_booking = Booking.objects.filter(
                date=requested_date,
                arrival_time=requested_time
                ).count()
            if check_for_same_booking >= NUMBER_MAX_OF_BOOKINGS:
                messages.error(
                        request,
                        f'Sorry! {user} ' +
                        'No appointment is available on that date and time'
                        )
                return redirect('booking')
            else:
                form.instance.user = user
                sender = settings.EMAIL_HOST_USER
                subject = 'Reservation confirmation'
                message = (
                    f"Hey there {user}" +
                    "\n\n" +
                    f"Your reservation for {requested_date} is confirmed" +
                    "\n\nSee you soon!\n\n" +
                    "Grace Team"
                    )
                send_mail(
                    subject,
                    message,
                    sender,
                    [user.email],
                    fail_silently=False
                    )
                form.save()
                messages.success(
                    request,
                    f'Thank you {user} ' +
                    'Your appointment has been confirmed.'
                    )
                return redirect('booking')
            form = ReservationForm()
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'booking.html', context)


@login_required()
def booking_view_update(request):
    """
    VIEW ALL BOOKINGS
    """
    today_date = datetime.now()
    bookings = Booking.objects.filter(date__gte=today_date)
    context = {
        'bookings': bookings
    }
    return render(request, 'booking-view-all.html', context)


@login_required()
def edit_booking(request, booking_id):
    """
    EDIT RESERVATIONS
    """
    booking = get_object_or_404(Booking, id=booking_id)
    user = get_object_or_404(User, username=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=booking)
        if form.is_valid():
            new_requested_date = form.cleaned_data['date']
            new_reservation_name = form.cleaned_data['booking_name']
            new_requested_time = form.cleaned_data['arrival_time']
            new_no_of_persons = form.cleaned_data['number_of_persons']
            new_details = form.cleaned_data['booking_details']
            new_allergies = form.cleaned_data['allergies']
            form.save()
            messages.success(
                request,
                'Your request has been sent succesfully updated'
                )
            sender = settings.EMAIL_HOST_USER
            subject = 'Reservation confirmation'
            message = (
                "Hey there" +
                "\n\n" +
                "Your new reservation is confirmed \n\n" +
                "See the details below: \n" +
                f'Booking name: {new_reservation_name}' +
                '\n' +
                f'Reservation date: {new_requested_date}' +
                '\n' +
                f'Arrival time: {new_requested_time}' +
                '\n' +
                f'Number or persons: {new_no_of_persons}' +
                '\n' +
                f'Booking details: {new_details}' +
                '\n' +
                f'Allergies: {new_allergies}' +
                '\n' +
                "\n\nSee you soon!\n\n" +
                "Grace Team"
                    )
            send_mail(
                subject,
                message,
                sender,
                [user.email],
                fail_silently=False
                )
            return redirect('update-booking')
        else:
            messages.error(
                request,
                'Your request is not valid'
                )
    form = ReservationForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking-edit.html', context)


@login_required()
def delete_booking(request, booking_id):
    """
    DELETE BOOKING
    """
    booking = get_object_or_404(Booking, id=booking_id)
    sender = settings.EMAIL_HOST_USER
    subject = 'Reservation has been canceled'
    message = (
        "Hey there" +
        "\n\n" +
        "As per request, your new reservation is canceled \n\n" +
        "See you next time!\n\n" +
        "Grace Team"
        )
    send_mail(
        subject,
        message,
        sender,
        [booking.user.email],
        fail_silently=False
    )
    booking.delete()
    messages.success(
            request,
            'Your request has been sent succesfully deleted'
            )
    return redirect('update-booking')
