from django.shortcuts import render

from . import models


def index(request):
    next_years_courses = models.Course.objects.all().filter(
        course_state="Next Year"
    )
    next_school_year = next_years_courses[0].school_year
    current_years_courses = models.Course.objects.all().filter(
        course_state="Current Year"
    )
    current_school_year = current_years_courses[0].school_year
    previous_years_courses = models.Course.objects.all().filter(
        course_state="Previous Year"
    )
    school_years = [course.school_year
                    for course in models.Course.objects.all()]
    school_years = sorted(set(school_years), reverse=True)
    return render(request,
                  "teaching/course_list.html",
                  {"next_years_courses": next_years_courses,
                   "next_school_year": next_school_year,
                   "current_years_courses": current_years_courses,
                   "current_school_year": current_school_year,
                   "previous_years_courses": previous_years_courses,
                   "school_years": school_years, })
