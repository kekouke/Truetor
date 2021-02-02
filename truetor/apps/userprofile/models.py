from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
