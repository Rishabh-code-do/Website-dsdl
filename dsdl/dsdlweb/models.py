from django.db import models

# Create your models here.

class Coordinators(models.Model):
    
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    insta_url=models.URLField(max_length=200,null=True,blank=True)
    linked_in_url=models.URLField(max_length=200,null=True,blank=True)