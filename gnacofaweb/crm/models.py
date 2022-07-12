from secrets import choice
from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.forms import BooleanField, ImageField
import requests
from django.contrib.auth.models import User



# // fields for choices //
REGION = [
    ('Ashanti(Kumasi)','Ashanti(Kumasi)'),
    ('Ahafo(Gaoso)','Ahafo(Gaoso)'),
    ('Bono(Sunyani)','Bono(Sunyani)'),
    ('Western(Takoradi)','Western(Takoradi)'),
    ('Central(Cape Coast)','Central(Cape Coast)'),
    ('Bono East (Techiman)','Bono East (Techiman)'),
    ('Oti(Dambai)','Oti(Dambai)'),
    ('Volta(Ho)','Volta(Ho)'),
    ('Eastern(Koforidua)','Eastern(Koforidua)'),
    ('Western North(Sefwi Wiaso)','Western North(Sefwi Wiaso)'),
     
]
DISTRICT = [
    ('Atwima-Mponua-District','Atwima-Mponua District'),
    ('Adansi South District','Adansi South District'),
    ('Afigya-Kwabre District','Afigya-Kwabre District'),
    ('Ahafo-Ano North District','Ahafo-Ano North District'),
    ('Ahafo-Ano South District','Ahafo-Ano South District'),
    ('Amansie Central District','Amansie Central District'),
    ('Amansie West District','Amansie West District'),
    ('Asante-Akim Central Municipal District','Asante-Akim Central Municipal District'),
    ('Asante-Akim North District','Asante-Akim North District'),
    ('Asante-Akim South District','Asante-Akim South District'),
    ('Asokore-Mampong Municipal District','Asokore-Mampong Municipal District'),
    ('Atwima-Kwanwoma District','Atwima-Kwanwoma District'),
    ('Atwima-Nwabiagya District','Atwima-Nwabiagya District'),
    ('Bekwai Municipal District','Bekwai Municipal District'),
    ('Bosome-Freho District','Bosome-Freho District'),
    ('Bosomtwe District','Bosomtwe District'),
    ('Ejisu-Juaben Municipal District','Ejisu-Juaben Municipal District'),
    ('Ejura-Sekyedumase District','Ejura-Sekyedumase District'),
    ('Kumasi Metropolitan District','Kumasi Metropolitan District'),
    ('Kumawu District','Kumawu District'),
    ('Kwabre East District','Kwabre East District'),
    ('Mampong Municipal District','Mampong Municipal District'),
    ('Obuasi Municipal District','Obuasi Municipal District'),
    ('Offinso Municipal District','Offinso Municipal District'),
    ('Offinso North District','Offinso North District'),
    ('Sekyere-Afram Plains District (map)','Sekyere-Afram Plains District (map)'),
    ('Sekyere East District','Sekyere East District'),
    ('Sekyere South District (map)','Sekyere South District (map)'),
    ('Adansi North District (map)','Adansi North District (map)'),
    ('Berekum East Municipal District','Berekum Wast Municipal District'), # // Bono Region
    ('Berekum West Municipal District','Berekum West Municipal District'),
    ('Dormaa East District','Dormaa East District'),
    ('Dormaa Central Municipal District','Dormaa Central Municipal District'),
    ('Dormaa West District','Dormaa West District'),
    ('Jaman North District','Jaman North District'),
    ('Jaman South District','Jaman South District'),
    ('Sunyani Municipal District','Sunyani Municipal District'),
    ('Sunyani West District','Sunyani West District'),
    ('Tain District','Tain District'),
    ('Banda District','Banda District'),
    ('Asunafo South District','Asunafo South District'), # // Ahafo District //
    ('Asutifi District','Asutifi District'),
    ('Asutifi South District','Asutifi South District'),
    ('Atebubu-Amantin District','Atebubu-Amantin District'),
    ('Kintampo North Municipal District','Kintampo North Municipal District'),
    ('Kintampo South District','Kintampo South District'),
    ('Nkoranza North District','Nkoranza North District'),
    ('Nkoranza South Municipal District','Nkoranza South Municipal District'),
    ('Pru District','Pru District'),
    ('Sene East District','Sene East District'),
    ('Sene West District','Sene West District'),
    ('Tano North District','Tano North District'),
    ('Tano South District','Tano South District'),
    ('Techiman Municipal District','Techiman Municipal District'),
    ('Techiman North District','Techiman North District'),
    ('Asunafo North Municipal District','Asunafo North Municipal District'),
    ('Abura - Asebu - Kwamankese District','Abura - Asebu - Kwamankese District'), # // Central District //
    ('Agona West Municipal District','Agona West Municipal District'),
    ('Ajumako-Enyan-Essiam District','Ajumako-Enyan-Essiam District'),
    ('Asikuma - Odoben - Brakwa District','Asikuma - Odoben - Brakwa District'),
    ('Assin North Municipal District','Assin North Municipal District'),
    ('Assin South District','Assin South District'),
    ('Awutu-Senya District','Awutu-Senya District'),
    ('Awutu Senya East Municipal District','Awutu Senya East Municipal District'),
    ('Cape Coast Metropolitan District','Cape Coast Metropolitan District'),
    ('Effutu Municipal District','Effutu Municipal District'),
    ('Ekumfi District','Ekumfi District'),
    ('Gomoa East District','Gomoa East District'),
    ('Gomoa West District','Gomoa West District'),
    ('Komenda-Edina','Komenda-Edina'),
    ('Eguafo-Abrem Municipal District','Eguafo-Abrem Municipal District'),
    ('Mfantseman Municipal District','Mfantseman Municipal District'),
    ('Twifo Atti - Mokwa District','Twifo Atti - Mokwa District'),
    ('Twifo Hemang - Lower Denkyira District','Twifo Hemang - Lower Denkyira District'),
    ('Upper Denkyira East Municipal District','Upper Denkyira East Municipal District'),
    ('Upper Denkyira West District','Upper Denkyira West District'),
    ('Agona East District','Agona East District'),
    ('Aowin District','Aowin District'), # // Western North
    ('Bia District','Bia District'),
    ('Bia East District','Bia East District'),
    ('Bibiani-Anhwiaso-Bekwai District','Bibiani-Anhwiaso-Bekwai District'),
    ('Bodi District','Bodi District'),
    ('Sefwi-Wiawso District','Sefwi-Wiawso District'),
    ('Yilo Krobo Municipal District','Yilo Krobo Municipal District'),
    ('Suaman District','Suaman District'),
    ('Juaboso District','Juaboso District'),
    ('Sefwi-Akontombra District','Sefwi-Akontombra District'),
    ('Keta','Keta'), # // Volta Region //
    ('Kpando','Kpando'),
    ('Ho','Ho'),
    ('Kadjebi','Kadjebi'),
    ('South Tongu','South Tongu'),
    ('South Dayi','South Dayi'),
    ('Krachi East','Krachi East'),
    ('Ketu North','Ketu North'),
    ('Nkwanta North','Nkwanta North'),
    ('Biakoye','Biakoye'),
    ('Nkwanta South','Nkwanta South'),
    ('Jasikan','Jasikan'),
    ('North Dayi','North Dayi'),
    ('Central Tongu','Central Tongu'),
    ('Krachi West','Krachi West'),
    ('Afadzato - South','Afadzato - South'),
    ('Agortime Ziope','Agortime Ziope'),
    ('North Tongu','North Tongu'),
    ('Akatsi North','Akatsi North'),
    ('Ho West','Ho West'),
    ('Krachi Ntsumuru','Krachi Ntsumuru'),
    ('Adaklu','Adaklu'),
    ('Akatsi South','Akatsi South'),
    ('>Ketu South','>Ketu South'),
    ('Hohoe','Hohoe'),
    ('Atebubu Amantin Municipal','Atebubu Amantin Municipal'), # // Bono East Region
    ('Kintampo South','Kintampo South'),
    ('Nkoranza North','Nkoranza North'),
    ('Nkoranza South Municipal','Nkoranza South Municipal'),
    ('Pru','Pru'),
    ('Sene East','Sene East'),
    ('Sene West','Sene West'),
    ('Techiman Municipal','Techiman Municipal'),
    ('Techiman North','Techiman North'),
    ('Kintampo Municipal','Kintampo Municipal'),
    ('JASIKAN DISTRICT','JASIKAN DISTRICT'), # // Oti Region
    ('KRACHI EAST MUNICIPAL','KRACHI EAST MUNICIPAL'),
    ('BIAKOYE DISTRICT','BIAKOYE DISTRICT'),
    ('KADJEBI DISTRICT','KADJEBI DISTRICT'),
    ('KRACHI NCHUMURU DISTRICT','KRACHI NCHUMURU DISTRICT'),
    ('KRACHI WEST DISTRICT','KRACHI WEST DISTRICT'),
    ('NKWANTA NORTH DISTRICT','NKWANTA NORTH DISTRICT'),
    ('NKWANTA SOUTH MUNICIPAL','NKWANTA SOUTH MUNICIPAL'),
    ('Akwapim North Municipal District','Akwapim North Municipal District'), # // Eastern Region
    ('Akyemansa District','Akyemansa District'),
    ('Asuogyaman District','Asuogyaman District'),
    ('Atiwa District','Atiwa District'),
    ('Ayensuano District','Ayensuano District'),
    ('Birim Central Municipal District','Birim Central Municipal District'),
    ('Birim North District','Birim North District'),
    ('Birim South District','Birim South District'),
    ('Denkyembour District','Denkyembour District'),
    ('East Akim Municipal District','East Akim Municipal District'),
    ('Fanteakwa District','Fanteakwa District'),
    ('Kwaebibirem District','Kwaebibirem District'),
    ('Kwahu Afram Plains North District','Kwahu Afram Plains North District'),
    ('Kwahu Afram Plains South District','Kwahu Afram Plains South District'),
    ('Kwahu East District','Kwahu East District'),
    ('Kwahu South District','Kwahu South District'),
    ('Kwahu West Municipal District','Kwahu West Municipal District'),
    ('Lower Manya Krobo Municipal District','Lower Manya Krobo Municipal District'),
    ('New Juaben Municipal District','New Juaben Municipal District'),
    ('Nsawam - Adoagyire Municipal District','Nsawam - Adoagyire Municipal District'),
    ('Suhum Municipal District','Suhum Municipal District'),
    ('Upper Manya Krobo District','Upper Manya Krobo District'),
    ('Upper West Akim District','Upper West Akim District'),
    ('West Akim Municipal','West Akim Municipal'),
    ('Akwapim South District','Akwapim South District'),    
]
TITLE = [
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss'),
    ('Dr','Dr'),
    ('Engr','Engr'),
    ('Nana','Nana'),
    ('Ohemaa','Ohemaa'),
]
MONTH_OF_BIRTH = [
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December'),
]
GENDER = [
    ('Male','Male'),
    ('Female','Female'),
]
LEVEL_OF_EDUCATION = [
    ('Basic Education','Basic Education'),
    ('JHS/JSS','JHS/JSS'),
    ('Middle School Leaving Certificate','Middle School Leaving Certificate'),
    ('High School/Secondary School','High School/Secondary School'),
    ('Tertiary Level','Tertiary Level'),
]
ID_TYPE = [
    ('National ID (Ghana Card)','National ID (Ghana Card)'),
    ('Voters ID','Voters ID'),
]
MARITAL_STATUS = [
    ('Single','Single'),
    ('Married','Married'),
    ('Divorced','Divored'),
    ('Widow','Widow'),
    ('Widower','Widower'),
]
NUMBER_OF_FARMS = [
    ('One','1'),
    ('Two','2'),
    ('Three','3'),
    ('Four','4'),
    ('Five','5'),
]
FARM_OWNER_SELECTION = [
    ('self','self'),
    ('labourer','labourer'),
    ('rented','rented/lease'),
    ('cropsharing','crop sharing'),
    ('family','family'),
    
]
QUEST = [
    ('yes','Yes'),
    ('No','No'),
]


