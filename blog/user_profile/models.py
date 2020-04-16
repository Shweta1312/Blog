from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # GENDER_CHOICES=(
    #     ('M','Male'),
    #     ('F','Female'),
    # )
    user_name=models.ForeignKey(User,  on_delete=models.CASCADE)
    bio=models.TextField()
    interests=models.TextField()
    phone=models.CharField('Contact Phone', max_length=20)
    # gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    age=models.IntegerField()
    image = models.FileField(upload_to='myfiles/', null=True, blank=True) 
    user_created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name.username