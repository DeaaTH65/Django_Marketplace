from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    profile_img = models.ImageField(null=True, blank=True, upload_to='Profile/')
    profile_bio = models.TextField(null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    instagram_link = models.CharField(max_length=100, null=True, blank=True)
    twitter_link = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    

# Create Profile with User Signup
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()        
post_save.connect(create_profile, sender=User)