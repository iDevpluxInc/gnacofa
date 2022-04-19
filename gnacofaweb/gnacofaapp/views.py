from django.shortcuts import render
from .models import Event


# Create your views here.

def home(request):
    eve = {
        'events': Event.objects.all()
    }
    
    Event.objects.order_by('-date_posted')
    return render(request, 'home.html', eve)

def about(request):
    return render(request, 'views-pages/about-us.html')

def management(request):
    return render(request, 'views-pages/our-management.html')

def structure(request):
    return render(request, 'views-pages/our-structure.html')

def archieves(request):
    return render(request, 'views-pages/archieves.html')

def projects(request):
    return render(request, 'views-pages/projects.html')

def news(request):
    return render(request, 'views-pages/news.html')

def events(request):
    return render(request, 'views-pages/events.html')

def photos(request):
    return render(request, 'views-pages/gnacofa-gal.html')

def contact(request):
    return render(request, 'views-pages/contact-us.html')

def faqs(request):
    return render(request, 'views-pages/faqs.html')

def covid(request):
    return render(request, 'views-pages/covid.html')
