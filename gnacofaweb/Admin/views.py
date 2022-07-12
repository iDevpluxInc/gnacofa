import email
from enum import unique
from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crm.models import Members, Profile
from crm.MainForms import UserCreateForm


# Create your views here.
#from email import message
#from email.message import Message



# Create your views here.

@login_required(login_url="admin-login")
def staff_page(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        profile = Profile.objects.filter(staff_id__contains = searched)
        return render(request, 'user/staff_page.html',{'searched':searched, 'profile':profile})
    else:
        profile = Profile.objects.all()
        return render(request, 'user/staff_page.html', {'profile':profile})

@login_required(login_url="admin-login")
def users(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-add')
    else:
       form = UserCreateForm     
    context = {'form':form}
    return render(request, 'user/user.html', context)

@login_required(login_url="admin-login")
def member_dash(request):
    if request.method =='POST':
        search = request.POST['search']
        member = Members.objects.filter(gfxnumber = search)
        return render(request, 'member-page/admin-mem-dash.html', {'member':member, 'search':search})
    else:
        member = Members.objects.all()
        return render(request, 'member-page/admin-mem-dash.html', {'member':member})   
    
@login_required(login_url="admin-login")
def admin_main(request):
    member = Members.objects.all()
    member_all_count = member.count()
    profile_count = Profile.objects.all().count()
    
    context = {'member': member, 'member_all_count':member_all_count, 'staff_count':profile_count}
    return render(request, 'main/admin-dashboard.html', context)

