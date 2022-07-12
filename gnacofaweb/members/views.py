from django.shortcuts import render
from crm.models import Members

# Create your views here.

#// Member authentication routes //
def member_dashboard(request):
    return render(request, 'members/member_dashboard.html')

def member_login(request):    
    return render(request, 'auth-tenticate/member-login.html')



# // Member Profiles Section //

def member_profile(request):
    member = Members.objects.all()
    context={
        'member': member
    }
    return render(request, 'members/member-profile.html', context)

def member_due(request):
    return render(request, 'members/member_due.html')

def member_loan(request):
    return render(request, 'members/.html')

def make_request(request):
    pass
