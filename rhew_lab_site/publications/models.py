from django.db import models


class Publication(models.Model):
    order = models.IntegerField(default=0)
    authors = models.TextField(default="", )
    title = models.CharField(max_length=400, default="")
    pub_name = models.CharField(
        max_length=255, default="", 
        verbose_name="Publisher Name",
    )
    volume = models.CharField(max_length=255, null=True)
    issue = models.CharField(max_length=255, blank=True, default="")
    pages = models.CharField(max_length=255, default="", blank=True)
    doi = models.CharField(max_length=255, default="", blank=True)
    link = models.CharField(max_length=255, default="", blank=True)
    pub_year = models.IntegerField(null=True, verbose_name="Year Published")

    class Meta:
        ordering = ["-pub_year"]