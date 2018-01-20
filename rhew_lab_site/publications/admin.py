from django.contrib import admin

from .models import Publication, Presentation


class PublicationAdmin(admin.ModelAdmin):
    search_fields = (
        "authors",
        "title",
        "pub_name",
        "doi",
        "link",
        "pub_year",
    )
    ordering = ["-pub_year", "-order"]
    list_filter = ['pub_year', "pub_name"]
    list_display = [
        "title",
        "pub_name",
        "pub_year",
        "authors",
        "order",
    ]


class PresentationAdmin(admin.ModelAdmin):
    search_fields = (
        "year",
        "description"
    )
    ordering = ["-order"]
    list_filter = ["year"]
    list_display = [
        "order",
        "description",
        "year"
    ]


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Presentation, PresentationAdmin)
