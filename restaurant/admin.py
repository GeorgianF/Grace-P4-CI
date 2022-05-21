from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'course_type')
    list_filter = ('course_type', )
    search_fields = ['name', 'description']


admin.site.register(Course, CourseAdmin)
