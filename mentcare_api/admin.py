from django.contrib import admin
from .models import Patient, Physician, UpcomingAppointments
from django.contrib import messages

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('PatientName', 'PatientClinician', 'PatientCondition', 'DateOfLastVisit', 'PatientAdmitDate', 'IsActive')

    def active(self, obj):
        return obj.IsActive == 1

    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(IsActive=1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(IsActive=0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully!")

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")


class PhysicianAdmin(admin.ModelAdmin):
    list_display = ('PhysicianName', 'ListOfPatients')


class UpcomingAppointmentsAdmin(admin.ModelAdmin):
    list_display = ('PatientName', 'PhysicianName', 'DateOfAppointment', 'Time')


admin.site.register(Patient, PatientAdmin)
admin.site.register(Physician, PhysicianAdmin)
admin.site.register(UpcomingAppointments, UpcomingAppointmentsAdmin)