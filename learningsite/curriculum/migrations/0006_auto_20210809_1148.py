# Generated by Django 3.2.6 on 2021-08-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_imagevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagevideo',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='imagevideo',
            name='your_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
