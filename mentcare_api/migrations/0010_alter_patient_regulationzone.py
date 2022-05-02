# Generated by Django 4.0.2 on 2022-04-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare_api', '0009_alter_patient_regulationzone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='RegulationZone',
            field=models.IntegerField(blank=True, choices=[(0, 'Green'), (1, 'Yellow'), (2, 'Blue'), (3, 'Red')], default=0, null=True),
        ),
    ]