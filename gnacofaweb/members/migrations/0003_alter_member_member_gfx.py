# Generated by Django 4.0.1 on 2021-01-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_gfx',
            field=models.CharField(max_length=7),
        ),
    ]