from django.contrib import admin
from .models import Course, EventForm, Booking


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'course_type')
    list_filter = ('course_type', )
    search_fields = ['name', 'description']


class EventFormAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_no',
        'event_date',
        'event_details'
        )


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'booking_name',
        'date',
        'arrival_time',
        'allergies',
        'booking_details'
        )


courses = admin.site.register(Course, CourseAdmin)
events = admin.site.register(EventForm, EventFormAdmin)
booking = admin.site.register(Booking, BookingAdmin)
