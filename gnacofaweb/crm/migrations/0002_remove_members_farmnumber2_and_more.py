# Generated by Django 4.0.2 on 2022-06-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='farmnumber2',
        ),
        migrations.RemoveField(
            model_name='members',
            name='farmnumber3',
        ),
        migrations.RemoveField(
            model_name='members',
            name='farmnumber4',
        ),
        migrations.RemoveField(
            model_name='members',
            name='farmnumber5',
        ),
        migrations.AlterField(
            model_name='members',
            name='duration',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='members',
            name='enddate',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='enddate2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='enddate3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='enddate4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='enddate5',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='members'),
        ),
        migrations.AlterField(
            model_name='members',
            name='numberofpeep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='startdate',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='startdate2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='startdate3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='startdate4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='startdate5',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]