#!/usr/bin/python
"""Scrapes the p tags containing each presentation."""

from bs4 import BeautifulSoup
import os
import re
import requests
import sys

from django.core.wsgi import get_wsgi_application


project_path = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhew_lab_site.settings")
sys.path.append(project_path)
application = get_wsgi_application()
from people.models import LabMember 


def load_database():
    """Adds each presentation's information to an sqlite3 database"""
    res = requests.get("http://rhewlab.geog.berkeley.edu/People.html")
    res.raise_for_status
    courses_pg = BeautifulSoup(res.text, "html.parser")
    p_tags = courses_pg.select('p')

    for tag in p_tags[33:102]:
        try:
            order = re.search(r"\A\d\d?", tag.getText()).group(0)
            name = re.search(r"[a-zA-Z\-]+\s[a-zA-z]+", tag.getText()).group(0)
            details = re.search(r"\(.*\)", tag.getText()).group(0)
        except AttributeError:
            pass
        else:
            # print(order)
            # print(name)
            # print(details)
            # print("\n")

            alpha = LabMember()
            alpha.order = order
            alpha.name = name
            alpha.details = details
            alpha.save()


if __name__ == "__main__":
    load_database()
