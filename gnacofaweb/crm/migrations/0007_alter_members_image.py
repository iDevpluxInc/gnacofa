# Generated by Django 4.0.2 on 2022-07-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_remove_members_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='members'),
        ),
    ]
