from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('resume/', views.resume_view, name='resume'),  # Resume page
    path('projects/', views.projects_view, name='projects'),  # Projects page
    path('certifications/', views.certifications_view, name='certifications'),  # Certifications page
    path('achievements/', views.achievements_view, name='achievements'),  # achivements page
    path('education/', views.education_view, name='education'),
]


