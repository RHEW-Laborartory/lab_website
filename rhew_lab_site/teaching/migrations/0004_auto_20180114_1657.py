# Generated by Django 2.0.1 on 2018-01-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0003_auto_20180114_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_dept_num',
            field=models.CharField(max_length=255, verbose_name='Course Number'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester_year',
            field=models.IntegerField(null=True, verbose_name='Year'),
        ),
    ]