from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    p_title = models.CharField(max_length=200)
    p_desc = models.TextField() 
    file = models.FileField(upload_to='files/') 
    tag = models.CharField(max_length=50, default="Others")
    likes= models.ManyToManyField(User,related_name='likes',blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.p_title

    def total_likes(self):
        return self.likes.count()
