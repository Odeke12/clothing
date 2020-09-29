from django.db.models.signals import post_save
from django.contrib.auth.models import User #act as the sender sending the signal
from django.dispatch import receiver #receiver gets the signal and performs tasks
from .models import Profile

@receiver(post_save, sender=User) #post_save is the signal with user as the sender, the receiver is create_profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()   
        
