# Generated by Django 4.0.4 on 2022-07-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myact', '0011_alter_activities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='image',
            field=models.ImageField(default='fuckyou.jpg', upload_to='media'),
        ),
    ]
