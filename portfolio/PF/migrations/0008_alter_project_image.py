# Generated by Django 4.1.5 on 2023-01-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PF', '0007_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]