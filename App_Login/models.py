from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return str(self.user)


