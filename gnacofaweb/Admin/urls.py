from django.urls import path
from . import views

urlpatterns = [    
    path('administrator/', views.admin_main, name='admin-dashboard'),
    path("staff-page/", views.staff_page, name="staff"),
    path("admin/addusers/", views.users, name="users"),
    path("member-dash/", views.member_dash, name="admin-member-dash"),
]