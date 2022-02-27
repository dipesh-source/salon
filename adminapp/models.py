from django.db import models
from django.contrib.auth.models import User


'''
    will maintain the relationship with data 
    of the date when access expire
'''
class Account_access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.PositiveIntegerField()
    set_date = models.DateField(max_length=100)
    set_time = models.TimeField()
    ex_date = models.DateField(max_length=100)
    ex_time = models.TimeField()
    fdate = models.DateTimeField(auto_now_add=True)

'''
    will update and extend the client account access
'''
class Extend_access(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    month = models.PositiveIntegerField(default=0)
    set_date = models.CharField(max_length=100)
    set_time = models.CharField(max_length=100)
    ex_date = models.CharField(max_length=100)
    ex_time = models.CharField(max_length=100)
    fdate = models.DateTimeField(auto_now_add=True)