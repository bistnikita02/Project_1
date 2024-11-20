from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    skill = models.ManyToManyField(Skill)


    def __str__(self):
        return f'{self.user.username} Profile'

    def get_skill_list(self):
        data=list(self.skill.values_list('name',flat=True))
        return data

