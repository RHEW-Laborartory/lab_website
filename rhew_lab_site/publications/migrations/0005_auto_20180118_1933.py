# Generated by Django 2.0.1 on 2018-01-19 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_publication_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='issue',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
