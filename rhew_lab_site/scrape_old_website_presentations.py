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
from publications.models import Presentation


def load_database():
    """Adds each presentation's information to an sqlite3 database"""
    res = requests.get("http://rhewlab.geog.berkeley.edu/Presentations.html")
    res.raise_for_status
    courses_pg = BeautifulSoup(res.text, "html.parser")
    p_tags = courses_pg.select('.paragraph_style_2')

    for tag in p_tags:
        order = 0
        description = ""
        year = 0000 
        sorted_description = re.findall(r'''
            (?P<order>\A\d\d?)
            (?P<description>.*)
        ''', tag.getText(), re.X | re.M | re.I | re.X)
        try:
            order, description = sorted_description[0]
        except IndexError:
            pass
        else:
            while "Â" in description:
                description = re.sub("Â", "", description).strip()
            description = re.sub("\A.", "", description).strip()
            description = re.sub(",\Z", ".", description).strip()
            description = re.sub("Ã©", "é", description)
            description = re.sub("stergaard", "Østergaard", description)

            # print(order)
            # print(description)

            try:
                year = re.findall(r'19\d{2}|20\d{2}', description)[0]
            except IndexError:
                pass
            else:
                print(year)
            # print("\n")

            alpha = Presentation()
            alpha.order = order
            alpha.description = description
            if year:
                alpha.year = year
            alpha.save()

            


if __name__ == "__main__":
    load_database()
