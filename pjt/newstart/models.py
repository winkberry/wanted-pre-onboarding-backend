from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    region = models.CharField(max_length=150)

class RecruitmentNotice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=150)
    compensation = models.IntegerField()
    content = models.TextField()
    technologies = models.CharField(max_length=255)

class Applicant(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=150)
    technologies = models.CharField(max_length=255)
    experience = models.IntegerField() #경력