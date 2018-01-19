from django.contrib import admin
# from django.contrib.admin import AdminSite

from .models import Course, CoursePage


class CourseAdmin(admin.ModelAdmin):
    search_fields = (
        "course_dept_num",
        "semester_season",
        "semester_year",
        "description",
        "course_state",
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


class CoursePageAdmin(admin.ModelAdmin):
    fields = ('course_dept_num',
              'course_title',
              'full_description'
              )
    search_fields = (
        "last_updated",
        "full_description",
        "course_dept_num",
        "course_title",
    )
    ordering = ["course_dept_num"]
    list_filter = ["last_updated"]
    list_display = [
        "course_dept_num",
        "course_title",
        "last_updated"
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePage, CoursePageAdmin)
