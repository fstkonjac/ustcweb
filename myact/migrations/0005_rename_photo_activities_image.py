# Generated by Django 4.0.4 on 2022-06-13 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myact', '0004_remove_activities_img_url_activities_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='Photo',
            new_name='image',
        ),
    ]
