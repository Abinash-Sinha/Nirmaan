# Generated by Django 5.0.6 on 2024-06-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_remove_patient_details_of_id_proof_recieved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representative',
            name='address',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='address_of_local_guardian',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='detail_of_id_proof_recieved',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='name_of_local_guardian',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='name_of_person_responsible_for_treatment',
        ),
        migrations.AddField(
            model_name='representative',
            name='Address of Local Guardian',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Address of Person Responsible for Treatment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Details of ID Proof Recieved',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Name of Local Guardian',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Name of Person Responsible for Treatment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Phone Number of Local Guardian',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Phone Number of Person Responsible for Treatment',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
