# Generated by Django 3.0.3 on 2020-02-19 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='TestNote',
        ),
    ]