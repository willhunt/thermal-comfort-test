from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import timedelta

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Prefer not to say")
    ]
    sex = models.CharField(choices=SEX_CHOICES, default="F", max_length=1)

class OccupantModel(models.Model):
    position = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class BodyZoneModel(models.Model):
    body_zones = models.CharField(max_length=20)

class TestModel(models.Model):
    date = models.DateField(auto_now=True)
    project = models.CharField(max_length=10)
    rig = models.CharField(max_length=30)
    condition = models.CharField(max_length=20)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    notes = models.TextField()
    body_zones = models.ManyToManyField(BodyZoneModel)
    duration = models.DurationField(default=timedelta(hours=1))
    frequency = models.DurationField(default=timedelta(minutes=10))
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers")
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="participants")

    SENSATION_CHOICES = [
        ("ASHRAE", "ASHRAE scale"),
        ("Berkley", "Berkley advanced scale")
    ]
    sensation_scale = models.CharField(choices=SENSATION_CHOICES, default="Berkley", max_length=15)

    COMFORT_CHOICES = [
        ("ASHRAE", "ASHRAE scale"),
        ("Berkley", "Berkley advanced scale")
    ]
    sensation_scale = models.CharField(choices=COMFORT_CHOICES, default="Berkley", max_length=15)

class PresetZonesModel(models.Model):
    name = models.CharField(max_length=30)
    zone = models.ManyToManyField(BodyZoneModel)

class GlobalResponseModel(models.Model):
    test = models.ForeignKey('TestModel', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    occupant = models.ForeignKey('OccupantModel', on_delete=models.SET_NULL, null=True)
    sensation_change = models.IntegerField(default=0)
    acceptable = models.BooleanField(default=True)
    satisfied = models.BooleanField(default=True)
    notes = models.TextField()

class LocalResponseModel(models.Model):
    test = models.ForeignKey('TestModel', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    occupant = models.ForeignKey('OccupantModel', on_delete=models.CASCADE)
    body_zone = models.ForeignKey('BodyZoneModel', on_delete=models.SET_NULL, null=True)
    comfort = models.IntegerField(default=0)
    sensation = models.IntegerField(default=0)
    stickiness = models.IntegerField(default=0)


