from django.contrib import admin

from .models import LabMember, Staff


class LabMemberAdmin(admin.ModelAdmin):
    ordering = ["group", "-order"]
    list_display = [
        "name",
        "title",
        "group",
        "order"
    ]
    list_filter = [
        "group",
    ]
    search_fields = (
        "name",
        "currently"
    )
    radio_fields = {"group": admin.VERTICAL}


class StaffAdmin(admin.ModelAdmin):
    ordering = ["-order"]
    list_display = [
        "name",
        "title",
        "email",
        "joined_group",
    ]


admin.site.register(LabMember, LabMemberAdmin)
admin.site.register(Staff, StaffAdmin)
