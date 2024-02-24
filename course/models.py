from django.db import models

# Create your models here.
class course(models.Model):
    course=models.CharField(max_length=250)
    duration=models.CharField(max_length=250,default='no')
    slot=models.CharField(max_length=250,default='no')
    seats=models.IntegerField(default='0')
    
    
    def __str__(self):
       return self.name
class student_details(models.Model):
    fullname=models.CharField(max_length=250,default='no')
    email=models.CharField(max_length=250,default='no')
    duration=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    mobile_no=models.IntegerField(default='0')
    course=models.CharField(max_length=250)
    slot=models.CharField(max_length=250,default='0')
    seats=models.IntegerField(default='0')


 


