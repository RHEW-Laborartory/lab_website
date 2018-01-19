# Generated by Django 2.0.1 on 2018-01-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publication_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pub_name',
            field=models.CharField(default='', max_length=255, verbose_name='Publisher Name'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pub_year',
            field=models.IntegerField(null=True, verbose_name='Year Published'),
        ),
    ]
