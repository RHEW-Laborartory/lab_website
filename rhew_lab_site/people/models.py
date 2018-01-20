from datetime import date

from django.db import models


class People(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    joined_group = models.DateField(default=date.today)
    left_group = models.DateField(blank=True, default=date.today)

    class Meta:
        abstract = True
        ordering = ['-order']


class Staff(People):
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    office = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    background_link = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Staff"


class LabMember(People):
    GROUP_CHOICES = (
        ("Undergraduate Researcher", "Undergraduate Researcher"),
        ("Graduate Student", "Graduate Student"),
        ("Visiting Scholar/Post-Doctoral Researcher",
         "Visiting Scholar/Post-Doctoral Researcher"),
    )
    group = models.CharField(
        max_length=255,
        choices=GROUP_CHOICES,
        default="Undergraduate Researcher"
    )
    currently = models.CharField(
        max_length=255,
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        default="Undergraduate Researcher"
    )
