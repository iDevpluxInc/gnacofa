# Generated by Django 4.0.2 on 2022-07-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_remove_profile_firstname_remove_profile_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='home_region',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hometown',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middleName',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
