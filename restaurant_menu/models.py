from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ('starter', 'Starter'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Dessert'),

)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


class Item(models.Model):
    meal = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
