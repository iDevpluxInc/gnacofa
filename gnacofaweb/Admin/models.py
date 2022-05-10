from email.policy import default
from django.db import models
from members.models import Member
# Create your models here.

class Loan(models.Model):
    pass

class Due(models.Model):
    pass
class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 10, blank=True)
    firstName = models.CharField(max_length=120, blank=False, null=True)
    middleName = models.CharField(max_length=120, blank=False, null=True)
    lastName = models.CharField(max_length=120, blank=False, null=True)
    day = models.CharField(max_length=3, blank=True)
    month = models.CharField(max_length=20, blank=True)
    year = models.CharField(max_length=4, blank=True)
    id_type = models.CharField(max_length=120, blank=False)
    id_number = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120, blank=False)
    telephone = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=120, blank=True)
    password = models.CharField(max_length=120, blank=True)
    gender = models.CharField(max_length=120, blank=True)
    staff_image = models.ImageField(upload_to = 'staff_pics')
    staff_id = models.CharField(max_length=120, blank=True, unique=True)
    position = models.CharField(max_length=120, blank=False)
    department = models.CharField(max_length=120, blank=False)
    emergency_person = models.CharField(max_length=120, blank=False)
    emergency_phone = models.CharField(max_length=120, blank=True, null=True)
    relationship = models.CharField(max_length=120, blank=True )
    emergency_address = models.CharField(max_length=120)
    
    def __str__(self):
        return self.staff_id + " " + self.firstName
    