# Generated by Django 2.0.1 on 2018-01-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester_year',
            field=models.IntegerField(),
        ),
    ]
