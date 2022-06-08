from django.contrib import admin
from .models import Course, EventForm


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'course_type')
    list_filter = ('course_type', )
    search_fields = ['name', 'description']


class EventFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_no', 'event_date')


courses = admin.site.register(Course, CourseAdmin)
events = admin.site.register(EventForm, EventFormAdmin)
