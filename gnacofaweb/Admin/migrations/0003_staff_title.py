# Generated by Django 4.0.2 on 2022-05-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_staff_delete_executivemembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='title',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]