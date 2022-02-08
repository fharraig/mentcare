from django.db import models

# Create your models here.
class Patient(models.Model):
    PatientName = models.CharField(max_length=256)
    PatientAdmitDate = models.DateField()
    PatientReleaseDate = models.DateField()
    PatientCondition = models.CharField(max_length=256)
    PatientClinician = models.CharField(max_length=256)
    PatientStatus = models.CharField(max_length=256)