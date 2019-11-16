from django.db import models
class Student(models.Model):
    increment = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=200)
    dateB = models.DateField()
    desc = models.TextField(max_length=5000)
    zarplata = models.SmallIntegerField()
    slug = models.SlugField(max_length=200, unique=True, default='')
class Rooms(models.Model):
    increment = models.AutoField(primary_key=True, db_index=True)
    number = models.SmallIntegerField()
    desc = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=200, unique=True, default='')