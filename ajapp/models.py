from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90)
    password = models.CharField(max_length=90)
    type = models.CharField(max_length=90)

class department(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()

class course(models.Model):
    depId = models.ForeignKey(department, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    description = models.TextField()

class subject(models.Model):
    depId = models.ForeignKey(department, on_delete=models.CASCADE)
    cid = models.ForeignKey(course, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    description = models.TextField()

class student(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    depId = models.ForeignKey(department, on_delete=models.CASCADE)
    cid = models.ForeignKey(course, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    age = models.IntegerField()

class studentAttendence(models.Model):
    sid = models.ForeignKey(student, on_delete=models.CASCADE)
    attendence = models.IntegerField(null=True, blank=True, default=None)
    date = models.DateField()



