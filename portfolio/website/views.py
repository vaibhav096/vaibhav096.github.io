from django.shortcuts import render
from django.http import HttpResponse
from .models import About,Resume,Project,Certification,Achievement,Education

def home(request):
    about = About.objects.latest('updated_at')
    return render(request, 'home.html', {'about': about})



def resume_view(request):
    resume = Resume.objects.last()
    pdf_url = resume.pdf.url  # Adjust according to your model field
    return render(request, 'resume.html', {'pdf_url': pdf_url})




def projects_view(request):
    projects = Project.objects.all()
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