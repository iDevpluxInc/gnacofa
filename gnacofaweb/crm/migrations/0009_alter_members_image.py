# Generated by Django 4.0.2 on 2022-07-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_alter_members_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='members/'),
        ),
    ]
