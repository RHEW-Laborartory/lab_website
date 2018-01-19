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
                                       verbose_name="Course Number",
                                       )

    STATE_CHOICES = (("Previous Year", "Previous Year"),
                     ("Current Year", "Current Year"),
                     ("Next Year", "Next Year"))
    course_state = models.CharField(
        max_length=255, choices=STATE_CHOICES, default="Previous Year"
    )

    class Meta:
        ordering = ["-semester_year"]


class CoursePage(models.Model):
    """Model designed for course detail pages."""
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    full_description = models.TextField(verbose_name="Description", default="")
    course_dept_num = models.CharField(
        max_length=255, verbose_name="Course Number", default=""
    )
    course_title = models.CharField(
        max_length=255, verbose_name="Title", default=""
    )

    class Meta:
        ordering = ["course_dept_num"]

    def previous_years(self, course_dept_num):
        previous_years = []
        courses = models.Course.objects.all().filter(
            course_dept_num=course_dept_num,
        )
        for course in courses:
            year = course.semester_year
            semseter = course.semester_season
            previous_years.append((year, semseter))
        return sorted(previous_years)



