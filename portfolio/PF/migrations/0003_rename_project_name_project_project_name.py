# Generated by Django 4.1.5 on 2023-01-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PF', '0002_alter_project_project_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Project_name',
            new_name='project_name',
        ),
    ]
