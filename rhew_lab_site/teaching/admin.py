from django.contrib import admin
# from django.contrib.admin import AdminSite

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    search_fields = (
        "course_dept_num",
        "semester_season",
        "semester_year",
        "description",
        "course_state"
    )
    ordering = ["-semester_year"]
    list_filter = ["school_year", "course_dept_num", "course_state"]
    list_display = (
        "course_dept_num",
        "semester_season",
        "semester_year",
        "description",
        "course_state"
    )
    radio_fields = {"course_state": admin.VERTICAL}


admin.site.register(Course, CourseAdmin)
