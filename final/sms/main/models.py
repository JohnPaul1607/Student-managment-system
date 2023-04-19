from django.db import models

# Create your models here.

class Student(models.Model):
    school=models.CharField(max_length=100,null=True)
    Class=models.CharField(max_length=100,null=True)
    section=models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default="Male")
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.IntegerField(default=1234567)
    date_of_birth = models.DateField()
    stu_id = models.CharField(max_length=50)
   

    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField()

    def __str__(self):
        return self.full_name
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    mark = models.IntegerField()