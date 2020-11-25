from django.db import models

# Create your models here.
class Carousel(models.Model):
    image_name = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.image_name