# Generated by Django 3.1.1 on 2020-09-21 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200921_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_desc',
            new_name='task_dec',
        ),
    ]
