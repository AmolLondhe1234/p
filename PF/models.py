from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class certificate(models.Model):
    cert_name=models.CharField( max_length=100)
    cert_course=models.CharField(max_length=100)
    cert_institute=models.CharField(max_length=100)
    cert_img=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.cert_name
    
    
class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    feedback_text=models.TextField()
    
    def __str__(self):
        return self.name
        
    