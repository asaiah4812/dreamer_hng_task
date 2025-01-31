from django.db import models

# Create your models here.

class Dreamer(models.Model):
    email = models.CharField(max_length=100)
    current_datetime = models.DateTimeField(auto_now_add=True)
    github_url =models.URLField(max_length=100)
    
    def __str__(self):
        return self.email