# Create your models here.

# // Members Database model //
class Members(models.Model):
    gfxnumber = models.CharField(max_length=10, primary_key=True, unique=True, blank=False)
    region = models.CharField(max_length=120, blank=False, null=False, choices = REGION)
    district = models.CharField(max_length=120, blank=False, null=False, choices = DISTRICT)
    society = models.CharField(max_length=120, blank=False, null=False)
    title = models.CharField(max_length=20, blank=False, choices = TITLE)
    image = models.ImageField(default='default.jpg', upload_to='members/')
    firstname = models.CharField(max_length=120, blank=False)
    middlename = models.CharField(max_length=120, blank=True)
    lastname = models.CharField(max_length=120, blank=False)
    preferredname = models.CharField(max_length=120,blank=True )
    day = models.IntegerField()
    month = models.CharField(max_length=120, blank=False, choices = MONTH_OF_BIRTH)
    year = models.IntegerField()
    gender = models.CharField(max_length=100, blank=False, choices = GENDER)
    hometown = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=120, blank=False)
    education = models.CharField(max_length=100, blank=False, choices = LEVEL_OF_EDUCATION)
    idtype = models.CharField(max_length=100, blank=False, choices = ID_TYPE)
    idnum = models.IntegerField()
    phone = models.CharField(max_length=10,blank=False)
    marriage = models.CharField(max_length=120, blank=False, choices = MARITAL_STATUS)
    spousename = models.CharField(max_length=120, blank=True)
    spouseoccupation = models.CharField(max_length=120, blank=True)
    spousenumber = models.CharField(max_length=10, blank=True)
    kinsname = models.CharField(max_length=120, blank=False)
    kinsrelationship = models.CharField(max_length=120, blank=True)
    kinsnumber = models.CharField(max_length=10, blank=False)
    familysize = models.IntegerField(blank=False)
    farmnumber = models.IntegerField()
    farmowner = models.CharField(max_length=120, blank=False, null=False, choices=FARM_OWNER_SELECTION)
    crop = models.CharField(max_length=20, blank=True)
    farmsize = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=150, blank=True)
    loc_latitude = models.FloatField(blank=True, null=True)
    loc_longitude = models.FloatField(blank=True, null=True)
    farmowner2 = models.CharField(max_length=120, blank=True, null=True, choices=FARM_OWNER_SELECTION)
    crop2 = models.CharField(max_length=20, blank=True)
    farmsize2 = models.FloatField(blank=True, null=True)
    location2 = models.CharField(max_length=150, blank=True)
    loc_latitude2 = models.FloatField(blank=True, null=True)
    loc_longitude2 = models.FloatField(blank=True, null=True)
    farmowner3 = models.CharField(max_length=120, blank=True, null=True, choices=FARM_OWNER_SELECTION)
    crop3 = models.CharField(max_length=20, blank=True)
    farmsize3 = models.FloatField(blank=True, null=True)
    location3 = models.CharField(max_length=150, blank=True)
    loc_latitude3 = models.FloatField(blank=True, null=True)
    loc_longitude3 = models.FloatField(blank=True, null=True)
    farmowner4 = models.CharField(max_length=120, blank=True, null=True, choices=FARM_OWNER_SELECTION)
    crop4 = models.CharField(max_length=20, blank=True)
    farmsize4 = models.FloatField(blank=True, null=True)
    location4 = models.CharField(max_length=150, blank=True)
    loc_latitude4 = models.FloatField(blank=True, null=True)
    loc_longitude4 = models.FloatField(blank=True, null=True)
    farmowner5 = models.CharField(max_length=120, blank=True, null=True, choices=FARM_OWNER_SELECTION)
    crop5 = models.CharField(max_length=20, blank=True)
    farmsize5 = models.FloatField(blank=True, null=True)
    location5 = models.CharField(max_length=150, blank=True)
    loc_latitude5 = models.FloatField(blank=True, null=True)
    loc_longitude5 = models.FloatField(blank=True, null=True)
    farmingyears = models.IntegerField(blank=False)
    bbf = models.CharField(max_length=150, blank=True)
    baf = models.CharField(max_length=150, blank=True)
    averageyield = models.IntegerField()
    previousyield = models.IntegerField()
    farmbenefit = models.CharField(max_length=150, blank=False)
    buyerofproduce = models.CharField(max_length=150, blank=False)
    numberoftimes = models.CharField(max_length=150, blank=False)
    buyerbenefits = models.CharField(max_length=150, blank=False)
    useoffund = models.TextField(max_length=150, blank=True)
    transactingbank = models.CharField(max_length=150, blank=True)
    duration = models.CharField(max_length=120, blank=False, null=False)
    partoffarmers = models.CharField(max_length=150, blank=True)
    declaration = models.BooleanField(default=False)
    date_created = models.DateTimeField(blank=False, auto_now=True, editable=False)
    #resgistrar = models.ForeignKey(User, on_delete=SET)
    
    def __str__(self):
        return self.gfxnumber + " " + self.firstname

