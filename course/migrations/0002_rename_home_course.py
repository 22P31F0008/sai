# Generated by Django 3.2 on 2023-11-25 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='home',
            new_name='course',
        ),
    ]
