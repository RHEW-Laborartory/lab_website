from django.contrib import admin
# from django.contrib.admin import AdminSite

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    search_fields = (
        "course_dept_num",
        "semester_season",
        "semester_year",
        "description",
    )
    ordering = ["-semester_year"]
    list_filter = ["school_year", "course_dept_num"]
    list_display = (
        "course_dept_num",
        "semester_season",
        "semester_year",
        "description",
    )


admin.site.register(Course, CourseAdmin)
