from django.urls import path
from . import views

urlpatterns = [    
    path('administrator/', views.admin_main, name='administrator'),
    path('adminlogin/', views.adlogin, name='admin_login'),
    path("dues/", views.dues, name="dues"),
    path("add-dues/", views.add_dues, name="add-dues"),
    path("staff-page/", views.staff_page, name="staff"),
    path("show-staff/<staffs>", views.show_staff, name="show-id"),
    path("add-staff/", views.add_staff, name="add-staff"),
    path("edit-view/<member_id>", views.edit_view, name="edit-view"),
    path("member-view/", views.member_view, name="member-view"),
]