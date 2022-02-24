from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    PatientName = models.CharField(max_length=256)
    PatientAdmitDate = models.DateField()
    PatientReleaseDate = models.DateField()
    PatientCondition = models.CharField(max_length=256)
    PatientClinician = models.CharField(max_length=256)
    PatientStatus = models.CharField(max_length=256)
    CreatedOn = models.DateTimeField(default=timezone.now)
    UpdatedOn = models.DateTimeField(default=timezone.now, null=True, blank=True)
    IsActive = models.IntegerField(default=1, blank=True, null=True, help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')))

    class Meta:
        # Add verbose name
        verbose_name = 'Patient'
