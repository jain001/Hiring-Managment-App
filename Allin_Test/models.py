from django.db import models
from django.conf import settings








class Questions(models.Model):
    questions = models.TextField(max_length=1024*2)


    def __str__(self):
        return self.questions



class Solution(models.Model):
    RESULT = (
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    )
    result = models.CharField(max_length=1, choices=RESULT,default ='default')
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True,default ='jainhardik255@gmail.com')
    Full_Name = models.CharField(max_length=50,blank=True)
    Zip_File = models.FileField(upload_to ='candidate/solutions/')
    Video_File = models.FileField(upload_to ='candidate/video_solutions/')

    def __str__(self):
        return self.result






