# Generated by Django 2.1.1 on 2018-10-15 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notfies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignmments',
            new_name='Assignmment',
        ),
        migrations.RenameModel(
            old_name='Lists',
            new_name='List',
        ),
    ]