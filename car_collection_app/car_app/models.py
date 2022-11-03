from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import ModelForm


def car_year_validate(year):
    if not 1980 <= year <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


def age_validate(age):
    if age < 18:
        raise ValidationError("Age must be equal or above 18")


def car_price_validator(price):
    if price < 1:
        raise ValidationError("The price cannot be less than 1")


def name_len_validator(name):
    if len(name) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


class Profile(models.Model):
    username = models.CharField(max_length=10, null=False, blank=False,
                                validators=(name_len_validator,))
    email = models.EmailField(null=False, blank=False, )
    age = models.IntegerField(null=False, blank=False, validators=(age_validate,))
    password = models.CharField(max_length=30, null=False, blank=False, )
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True, )


class Car(models.Model):
    SPORT = "Sports Car"
    PICKUP = "Pickup"
    CROSS = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CHOICES = (
        (SPORT, SPORT),
        (PICKUP, PICKUP),
        (CROSS, CROSS),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(max_length=10, null=False, blank=False, choices=CHOICES)
    model = models.CharField(max_length=20, null=False, blank=False, validators=(MinLengthValidator(2),))
    year = models.IntegerField(null=False, blank=False, validators=(car_year_validate,))
    image_url = models.URLField(null=False, blank=False, )
    price = models.FloatField(null=False, blank=False, validators=(car_price_validator,))


