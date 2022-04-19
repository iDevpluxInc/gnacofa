from django.urls import path
from . import views

urlpatterns = [    
    path('admin/', views.admin_main, name='admin'),
]