from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    def save(self,commit = False):
        if self.age<18:
            raise Exception
        else:
            super().save()


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    like = models.ManyToManyField(Person)


class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/post/image',default='')