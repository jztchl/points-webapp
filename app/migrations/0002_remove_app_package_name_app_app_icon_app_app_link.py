# Generated by Django 5.1 on 2024-08-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='package_name',
        ),
        migrations.AddField(
            model_name='app',
            name='app_icon',
            field=models.ImageField(blank=True, null=True, upload_to='app_icon/'),
        ),
        migrations.AddField(
            model_name='app',
            name='app_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
