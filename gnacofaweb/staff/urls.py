
from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_page, name='staff'),
    #path('add-staff/',view.add_staff)
]
