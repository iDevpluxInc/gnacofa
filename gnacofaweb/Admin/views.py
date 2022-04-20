from django.shortcuts import render

# Create your views here.
from email import message
from email.message import Message
from django.shortcuts import render
from django.contrib import messages


# Create your views here.


def admin_main(request):
    return render(request, 'main/admin-main.html')
