# Generated by Django 4.0.3 on 2022-03-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammatcherapp', '0005_user_age_user_gender_user_mode_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(default='begginer', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]