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
from teaching.models import Course


def load_database():
    """Adds each course's information to an sqlite3 database"""
    res = requests.get("http://rhewlab.geog.berkeley.edu/Teaching.html")
    res.raise_for_status
    courses_pg = BeautifulSoup(res.text, "html.parser")
    p_tags = courses_pg.select('p')

    for tag in p_tags:
        if '[' in tag.getText():
            semester = re.search(r'\[\w+\s\d{4}\]', tag.getText()).group()
            semester = re.sub("\[", " ", semester)
            semester = re.sub("\]", "", semester).strip()

            season, year = semester.split(" ") 
            if season[0] == "F":
                school_year = "{}-{}".format(year, int(year)+1)
                if len(season) == 2:
                    semester = re.sub(semester[:2], "Fall", semester)
            else:
                school_year = "{}-{}".format(int(year)-1, year)
                if len(season) == 2:
                    semester = re.sub(semester[:2], "Spring", semester)
            # print(school_year)
            season, year = semester.split(" ")
            # print(season, year)
            try:
                text = re.search(r'[-\w+\s+\d+/*<*>*]*:(.*)', tag.getText()).group()
                course, description = text.split(":")
            except Exception:
                description = "<Active Service-Modified Duties>"
            
            description = re.sub("\*", "", description)
            description = re.sub("Â", "", description).strip()
            course = re.sub("Â", "", course).strip()
            # try:
            #     print(course)
            # except Exception:
            #     pass
            # print(description)
            # print('\n')

            alpha = Course()
            alpha.school_year = school_year
            alpha.semester_year = year
            alpha.semester_season = season
            alpha.description = description
            alpha.course_dept_num = course
            alpha.save()

            semester = ""
            school_year = ""
            text = ""
            course = ""
            description = ""


if __name__ == "__main__":
    load_database()
