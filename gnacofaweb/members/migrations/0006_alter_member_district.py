# Generated by Django 4.0.2 on 2022-04-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_member_gfx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='district',
            field=models.CharField(max_length=500),
        ),
    ]
