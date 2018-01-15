#!/usr/bin/python
import os
import sys

from django.core.wsgi import get_wsgi_application


project_path = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhew_lab_site.settings")
sys.path.append(project_path)
application = get_wsgi_application()
from teaching.models import Course


def add_previous_choice():
    """Adds the previous year choice to all courses in
    the database.
    """
    for course in Course.objects.all():
        course.course_state = "Previous Year"
        course.save()


if __name__ == "__main__":
    add_previous_choice()
