# Generated by Django 2.0.1 on 2018-01-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0007_auto_20180114_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_state',
            field=models.CharField(choices=[('previous_year', 'Previous Year'), ('current_year', 'Current Year'), ('next_year', 'Next Year')], default='previous_year', max_length=255),
        ),
    ]
