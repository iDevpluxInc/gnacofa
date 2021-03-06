# Generated by Django 4.0.2 on 2022-06-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gfxnumber', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=120)),
                ('district', models.CharField(max_length=120)),
                ('society', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='members')),
                ('firstname', models.CharField(max_length=120)),
                ('middlename', models.CharField(blank=True, max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('preferredname', models.CharField(blank=True, max_length=120)),
                ('day', models.IntegerField()),
                ('month', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=120)),
                ('education', models.CharField(max_length=100)),
                ('idtype', models.CharField(max_length=100)),
                ('idnum', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('marriage', models.CharField(max_length=120)),
                ('spousename', models.CharField(blank=True, max_length=120)),
                ('spouseoccupation', models.CharField(blank=True, max_length=120)),
                ('spousenumber', models.CharField(blank=True, max_length=10)),
                ('kinsname', models.CharField(max_length=120)),
                ('kinsrelationship', models.CharField(blank=True, max_length=120)),
                ('kinsnumber', models.CharField(max_length=10)),
                ('familysize', models.CharField(max_length=6)),
                ('farmnumber', models.IntegerField()),
                ('farmowner', models.CharField(blank=True, max_length=120)),
                ('crop', models.CharField(blank=True, max_length=20)),
                ('farmsize', models.CharField(blank=True, max_length=120)),
                ('location', models.CharField(blank=True, max_length=150)),
                ('loc_latitude', models.CharField(blank=True, max_length=150)),
                ('loc_longitutde', models.CharField(blank=True, max_length=150)),
                ('ownersfullname', models.CharField(blank=True, max_length=120)),
                ('ownersgfx', models.CharField(blank=True, max_length=10)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('numberofpeep', models.CharField(blank=True, max_length=10)),
                ('namesofpeep', models.CharField(blank=True, max_length=150)),
                ('caretaker', models.CharField(blank=True, max_length=15)),
                ('namesoffamilymembers', models.CharField(blank=True, max_length=150)),
                ('farmnumber2', models.IntegerField()),
                ('farmowner2', models.CharField(blank=True, max_length=120)),
                ('crop2', models.CharField(blank=True, max_length=20)),
                ('farmsize2', models.CharField(blank=True, max_length=120)),
                ('location2', models.CharField(blank=True, max_length=150)),
                ('loc_latitude2', models.CharField(blank=True, max_length=150)),
                ('loc_longitutde2', models.CharField(blank=True, max_length=150)),
                ('ownersfullname2', models.CharField(blank=True, max_length=120)),
                ('ownersgfx2', models.CharField(blank=True, max_length=10)),
                ('startdate2', models.DateField()),
                ('enddate2', models.DateField()),
                ('numberofpeep2', models.CharField(blank=True, max_length=10)),
                ('namesofpeep2', models.CharField(blank=True, max_length=150)),
                ('caretaker2', models.CharField(blank=True, max_length=15)),
                ('namesoffamilymembers2', models.CharField(blank=True, max_length=150)),
                ('farmnumber3', models.IntegerField()),
                ('farmowner3', models.CharField(blank=True, max_length=120)),
                ('crop3', models.CharField(blank=True, max_length=20)),
                ('farmsize3', models.CharField(blank=True, max_length=120)),
                ('location3', models.CharField(blank=True, max_length=150)),
                ('loc_latitude3', models.CharField(blank=True, max_length=150)),
                ('loc_longitutde3', models.CharField(blank=True, max_length=150)),
                ('ownersfullname3', models.CharField(blank=True, max_length=120)),
                ('ownersgfx3', models.CharField(blank=True, max_length=10)),
                ('startdate3', models.DateField()),
                ('enddate3', models.DateField()),
                ('numberofpeep3', models.CharField(blank=True, max_length=10)),
                ('namesofpeep3', models.CharField(blank=True, max_length=150)),
                ('caretaker3', models.CharField(blank=True, max_length=15)),
                ('namesoffamilymembers3', models.CharField(blank=True, max_length=150)),
                ('farmnumber4', models.IntegerField()),
                ('farmowner4', models.CharField(blank=True, max_length=120)),
                ('crop4', models.CharField(blank=True, max_length=20)),
                ('farmsize4', models.CharField(blank=True, max_length=120)),
                ('location4', models.CharField(blank=True, max_length=150)),
                ('loc_latitude4', models.CharField(blank=True, max_length=150)),
                ('loc_longitutde4', models.CharField(blank=True, max_length=150)),
                ('ownersfullname4', models.CharField(blank=True, max_length=120)),
                ('ownersgfx4', models.CharField(blank=True, max_length=10)),
                ('startdate4', models.DateField()),
                ('enddate4', models.DateField()),
                ('numberofpeep4', models.CharField(blank=True, max_length=10)),
                ('namesofpeep4', models.CharField(blank=True, max_length=150)),
                ('caretaker4', models.CharField(blank=True, max_length=15)),
                ('namesoffamilymembers4', models.CharField(blank=True, max_length=150)),
                ('farmnumber5', models.IntegerField()),
                ('farmowner5', models.CharField(blank=True, max_length=120)),
                ('crop5', models.CharField(blank=True, max_length=20)),
                ('farmsize5', models.CharField(blank=True, max_length=120)),
                ('location5', models.CharField(blank=True, max_length=150)),
                ('loc_latitude5', models.CharField(blank=True, max_length=150)),
                ('loc_longitutde5', models.CharField(blank=True, max_length=150)),
                ('ownersfullname5', models.CharField(blank=True, max_length=120)),
                ('ownersgfx5', models.CharField(blank=True, max_length=10)),
                ('startdate5', models.DateField()),
                ('enddate5', models.DateField()),
                ('numberofpeep5', models.CharField(blank=True, max_length=10)),
                ('namesofpeep5', models.CharField(blank=True, max_length=150)),
                ('caretaker5', models.CharField(blank=True, max_length=15)),
                ('namesoffamilymembers5', models.CharField(blank=True, max_length=150)),
                ('farmingyears', models.IntegerField()),
                ('bbf', models.CharField(blank=True, max_length=150)),
                ('baf', models.CharField(blank=True, max_length=150)),
                ('averageyield', models.IntegerField()),
                ('previousyield', models.IntegerField()),
                ('farmbenefit', models.CharField(max_length=150)),
                ('buyerofproduce', models.CharField(max_length=150)),
                ('numberoftimes', models.CharField(max_length=150)),
                ('buyerbenefits', models.CharField(max_length=150)),
                ('useoffund', models.CharField(blank=True, max_length=150)),
                ('transactingbank', models.CharField(blank=True, max_length=150)),
                ('duration', models.DurationField()),
                ('partoffarmers', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
