# Generated by Django 4.0.2 on 2022-04-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare_api', '0003_alter_patient_appointmentoverdue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='PhysicianEmail',
            field=models.CharField(blank=True, default='doctor@hospital.com', max_length=256, null=True),
        ),
    ]