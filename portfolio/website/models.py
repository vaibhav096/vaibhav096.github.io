from django.db import models

class About(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About (Updated on {self.updated_at})"


# Create your models here.
