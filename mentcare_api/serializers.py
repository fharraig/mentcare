from rest_framework import serializers
from .models import Patient
from django.utils import timezone

class PatientSerializer(serializers.ModelSerializer):
    PatientName = serializers.CharField(max_length=256)
    PatientAdmitDate = serializers.DateField()
    PatientReleaseDate = serializers.DateField()
    PatientCondition = serializers.CharField(max_length=256)
    PatientClinician = serializers.CharField(max_length=256)
    PatientStatus = serializers.CharField(max_length=256)

    class Meta:
        model = Patient
        fields = ('__all__')