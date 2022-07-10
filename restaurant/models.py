import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


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

# Event form model for the the events.html page


class EventForm(models.Model):
    """
    Event form model
    """
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

# the booking model for the reservations


class Booking(models.Model):
    """
    Booking model
    """
    class ALLERGENS(models.TextChoices):
        """
        Allergies
        """
        NO_ALLERGIES = 'No Allergies'
        DAIRY = 'Dairy'
        EGGS = 'Eggs'
        FISH = 'Fish'
        SHELLFISH = 'Shelfish'
        NUTS = 'Nuts'
        PEANUTS = 'Peanuts'
        GLUTEN = 'Gluten'
        SOY = 'Soy'

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/
    class BookingTime(datetime.time, models.Choices):
        """
        Subclass appointment times for arrival_time field
        """
        PM_1700 = 17, 00, 00, '17:00'
        PM_1730 = 17, 30, 00, '17:30'
        PM_1800 = 18, 00, 00, '18:00'
        PM_1830 = 18, 30, 00, '18:30'
        PM_1900 = 19, 00, 00, '19:00'
        PM_1930 = 19, 30, 00, '19:30'
        PM_2000 = 20, 00, 00, '20:00'
        PM_2030 = 20, 30, 00, '20:30'
        PM_2100 = 21, 00, 00, '21:00'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    booking_details = models.CharField(max_length=500)
    arrival_time = models.TimeField(
        choices=BookingTime.choices,
        null=False,
        blank=False,
        default=BookingTime.PM_1700
        )
    number_of_persons = models.IntegerField(default=2, validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ])
    allergies = MultiSelectField(choices=ALLERGENS.choices)

    class Meta:
        """
        Order bookings by time
        """
        ordering = ['date', 'arrival_time']

    def __str__(self):
        return str(self.user)
