from django.db import models

class Feedentry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    
    
    def __str__(self):
        return self.name
    
