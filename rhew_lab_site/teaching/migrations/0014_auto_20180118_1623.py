# Generated by Django 2.0.1 on 2018-01-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0013_auto_20180118_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
