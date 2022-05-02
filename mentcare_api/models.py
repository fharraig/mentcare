from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# Model for patient
class Patient(models.Model):
    PatientName = models.CharField(max_length=256)
    PatientCondition = models.CharField(max_length=256)
    PatientClinician = models.CharField(max_length=256)
    PatientClinicianEmail = models.CharField(max_length=256)
    DateOfLastVisit = models.DateField(default=timezone.now, blank=True, null=True)
    PatientAdmitDate = models.DateField(default=timezone.now)
    PatientReleaseDate = models.DateField(blank=True, null=True)
    CreatedOn = models.DateTimeField(default=timezone.now, help_text='Time is in GMT')  # time is in GMT by default
    UpdatedOn = models.DateTimeField(default=timezone.now, null=True, blank=True)
    IsActive = models.IntegerField(default=1, blank=True, null=True, choices=((1, 'Admitted'), (0, 'Released')))
    AppointmentOverdue = models.IntegerField(default=0, blank=True, null=True, choices=((1, 'Overdue'), (0, 'Fine')))
    RegulationZone = models.IntegerField(default=0, blank=True, null=True, choices=((0, 'Green'), (1, 'Yellow'),
                                                                                                 (2, 'Blue'), (3, 'Red')))

    class Meta:
        verbose_name = 'Patient'


# Model for physician
class Physician(models.Model):
    PhysicianName = models.CharField(max_length=256)
    PhysicianEmail = models.CharField(max_length=256, default="doctor@hospital.com", blank=True, null=True)
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
