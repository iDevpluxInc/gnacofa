# Generated by Django 4.0.1 on 2021-01-01 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='author',
        ),
    ]
