from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100,null=False)
    regno=models.IntegerField()
    college=models.CharField(max_length=100,null=False)
    branch=models.CharField(max_length=100,null=False)
    city=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

