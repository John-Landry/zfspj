from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return f"Story: {self.tile}"