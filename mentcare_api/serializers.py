from rest_framework import serializers
from .models import Patient, Physician, UpcomingAppointments


class PatientSerializer(serializers.ModelSerializer):
    PatientName = serializers.CharField(max_length=256)
    PatientAdmitDate = serializers.DateField()
    PatientCondition = serializers.CharField(max_length=256)
    PatientClinician = serializers.CharField(max_length=256)
    PatientClinicianEmail = serializers.CharField(max_length=256)

    class Meta:
        model = Patient
        fields = '__all__'


class PhysicianSerializer(serializers.ModelSerializer):
    PhysicianName = serializers.CharField(max_length=256)
    ListOfPatients = serializers.CharField(max_length=256)

    class Meta:
        model = Physician
        fields = '__all__'


class UpcomingAppointmentsSerializer(serializers.ModelSerializer):
    PatientName = serializers.CharField(max_length=256)
    PhysicianName = serializers.CharField(max_length=256)
    DateOfAppointment = serializers.DateField()
    Time = serializers.CharField(max_length=256)

    class Meta:
        model = UpcomingAppointments
        fields = '__all__'

