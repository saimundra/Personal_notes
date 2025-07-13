from django.db import models

# Create your models here.
class Allnotes(models.Model):
    topic = models.CharField(max_length= 255)
    date = models.DateField()
    description = models.CharField(max_length= 1000)
    image = models.ImageField(upload_to='note_images/', blank=True, null=True)

    def __str__(self):
        return self.topic
