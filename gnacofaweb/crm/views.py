from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Members, Profile
from django.contrib.auth.models import User
from .MainForms import MemberCreationForm, StaffCreationForm

#// api class for arkesel sms //
import requests

# import for csv filehandling ///
import csv
from django.http import HttpResponse





# // SMS Classess //
class SMS:
    def _init_(self, api_key,sms_header):
        self.api_key = api_key
        self.sms_header=sms_header
            
    def SEND_ALERT (self, receiver, msg):
        try:
            _url = "https://sms.arkesel.com/api/v2/sms/send"
            _payload={ 
                        "sender": self.sms_header, 
                        "message": str (msg), 
                        "recipients": receiver,
                    }
            _headers = {'api-key':self.api_key,'Content-Type': 'application/json'}
                
            response = requests.request('POST', _url, headers=_headers, data=json.dumps(_payload))
            print("The responds: ", (response.text))
        except requests.exceptions.RequestException as e:
            print("Error sending sms:", SystemExit (e))
            


#// Main Views code //

# // authentication viewss ////
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            return redirect('admin-login')
    return render(request, 'auth-tenticate/admin-login.html')

# // STAFF -- AREA -- //
def staff_csv(request):
    files = HttpResponse(content_type = 'text/csv')
    files['Content-Disposition'] = 'attachement; filename = membersRecords.csv'
    
    writer = csv.writer(files)
    
    member = Members.objects.all()
    
    writer.writerow(['GFXNumber','Region','District','Society','Title','FirstName','MiddleName','LastName','PreferredName','Day','Month','Year','Gender','Hometown','Address','Level_of_Education','Type_of_ID','ID_Number','PhoneNumber','Marital_Status','SpouseName','SpouseOccupation','SpouseNumber','Next_of_kins_Name','Relationship','Next_of_kins_Phone','Number_of_Partners','Number_of_Farms','farm_one_owner','form_one_crop','farm_one_farm_size','farm_one_farm_location','farm_one_latitude','farm_one_longitude','farm_two_owner','form_two_crop','farm_two_farm_size','farm_two_farm_location','farm_two_latitude','farm_two_longitude','farm_three_owner','form_three_crop','farm_three_farm_size','farm_three_farm_location','farm_three_latitude','farm_three_longitude','farm_four_owner','form_four_crop','farm_four_farm_size','farm_four_farm_location','farm_four_latitude','farm_four_longitude','farm_five_owner','form_five_crop','farm_five_farm_size','farm_five_farm_location','farm_five_latitude','farm_five_longitude','Years_in_Farming','Business_before_Farming','side_Business_aside_farming','Average_crop_yield','Previous_crop_yield','benefit_from_farm','buyer_of_produce','how_often','benefits_from_buyer','Usage_of_fund','Bank_transacting','howLong','part_of_association','Declaration','Date_created'])
    
    for member in member:
        writer.writerow([member.gfxnumber, member.region, member.district, member.society,member.title, member.firstname,member.middlename,member.lastname,member.preferredname,member.day,member.month,member.year,member.gender,member.hometown,member.address,member.education,member.idtype,member.idnum,member.phone,member.marriage,member.spousename,member.spouseoccupation,member.spousenumber,member.kinsname,member.kinsrelationship,member.kinsnumber,member.familysize,member.farmnumber,member.farmowner,member.crop,member.farmsize,member.location,member.loc_latitude,member.loc_longitude,member.farmowner2,member.crop2,member.farmsize2,member.location2,member.loc_latitude2,member.loc_longitude2,member.farmowner3,member.crop3,member.farmsize3,member.location3,member.loc_latitude3,member.loc_longitude3,member.farmowner4,member.crop4,member.farmsize4,member.location4,member.loc_latitude4,member.loc_longitude4,member.farmowner5,member.crop5,member.farmsize5,member.location5,member.loc_latitude5,member.loc_longitude5,member.farmingyears,member.bbf,member.baf,member.averageyield,member.previousyield,member.farmbenefit,member.buyerofproduce,member.numberoftimes,member.buyerbenefits,member.useoffund,member.transactingbank,member.duration,member.partoffarmers,member.declaration,member.date_created])
    return files

