from django.db import models
from django.conf import settings

STATUS = [
    ("PENDING", "pending"),
    ("COMPLETED", "completed"),
    ("EXPIRED", "expired"),
]


class Farm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    size = models.FloatField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    date = models.DateField()
    cost = models.FloatField()
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default="PENDING")

    def __str__(self):
        return self.activity
