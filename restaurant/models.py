from django.db import models
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

# https://docs.djangoproject.com/en/4.0/ref/models/fields/
# https://pypi.org/project/django-multiselectfield/

class Course(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    ALLERGENS = [
        (1, 'None'),
        (2, 'Dairy'),
        (3, 'Eggs'),
        (4, 'Fish'),
        (5, 'Shelfish'),
        (6, 'Nuts'),
        (7, 'Peanuts'),
        (8, 'Wheat'),
        (9, 'Soy'),
    ]
    allergens = MultiSelectField(choices=ALLERGENS, default="None")

    STARTER = "Starter"
    SOUP = "Soup"
    SALADS = "Salads"
    FISH_COURSE = "Fish"
    MAIN_COURSE = "Main"
    DESSERT = "Dessert"

    COURSE_TYPE = [
        (STARTER, "Starter"),
        (SOUP, "Soup"),
        (SALADS, "Salads"),
        (FISH_COURSE, "Fish"),
        (MAIN_COURSE, 'Main'),
        (DESSERT, 'Dessert'),
    ]
    course_type = models.CharField(
        ('Course type'),
        max_length=25,
        choices=COURSE_TYPE,
        default="Starter"
        )

    class Meta:
        ordering = ['name']

# https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class EventForm(models.Model):
    user_email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = PhoneNumberField(max_length=15)
    event_date = models.DateField()
    event_details = models.CharField(max_length=500)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
