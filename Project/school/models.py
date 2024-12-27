from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    enrolled_date = models.DateField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title
