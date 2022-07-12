
from cProfile import label
from email.policy import default
from multiprocessing.sharedctypes import Value
from django import forms
from django.forms import ModelForm
from .models import Members, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    #email = forms.EmailField()
    #first_name = forms.CharField(max_length=120,)
    #last_name = forms.CharField(max_length=120,)
    #user_permissions = forms.MultiValueField()
    is_active = forms.BooleanField()
    is_staff = forms.BooleanField()
    
    
    
    class Meta:
        model = User
        fields = ['username','password1', 'password2','is_active','is_staff']
        
        
class MemberCreationForm(ModelForm):
    class Meta:
        model = Members
        fields = ('gfxnumber','region', 'district', 'society', 'title','image', 'firstname', 'middlename', 'lastname', 'preferredname', 'day', 'month', 'year','gender', 'hometown', 'address', 'education', 'idtype', 'idnum', 'phone', 'marriage', 'spousename', 'spouseoccupation', 'spousenumber', 'kinsname','kinsrelationship', 'kinsnumber', 'familysize', 'farmnumber','farmowner','crop', 'farmsize', 'location' , 'loc_latitude', 'loc_longitude', 'farmowner2','crop2', 'farmsize2', 'location2' , 'loc_latitude2', 'loc_longitude2', 'farmowner3','crop3', 'farmsize3', 'location3' , 'loc_latitude3', 'loc_longitude3', 'farmowner4','crop4', 'farmsize4', 'location4' , 'loc_latitude4', 'loc_longitude4', 'farmowner5','crop5', 'farmsize5', 'location5' , 'loc_latitude5', 'loc_longitude5','farmingyears', 'bbf', 'baf', 'averageyield', 'previousyield','farmbenefit', 'buyerofproduce', 'numberoftimes', 'buyerbenefits', 'useoffund', 'transactingbank', 'duration', 'partoffarmers', 'declaration')
        labels = {
            'gfxnumber': 'GFX Number',
            'region':'Region', 
            'district':'District', 
            'society':'Society', 
            'title':'Title', 
            'image':'Upload Image Here', 
            'firstname':'First Name', 
            'middlename':'Middle Name', 
            'lastname':'Last Name', 
            'preferredname':'Preferred Name', 
            'day':'Day', 
            'month':'Month',
            'year':'Year', 
            'gender':'Gender',
            'hometown':'Hometown',
            'address':'Address',
            'education':'Level of Education',
            'idtype':'ID Type',
            'idnum':'ID Num',
            'phone':'Phone',
            'marriage':'Marital Status',
            'spousename':'Spouse Name',
            'spouseoccupation':'Spouse Occupation',
            'spousenumber':'Spouse Number',
            'kinsname':'Next of Kins Nmae',
            'kinsrelationship':'Relationship to Next of Kins ',
            'kinsnumber':'Next of Kins Number',
            'familysize':'Family Size',
            'farmnumber':'Number of Farms',
            'farmowner':'Owner of Farm',
            'crop':'Crop',
            'farmsize':'Farm size (in arces)',
            'location':'Farm Location' ,
            'loc_latitude':'Latitude Co-ordinates',
            'loc_longitude':'Longitude Co-ordinates',
            'farmowner2':'Owner of Farm',
            'crop2':'Crop',
            'farmsize2':'Farm size (in arces)',
            'location2':'Farm Location' ,
            'loc_latitude2':'Latitude Co-ordinates',
            'loc_longitude2':'Longitude Co-ordinates',
            'farmowner3':'Owner of Farm',
            'crop3':'Crop',
            'farmsize3':'Farm size (in arces)',
            'location3':'Farm Location' ,
            'loc_latitude3':'Latitude Co-ordinates',
            'loc_longitude3':'Longitude Co-ordinates',
            'farmowner4':'Owner of Farm',
            'crop4':'Crop',
            'farmsize4':'Farm size (in arces)',
            'location4':'Farm Location' ,
            'loc_latitude4':'Latitude Co-ordinates',
            'loc_longitude4':'Longitude Co-ordinates',
            'farmowner5':'Owner of Farm',
            'crop5':'Crop',
            'farmsize5':'Farm size (in arces)',
            'location5':'Farm Location' ,
            'loc_latitude5':'Latitude Co-ordinates',
            'loc_longitude5':'Longitude Co-ordinates',
            'farmingyears':'Years in Farming',
            'bbf':'Business before farming',
            'baf':'Side Business aside farming',
            'averageyield':'Average Crop Yield',
            'previousyield':'Previous Crop Yield',
            'farmbenefit':'Benefit from  farm',
            'buyerofproduce':'Buyer of produce',
            'numberoftimes':'How often (Do you sell to this buyer)',
            'buyerbenefits':'Benefits from buyer',
            'useoffund':'How will you use your funds if allocated to you?',
            'transactingbank':'Bank Transacting with?',
            'duration':'How Long',
            'partoffarmers':'Do you belong to any farmers Association',
            'declaration':'Declaration',
        }
        widgets={
            'crop': forms.TextInput(attrs={'value':'Cocoa'}),
            'crop2': forms.TextInput(attrs={'value':'Cocoa'}),
            'crop3': forms.TextInput(attrs={'value':'Cocoa'}),
            'crop4': forms.TextInput(attrs={'value':'Cocoa'}),
            'crop5': forms.TextInput(attrs={'value':'Cocoa'}),
        }
    
    
   # def clean_gfxnumber(self):
    #    gfxnumber = self.cleaned_data.get('gfxnumber')
    #    for member in Members.objects.all():
    #        if member.gfxnumber == gfxnumber:
     #           raise forms.ValidationError('There is a member with this id')
     #   return gfxnumber

class StaffCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['staff_id','region', 'district', 'society','access_user','title','firstName','middleName','lastName','day','month','year','id_type','id_number','address','hometown','home_region','telephone','gender','staff_image','position','department','emergency_person','emergency_phone','relationship','emergency_address',]
        labels = {
            'staff_id':'Staff ID',
            'region':'Region', 
            'district':'District', 
            'society':'Society', 
            'access_user':'username',
            'title':'Title',
            'firstName':'First Name',
            'middleName':'Middle Name',
            'lastName':'LastName',
            'day':'Day',
            'month':'Month',
            'year':'Year',
            'id_type':'Type of ID',
            'id_number':'ID Number',
            'address':'Address',
            'hometown':'Hometown',
            'home_region':'Home Region',
            'telephone':'Telephone Number',
            'email':'Email Address',
            'gender':'Gender',
            'staff_image':'Upload an image',
            'position':'Position of Staff',
            'department':'Department of Staff',
            'emergency_person':'Name of Person',
            'emergency_phone':'Contact of emergency person',
            'relationship':'Relation with the person',
            'emergency_address':'Address of person',
        }
        