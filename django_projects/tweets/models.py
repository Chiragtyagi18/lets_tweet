from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"