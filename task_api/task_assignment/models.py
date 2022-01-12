from django.db import models
class Task(models.Model):
    Title=models.TextField()
    email=models.EmailField()
    date=models.DateTimeField()
    
    def __str__(self):
        return self.Title
    
