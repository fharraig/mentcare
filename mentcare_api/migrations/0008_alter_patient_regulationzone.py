# Generated by Django 4.0.2 on 2022-04-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare_api', '0007_rename_status_patient_regulationzone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='RegulationZone',
            field=models.CharField(blank=True, choices=[('green', 'Green'), ('yellow', 'Yellow'), ('blue', 'Blue'), ('red', 'red')], default='green', max_length=256, null=True),
        ),
    ]
