# Generated by Django 4.0.2 on 2022-06-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_members_farmnumber2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='id',
        ),
        migrations.AlterField(
            model_name='members',
            name='gfxnumber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
