from django.db import models
from django.contrib.auth.models import User
from django import forms

class CompanyProfile(models.Model):
    company = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    
 

    def __str__(self):
        return f'{self.company_name} Profile'

