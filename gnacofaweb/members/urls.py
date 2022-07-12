from re import template
from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('member-dashboard/en-GH/', views.member_dashboard, name='member-dashboard'),
    #path('member-login/en-GH/', views.member_login, name='member-login'),
    path('member-profile/en-GH/', views.member_profile, name='member-profile'),
    #path('member-due/en-GH/', views.member_due, name='member-due'),
    #path('member-loan/en-GH', views.member_loan, name='member-loan'),
    #path('make-request/en-GH/', views.make_request, name='make-request'),
    
]
