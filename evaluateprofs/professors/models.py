from django.db import models
from django.contrib.auth.models import User


RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )


class Professor(models.Model):
    name = models.CharField(max_length=124)
    school = models.CharField(max_length=124)
    department = models.CharField(max_length=124)
    title = models.CharField(max_length=124)
    communication = models.DecimalField(default=0, max_digits=5,
                                        decimal_places=2)
    marking = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    objectivity = models.DecimalField(default=0, max_digits=5,
                                      decimal_places=2)
    quality = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    score = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    comments_number = models.PositiveSmallIntegerField(default=0)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete="deleted")
    anonymity = models.BooleanField(default=False)
    text = models.CharField(max_length=400)
    communication = models.DecimalField(default=0, choices=RATING_CHOICES,
                                        max_digits=1, decimal_places=0)
    marking = models.DecimalField(default=0, choices=RATING_CHOICES,
                                  max_digits=1, decimal_places=0)
    objectivity = models.DecimalField(default=0, choices=RATING_CHOICES,
                                      max_digits=1, decimal_places=0)
    quality = models.DecimalField(default=0, choices=RATING_CHOICES,
                                  max_digits=1, decimal_places=0)
    score = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    professor = models.ForeignKey(Professor, on_delete="deleted")
    publish_date = models.DateField(auto_now=False, auto_now_add=True,
                                        null=True, blank=True)
