# Generated by Django 3.2.17 on 2023-05-17 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajapp', '0006_alter_studentattendence_attendence'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='studentAttendence',
            new_name='Attendance',
        ),
    ]
