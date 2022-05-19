from django.contrib import admin

# Register your models here.
from .models import Allergen, Course

admin.site.register(Allergen)
admin.site.register(Course)
