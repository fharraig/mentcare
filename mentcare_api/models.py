from django.db import models
from django.utils import timezone

# Model for patient
class Patient(models.Model):
    PatientName = models.CharField(max_length=256)
    PatientCondition = models.CharField(max_length=256)
    PatientClinician = models.CharField(max_length=256)
    PatientClinicianEmail = models.CharField(max_length=256)
    DateOfLastVisit = models.DateField(default=timezone.now, blank=True, null=True)
    PatientAdmitDate = models.DateField(default=timezone.now)
    PatientReleaseDate = models.DateField(blank=True, null=True)
    CreatedOn = models.DateTimeField(default=timezone.now, help_text='Time is in GMT') # time is in GMT by default
    UpdatedOn = models.DateTimeField(default=timezone.now, null=True, blank=True)
    IsActive = models.IntegerField(default=1, blank=True, null=True, help_text='1->Active, 0->Inactive',
                                   choices=((1, 'Active'), (0, 'Inactive')))

    class Meta:
        verbose_name = 'Patient'

# Model for physician
class Physician(models.Model):
    PhysicianName = models.CharField(max_length=256)
    ListOfPatients = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Physician'

# Model for upcoming appointments
class UpcomingAppointments(models.Model):
    PatientName = models.CharField(max_length=256)
    PhysicianName = models.CharField(max_length=256)
    DateOfAppointment = models.DateField()
    Time = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Upcoming Appointment"

