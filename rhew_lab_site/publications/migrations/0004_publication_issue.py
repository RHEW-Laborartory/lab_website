# Generated by Django 2.0.1 on 2018-01-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20180118_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='issue',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
