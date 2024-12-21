from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import About, Resume, Project, Certification, Achievement, Education

def home(request):
    try:
        about = About.objects.latest('updated_at')
    except ObjectDoesNotExist:
        about = None  # Fallback if no data is available
    return render(request, 'home.html', {'about': about})

def resume_view(request):
    try:
        resume = Resume.objects.last()
        pdf_url = resume.pdf.url if resume else None
    except ObjectDoesNotExist:
        pdf_url = None  # Fallback if no data is available
    return render(request, 'resume.html', {'pdf_url': pdf_url})

def projects_view(request):
    projects = Project.objects.all()  # Empty queryset is fine if no data is present
    return render(request, 'projects.html', {'projects': projects})

def certifications_view(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})

def achievements_view(request):
    achievements = Achievement.objects.all()
    return render(request, 'achievements.html', {'achievements': achievements})

def education_view(request):
    education_records = Education.objects.all()
    return render(request, 'education.html', {'education_records': education_records})
