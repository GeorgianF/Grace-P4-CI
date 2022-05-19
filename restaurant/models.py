from django.db import models
from django.utils.text import slugify


class Allergen(models.Model):
    DAIRY = 'Dairy'
    EGGS = 'Eggs'
    FISH = 'Fish'
    SHELFISH = 'Shelfish'
    NUTS = 'Nuts'
    PEANUTS = 'Peanuts'
    WHEAT = 'Wheat'
    SOY = 'Soy'
    ALLERGENS = [
        (DAIRY, 'Dairy'),
        (EGGS, 'Eggs'),
        (FISH, 'Fish'),
        (SHELFISH, 'Shelfish'),
        (NUTS, 'Nuts'),
        (PEANUTS, 'Peanuts'),
        (WHEAT, 'Wheat'),
        (SOY, 'Soy'),
    ]
    name = models.CharField(
        ('Allergen name'),
        max_length=20,
        choices=ALLERGENS,
        unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    allergens = models.ManyToManyField(Allergen, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['name']

# https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
