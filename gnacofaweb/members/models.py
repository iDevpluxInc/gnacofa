from email.policy import default
from django.db import models
from django.utils import timezone

#from django.contrib.auth.models import User



# Create your models here.
class Member(models.Model):
    member_gfx = models.CharField(max_length=10)
    region = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    society = models.CharField(max_length=120)
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    preferred_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    educational_level = models.CharField(max_length=120)
    hometown = models.CharField(max_length=120)
    id_type = models.CharField(max_length=120)
    id_number = models.CharField(max_length=30)
    marriage_status = models.CharField(max_length=120)
    spoue_name = models.CharField(max_length=120)
    spouse_occupation = models.CharField(max_length=120)
    spouse_number = models.CharField(max_length=120)
    next_of_kin = models.CharField(max_length=120)
    number_kin = models.CharField(max_length=120)
    relationship_kin = models.CharField(max_length=120)
    number_kin = models.CharField(max_length=120)
    Num_partners = models.CharField(max_length=30)
    family_size = models.CharField(max_length=30)
    image = models.ImageField(default = 'default.jpg', upload_to='pics')
    owner_of_farm = models.CharField(max_length=120)
    number_of_labourers = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    name_of_owner = models.CharField(max_length=120)
    owners_gfx = models.CharField(max_length=120)
    how_many_people = models.CharField(max_length=30)
    names_of_families = models.TextField()
    crop_cultivated = models.CharField(max_length=120)
    farm_size = models.CharField(max_length=30)
    farm_location = models.CharField(max_length=120)
    years_in_farming = models.CharField(max_length=30)
    side_business = models.CharField(max_length=120)
    side_business_specify = models.CharField(max_length=120)
    current_side_business = models.CharField(max_length=120)
    current_business_specify = models.CharField(max_length=120)
    average_yield = models.CharField(max_length=30)
    previous_yield = models.CharField(max_length=30)
    benefit_from_farm = models.CharField(max_length=120)
    buyer_of_produce = models.CharField(max_length=120)
    number_of_times = models.CharField(max_length=120)
    benefit_from_buyer = models.CharField(max_length=120)
    usage_of_funds = models.CharField(max_length=120)
    bank_transacting_with = models.CharField(max_length=120)
    other_specify = models.CharField(max_length=120)
    how_long = models.CharField(max_length=120)
    interes_in_gnacofa = models.CharField(max_length=120)
    specify_why = models.CharField(max_length=120)
    date_submitted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.member_gfx
    
    
