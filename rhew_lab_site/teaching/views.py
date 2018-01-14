from django.shortcuts import render

from . import models


def index(request):
    courses = models.Course.objects.all()
    school_years = [course.school_year for course in courses]
    school_years = sorted(set(school_years), reverse=True)
    return render(request,
                  "teaching/course_list.html",
                  {"courses": courses, "school_years": school_years, })
