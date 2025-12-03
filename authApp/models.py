from django.db import models

# Create your models here.
class Mountain(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)

    # 
    def __str__(self):
        return self.name
        



