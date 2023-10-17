from django.db import models
from datetime import date
from django.contrib.auth.models import User

branches = [
    ('CSE', 'Computer Science Engineering'),
    ('ECE', 'Electronics & Communication Engineering'),
    ('EEE', 'Electronics & Electrical Engineering'),
    ('CE', 'Civil Engineering'),
    ('MEC', 'Mechanical Engineering')
]

semesters = [
    ('sem1', '1'),
    ('sem2', '2'),
    ('sem3', '3'),
    ('sem4', '4'),
    ('sem5', '5'),
    ('sem6', '6'),
    ('sem7', '7'),
    ('sem8', '8')
]

levels = [
    ('dis', 'District'),
    ('state', 'State'),
    ('col', 'College'),
    ('nat', 'National')
]

categories = [
    ('hack', 'Hackathon'),
    ('work', 'Workshop'),
    ('design', 'Designathon'),
    ('sem', 'Seminar'),
    ('course', 'Courses')
]

status = [
    ('app', 'Approved'),
    ('can', 'Cancelled'),
    ('pen', 'Pending')
]


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reg = models.CharField(max_length=10, default=None)
    branch = models.CharField(max_length=100, choices=branches, default=None)
    sem = models.CharField(max_length=5, choices=semesters, default=None)
    img = models.ImageField(upload_to='images/avatar', default=None)

    def __str__(self):
        return self


class Activitylist(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=10, default=None)
    level = models.CharField(max_length=100, choices=levels, default=None)
    img = models.ImageField(upload_to='images/certificate', default=None)
    category = models.CharField(
        max_length=100, choices=categories, default=None)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=100, choices=status, default='pen')

    def __str__(self):
        return self
