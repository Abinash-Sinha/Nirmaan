# Generated by Django 5.0.6 on 2024-06-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_rename_release_date_patient_date_of_release_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='details_of_id_proof_recieved',
        ),
        migrations.AddField(
            model_name='patient',
            name='Details of ID Proof Recieved',
            field=models.TextField(blank=True, null=True),
        ),
    ]