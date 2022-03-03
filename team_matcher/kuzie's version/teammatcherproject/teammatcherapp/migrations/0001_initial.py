# Generated by Django 4.0.3 on 2022-03-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(default='', max_length=7)),
                ('sport', models.CharField(default='', max_length=30)),
                ('mode', models.CharField(default='1v1', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(default='', max_length=7)),
                ('sport', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
