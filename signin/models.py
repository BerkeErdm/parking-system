from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    #Plaka
    Plaque = models.CharField(max_length=200)
    #Marka
    Brand = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

def __str__(self):
    return self.user.username

@receiver(post_save, sender= User)
def create_user_profile(sender,instance,created, **kwargs):
    if created :
        Profile.objects.create(user=instance)
        instance.profile.save()