# Generated by Django 4.0.3 on 2022-03-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teammatcherapp', '0003_user_age_user_experience_user_gender_user_mode_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Search',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]