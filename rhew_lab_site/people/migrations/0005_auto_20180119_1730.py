# Generated by Django 2.0.1 on 2018-01-20 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20180119_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labmember',
            old_name='left_group',
            new_name='left_group_year',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='left_group',
            new_name='left_group_year',
        ),
    ]