@login_required(login_url="admin-login")
def add_staff(request): 
    if request.method =='POST': 
        form = StaffCreationForm(request.POST, request.FILES)
        staff_id = form
        if form.is_valid():
            profile = Profile.objects.filter(staff_id=staff_id)
            if profile:
                messages.error(request, f'staff_id is already in the database or is entered') 
            else:
                form.save()
                messages.success(request, f'Staff Profile successfully added')
                return redirect('staff')
    else:
        form = StaffCreationForm
        
    context = {
        'form':form,
    }   
    return render(request, 'staffs/add_staff.html', context)

@login_required(login_url="admin-login")
def edit_staff(request, stfedit):
    profile = Profile.objects.get(staff_id = stfedit)
    if request.method == 'POST':
        form = StaffCreationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = StaffCreationForm(instance=profile)   
    context = {
        'profile':profile,
        'form':form
    }     
    return render(request, 'staffs/edit_staff.html', context)

@login_required(login_url="admin-login")
def view_staff(request, stfview): 
    profile = Profile.objects.get(staff_id = stfview)   
    context = {
        'profile':profile,
    }
    return render(request, 'staffs/view_staff.html', context)

@login_required(login_url="admin-login")
def delete_staff(request, stfdelete):
    profile = Profile.objects.get(staff_id = stfdelete)
    if request.method == 'POST':
        profile.delete()
        return redirect('staff')
    context = {
        'profile':profile,
    }     
    return render(request, 'staffs/delete_staff.html', context)



# /// MEMBERS ///
"""***************  for members ***************"""
def member_csv(request):
    files = HttpResponse(content_type = 'text/csv')
    files['Content-Disposition'] = 'attachement; filename = membersRecords.csv'
    
    writer = csv.writer(files)
    
    member = Members.objects.all()
    
    writer.writerow(['GFXNumber','Region','District','Society','Title','FirstName','MiddleName','LastName','PreferredName','Day','Month','Year','Gender','Hometown','Address','Level_of_Education','Type_of_ID','ID_Number','PhoneNumber','Marital_Status','SpouseName','SpouseOccupation','SpouseNumber','Next_of_kins_Name','Relationship','Next_of_kins_Phone','Number_of_Partners','Number_of_Farms','farm_one_owner','form_one_crop','farm_one_farm_size','farm_one_farm_location','farm_one_latitude','farm_one_longitude','farm_two_owner','form_two_crop','farm_two_farm_size','farm_two_farm_location','farm_two_latitude','farm_two_longitude','farm_three_owner','form_three_crop','farm_three_farm_size','farm_three_farm_location','farm_three_latitude','farm_three_longitude','farm_four_owner','form_four_crop','farm_four_farm_size','farm_four_farm_location','farm_four_latitude','farm_four_longitude','farm_five_owner','form_five_crop','farm_five_farm_size','farm_five_farm_location','farm_five_latitude','farm_five_longitude','Years_in_Farming','Business_before_Farming','side_Business_aside_farming','Average_crop_yield','Previous_crop_yield','benefit_from_farm','buyer_of_produce','how_often','benefits_from_buyer','Usage_of_fund','Bank_transacting','howLong','part_of_association','Declaration','Date_created'])
    
    for member in member:
        writer.writerow([member.gfxnumber, member.region, member.district, member.society,member.title, member.firstname,member.middlename,member.lastname,member.preferredname,member.day,member.month,member.year,member.gender,member.hometown,member.address,member.education,member.idtype,member.idnum,member.phone,member.marriage,member.spousename,member.spouseoccupation,member.spousenumber,member.kinsname,member.kinsrelationship,member.kinsnumber,member.familysize,member.farmnumber,member.farmowner,member.crop,member.farmsize,member.location,member.loc_latitude,member.loc_longitude,member.farmowner2,member.crop2,member.farmsize2,member.location2,member.loc_latitude2,member.loc_longitude2,member.farmowner3,member.crop3,member.farmsize3,member.location3,member.loc_latitude3,member.loc_longitude3,member.farmowner4,member.crop4,member.farmsize4,member.location4,member.loc_latitude4,member.loc_longitude4,member.farmowner5,member.crop5,member.farmsize5,member.location5,member.loc_latitude5,member.loc_longitude5,member.farmingyears,member.bbf,member.baf,member.averageyield,member.previousyield,member.farmbenefit,member.buyerofproduce,member.numberoftimes,member.buyerbenefits,member.useoffund,member.transactingbank,member.duration,member.partoffarmers,member.declaration,member.date_created])
    return files

