from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def home(request):
    about = About.objects.latest('updated_at')
    return render(request, 'home.html', {'about': about})
