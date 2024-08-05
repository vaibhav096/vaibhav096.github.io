from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    # path('resume/', views.resume, name='resume'),  # Resume page
    # path('projects/', views.projects, name='projects'),  # Projects page
    # path('certifications/', views.certifications, name='certifications'),  # Certifications page
    # path('experience/', views.experience, name='experience'),  # Experience page
]