@login_required(login_url="admin-login")
def add_mem(request):
    
    if request.method =='POST': 
        form = MemberCreationForm(request.POST, request.FILES)
        gfxnumber = form
        if form.is_valid():
            member = Members.objects.filter(gfxnumber=gfxnumber)
            if member:
                messages.error(request, f'Member is already in the database or is entered') 
            else:
                form.save()
                messages.success(request, f'Member added successfully!!!!')
                return redirect('mem-add')
    else:
        form = MemberCreationForm
    context = {
        'form':form,
    }
    return render(request, 'mempages/add_mem.html', context)

@login_required(login_url="admin-login")
def view_mem(request, pk):
    member = Members.objects.get(gfxnumber = pk) 
    context = {
        'member':member
    }  
    return render(request, 'mempages/view-mem.html', context)

@login_required(login_url="admin-login")
def edit_mem(request, edt):
    member = Members.objects.get(gfxnumber = edt)
    if request.method == 'POST':
        form = MemberCreationForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('admin-member-dash')
    else:
        form = MemberCreationForm(instance=member)
        
    context = {
        'member':member,
        'form':form,
    }     
    return render(request, 'mempages/edit-mem.html', context)

@login_required(login_url="admin-login")
def delete_mem(request, delk):
    member = Members.objects.get(gfxnumber = delk) 
    if request.method == 'POST':
        member.delete()
        return redirect('admin-member-dash')    
    return render(request, 'mempages/delete-mem.html')

@login_required(login_url="admin-login")
def mem_dash(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        member = Members.objects.filter(gfxnumber__contains = searched) 
        return render(request, 'mempages/mem-dash.html',{'searched':searched, 'member': member})
    
    else:
        member = Members.objects.all()  
        context = {
            'member': member, 
        } 
        return render(request, 'mempages/mem-dash.html', context)












"""***************  for loan ***************"""
@login_required(login_url="admin-login")
def loan_dash(request):    
    return render(request, 'mempages/loan-dash.html')


@login_required(login_url="admin-login")
def add_loan(request):    
    return render(request, 'mempages/add-loan.html')

@login_required(login_url="admin-login")
def view_loan(request):    
    return render(request, 'mempages/view-loan.html')
    """*************** for admin ***************"""

@login_required(login_url="admin-login")
def delete_loan(request):    
    return render(request, 'mempages/delete-loan.html')

@login_required(login_url="admin-login")
def edit_loan(request):    
    return render(request, 'mempages/edit-loan.html')



"""***************  for Dues ***************"""
@login_required(login_url="admin-login")
def dues_dash(request):    
    return render(request, 'dues/dues-dash.html')


@login_required(login_url="admin-login")
def add_dues(request):    
    return render(request, 'dues/add-dues.html')

@login_required(login_url="admin-login")
def view_dues(request):    
    return render(request, 'dues/view-dues.html')
    """*************** for admin ***************"""

@login_required(login_url="admin-login")
def edit_dues(request):    
    return render(request, 'dues/edit-dues.html')

@login_required(login_url="admin-login")
def delete_dues(request):    
    return render(request, 'dues/delete-dues.html')

@login_required(login_url="admin-login")
def announcements_events_page(request):
    return render(request, 'views-pages/announcement-events.html')

@login_required(login_url="admin-login")
def messages_page(request):
    return render(request, 'views-pages/message.html')


@login_required(login_url="admin-login")
def complaint_page(request):
    return render(request, 'views-pages/complaint_page.html')


@login_required(login_url="admin-login")
def report_gen(request):
    return render(request, 'views-pages/report_gen.html')