from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('admin-login', views.admin_login, name='admin-login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='auth-tenticate/logout.html'), name="logout"),

    path('add-staff/', views.add_staff, name='profile-add'),
    path('edit-staff/en-gh/<str:stfedit>', views.edit_staff, name='staff-edit'),
    path('view-staff/en-gh/<str:stfview>', views.view_staff, name='staff-view'),
    path('delete-staff/en-gh/<str:stfdelete>', views.delete_staff, name='staff-delete'),
    
    path('mem-dash/', views.mem_dash, name='mem-dash'),
    path('mem-csv/', views.member_csv, name='mem-csv'),
    path('add-mem/', views.add_mem, name='mem-add'),
    path('view-mem/<str:pk>/', views.view_mem, name='mem-view'),
    path('edit-mem/<str:edt>', views.edit_mem, name='mem-edit'),
    path('delete-mem/<str:delk>/', views.delete_mem, name='mem-delete'),
    
    path('loan-dash/', views.loan_dash, name='loan-dash'),
    path('add-loan/', views.add_loan, name='loan-add'),
    path('view-loan/', views.view_loan, name='loan-view'),           
    path('delete-loan/', views.delete_loan, name='loan-delete'),
    path('edit-loan/', views.edit_loan, name='loan-edit'),
    
    path('add-dues/', views.add_dues, name='dues-add'),
    path('dues-dash/', views.dues_dash, name='dues-dash'),  
    path('delete-dues/', views.delete_dues, name='dues-delete'),
    path('edit-dues/', views.edit_dues, name='dues-edit'),
    
    
    path('announts-events/', views.announcements_events_page, name='add-announcement'),
    path('messages/', views.messages_page, name='message'),
    path('complaint/', views.complaint_page, name='complaint'),
    path('report-page/', views.report_gen, name='report'),
]
