# Generated by Django 3.2.12 on 2022-03-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammatcherapp', '0009_alter_user_age_alter_user_gender_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
