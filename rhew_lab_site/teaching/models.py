from django.db import models


class Course(models.Model):
    """Model designed for courses to be displayed with
    the index view.
    """
    school_year = models.CharField(max_length=255)
    semester_year = models.IntegerField()
    semester_season = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    course = models.CharField(max_length=255, default="")


class CourseDetail(models.Model):
    """Model designed for a particular course's detail page."""
    pass
