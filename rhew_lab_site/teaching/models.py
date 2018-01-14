from django.db import models


class Course(models.Model):
    """Model designed for courses to be displayed with
    the index view.
    """
    school_year = models.CharField(max_length=255, verbose_name="School Year")
    semester_year = models.IntegerField(verbose_name="Year")
    semester_season = models.CharField(max_length=255, verbose_name="Semester")
    description = models.CharField(max_length=255)
    course_dept_num = models.CharField(max_length=255,
                                       default="",
                                       verbose_name="Course Number"
                                       )

    class Meta:
        ordering = ["-semester_year"]


class CourseDetail(models.Model):
    """Model designed for course detail pages."""
    pass
