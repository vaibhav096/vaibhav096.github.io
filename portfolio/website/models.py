from django.db import models

class About(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About (Updated on {self.updated_at})"
    
class Resume(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    github_link = models.URLField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    course_name = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    verification_link = models.URLField(blank=True, null=True)  # Optional field
    offered_by = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name
    
class Achievement(models.Model):
    description = models.TextField()  # This allows HTML content

    def __str__(self):
        return self.description[:50] 
    
class Education(models.Model):
    education_class = models.CharField(max_length=100)  # General CharField for class
    college_name = models.CharField(max_length=255)
    marks_obtained = models.FloatField()  # Use FloatField for percentages with decimal points

    def __str__(self):
        return f"{self.education_class} from {self.college_name}"


# Create your models here.
