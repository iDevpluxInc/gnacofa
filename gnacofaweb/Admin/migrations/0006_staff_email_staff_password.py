# Generated by Django 4.0.2 on 2022-05-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_alter_staff_staff_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
