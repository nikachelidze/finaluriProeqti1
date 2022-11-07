from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
 
class car(models.Model):
    modeli = models.CharField(max_length=255)
    texti = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to="img/")

    def __str__(self):
        return self.modeli

    def image_img(self):
        if self.img:
            return u'< img src="%s" width="100"/>' % self.img.url
        else:
            return '(none)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

class comment(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=25)

    texti = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True)

    