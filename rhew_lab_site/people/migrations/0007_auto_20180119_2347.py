# Generated by Django 2.0.1 on 2018-01-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20180119_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labmember',
            name='currently',
        ),
        migrations.RemoveField(
            model_name='labmember',
            name='joined_group',
        ),
        migrations.RemoveField(
            model_name='labmember',
            name='left_group',
        ),
        migrations.RemoveField(
            model_name='labmember',
            name='title',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='left_group',
        ),
        migrations.AddField(
            model_name='labmember',
            name='details',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='staff',
            name='joined_group',
            field=models.CharField(max_length=255),
        ),
    ]
