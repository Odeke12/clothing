from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade means if the user is deleted, then his profile is deleted but if we deleted the profile, we dont delete the user
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):  
        return f'{self.user.username} Profile'  
    
    def save(self, *args, **kwargs):#already exists in the parent class
        super().save(*args, **kwargs)
          
        img = Image.open(self.image.path)
         
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) #resizes the image
            img.save(self.image.path) 
