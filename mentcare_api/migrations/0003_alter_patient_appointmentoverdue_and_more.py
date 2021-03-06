# Generated by Django 4.0.2 on 2022-03-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare_api', '0002_patient_appointmentoverdue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='AppointmentOverdue',
            field=models.IntegerField(blank=True, choices=[(1, 'Overdue'), (0, 'Fine')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='IsActive',
            field=models.IntegerField(blank=True, choices=[(1, 'Admitted'), (0, 'Released')], default=1, null=True),
        ),
    ]
