import email
from enum import unique
from turtle import title
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Staff
from members.models import Member


# Create your views here.
#from email import message
#from email.message import Message



# Create your views here.
def dues(request):
    return render(request, 'dues/dues.html')

def add_dues(request):
    return render(request, 'dues/add_dues.html')

def staff_page(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        staff = Staff.objects.filter(staff_id__contains = searched)
        return render(request, 'staffs-page/staff_page.html',{'searched':searched, 'staff':staff})
    else:
        staff = Staff.objects.all()
        return render(request, 'staffs-page/staff_page.html', {'staff':staff})

def show_staff(request, staffs):
    staffy= Staff.objects.get(pk=staffs)
    return render(request, 'staffs-page/show_staff.html', {'staffy':staffy})

def add_staff(request):
    if request.method =='POST':
        title = request.POST['title']
        staff_id = request.POST['staff_id']
        firstName = request.POST['f_name']
        middleName = request.POST['m_name']
        lastName = request.POST['l_name']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        address = request.POST['address']
        telephone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        id_type = request.POST['id_type']
        id_number = request.POST['id_number']
        staff_image = request.FILES['image']
        position = request.POST['position']
        department = request.POST['department']
        emergency_person = request.POST['emergencyperson']
        emergency_phone = request.POST['emergencycontact']
        emergency_address = request.POST['emergencyaddress']
        relationship = request.POST['relation']
        
        staffs = Staff.objects.filter(staff_id = staff_id)
        if staffs:
            messages.error(request, f'This Staff already exist')
        elif staffs == '':
            messages.error(request, f'This Staff ID is required please input')
        else:
            new_staff = Staff(title = title, staff_id = staff_id, firstName = firstName, middleName = middleName, lastName = lastName, day = day, month = month, year = year, telephone = telephone, email = email, password = password, gender = gender, address = address, id_type = id_type, id_number = id_number, staff_image = staff_image, position = position, department = department, emergency_person = emergency_person, emergency_phone = emergency_phone, emergency_address = emergency_address, relationship = relationship)
            
            messages.success(request, f'form is submitted successfully')
            new_staff.save()
    return render(request, 'staffs-page/add_staff.html')

def edit_view(request, member_id):
    member = Member.objects.get(pk = member_id)
    return render(request, 'member-page/edit_view_member.html', {'member':member})

def member_view(request):
    if request.method =='POST':
        search = request.POST['search']
        member = Member.objects.filter(member_gfx = search)
        return render(request, 'member-page/member_tree_view.html', {'search':search, 'member':member})
    else:
        member = Member.objects.all()
        return render(request, 'member-page/member_tree_view.html', {'member':member})
    
    
def adlogin(request):
    if request.method == 'POST':
        gfx = request.POST['gfxnum']
        passwd = request.POST['passwd']
        exec = ExecutiveMembers.objects.all()
        if exec:
            return redirect('administrator/')
        else:
            messages.error(request, f'Invalid credentials entered')      
    return render(request, 'auth-en/adlogin.html')


#@login_required(login_url="admin_login")
def admin_main(request):
    return render(request, 'main/admin-main.html')

