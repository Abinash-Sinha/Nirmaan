from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
