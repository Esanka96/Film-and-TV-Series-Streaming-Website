from django.db import models
import os
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
   name=models.CharField(max_length=200)

   def __str__(self):
      return self.name

class List(models.Model):
   name=models.CharField(max_length=50)

   def __str__(self):
      return self.name
   
class Actor(models.Model):
  name=models.CharField( max_length=50)

  def __str__(self):
     return self.name
  
class Filmname(models.Model):
   name=models.CharField(max_length=200)

   def __str__(self):
      return self.name

class Filmphoto(models.Model):
   photo=models.ImageField(upload_to='',blank=True, null=True,max_length=500)

class postTable(models.Model):
  name=models.CharField(max_length=200)
  date=models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  photo=models.ImageField(upload_to='', blank=True,null=True,max_length=500)
  item=models.ManyToManyField(List)
  persons=models.ManyToManyField(Person)
  actros=models.ManyToManyField(Actor)
  filmnames=models.ManyToManyField(Filmname)
  filmphotos=models.ManyToManyField(Filmphoto)

  def __str__(self):
    return self.name
  
  def delete(self, *args, **kwargs):
    if self.photo:
        photo_path = self.photo.path
        if os.path.exists(photo_path):
            os.remove(photo_path)
    super().delete(*args, **kwargs)

class TVtable(models.Model):
   name=models.CharField(max_length=200)
   date=models.CharField(max_length=200)
   photo=models.ImageField(upload_to='',blank=True,null=True,max_length=500)

   def __str__(self):
      return self.name
   
class Registerform(AbstractUser):
   First_name=models.CharField(max_length=50)
   Last_name=models.CharField(max_length=50)
   Email=models.CharField(max_length=100,unique=True)
   Password=models.CharField(max_length=50)
   username=None

   USERNAME_FIELD='Email'
   REQUIRED_FIELDS=[]

   def __str__(self):
      return self.Firstname