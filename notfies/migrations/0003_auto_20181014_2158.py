# Generated by Django 2.1.1 on 2018-10-15 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notfies', '0002_auto_20181014_2024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignmment',
            new_name='Assignmments',
        ),
        migrations.RenameModel(
            old_name='List',
            new_name='Lists',
        ),
    ]
