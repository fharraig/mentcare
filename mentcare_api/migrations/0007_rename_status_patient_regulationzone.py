# Generated by Django 4.0.2 on 2022-04-29 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare_api', '0006_rename_regulationzone_patient_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='status',
            new_name='RegulationZone',
        ),
    ]