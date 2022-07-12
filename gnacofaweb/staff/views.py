from django.shortcuts import render
from members.models import Member
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required(login_url="admin-login")
def staff_base(request):
    return render(request, 'staff/staff-base.html')

def staff_profile(request):
    return render(request, 'views/staff-profile')

def edit_profile(request):
    return render(request, 'views/edit-profile.html')