# // Loans Database model //
class Loan(models.Model):
    pass

# // Dues Database model //
class Due(models.Model):
    pass

# // Staff Database model //

class Profile(models.Model):
    access_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=True)
    staff_id = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    region = models.CharField(max_length=120, blank=False, null=True, choices = REGION)
    district = models.CharField(max_length=120, blank=False, null=True, choices=DISTRICT)
    society = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length = 10, blank=False, null=False, choices=TITLE)
    firstName = models.CharField(max_length = 120, blank=False, null=True)
    middleName = models.CharField(max_length = 120, blank=False, null=True)
    lastName = models.CharField(max_length = 120, blank=False, null=True)
    day = models.CharField(max_length=3, blank=True)
    month = models.CharField(max_length=20, blank=False, null=False, choices=MONTH_OF_BIRTH)
    year = models.CharField(max_length=4, blank=False, null=False)
    id_type = models.CharField(max_length=120, blank=False, null=False, choices=ID_TYPE)
    id_number = models.CharField(max_length=120, blank=False, null=False)
    address = models.CharField(max_length=120, blank=False, null=False)
    hometown = models.CharField(max_length = 120, blank=False, null=True)
    home_region = models.CharField(max_length = 120, blank=False, null=True)
    telephone = models.CharField(max_length=14, blank=False)
    email = models.EmailField(max_length=120, blank=True)
    gender = models.CharField(max_length=120, blank=False, null=False, choices=GENDER)
    staff_image = models.ImageField(upload_to = 'staff_pics',  default='default.jpg', blank=False, null=False)
    position = models.CharField(max_length=120, blank=False, null=False)
    department = models.CharField(max_length=120, blank=False, null=False)
    emergency_person = models.CharField(max_length=120, blank=False)
    emergency_phone = models.CharField(max_length=10, blank=False, null=False)
    relationship = models.CharField(max_length=120, blank=False, null=False )
    emergency_address = models.CharField(max_length=120, blank=False, null=False)
    
    
    def __str__(self):
        return self.staff_id
    