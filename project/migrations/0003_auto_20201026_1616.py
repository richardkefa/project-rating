# Generated by Django 3.1.2 on 2020-10-26 13:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201026_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='landing_page_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
