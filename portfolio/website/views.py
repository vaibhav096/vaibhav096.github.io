from django.shortcuts import render
from django.http import HttpResponse
from .models import About,Resume,Project,Certification

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