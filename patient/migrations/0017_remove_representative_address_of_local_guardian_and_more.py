# Generated by Django 5.0.6 on 2024-06-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0016_remove_patient_cut_mark_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representative',
            name='Address of Local Guardian',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Address of Person Responsible for Treatment',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Details of ID Proof Recieved',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Name of Local Guardian',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Name of Person Responsible for Treatment',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Phone Number of Local Guardian',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Phone Number of Person Responsible for Treatment',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='Relationship with Patient',
        ),
        migrations.AddField(
            model_name='representative',
            name='address_of_local_guardian',
            field=models.TextField(blank=True, null=True, verbose_name='Address of Local Guardian'),
        ),
        migrations.AddField(
            model_name='representative',
            name='address_of_person_responsible',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address of Person Responsible for Treatment'),
        ),
        migrations.AddField(
            model_name='representative',
            name='detail_of_id_proof_recieved',
            field=models.TextField(blank=True, null=True, verbose_name='Details of ID Proof Recieved'),
        ),
        migrations.AddField(
            model_name='representative',
            name='name_of_local_guardian',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of Local Guardian'),
        ),
        migrations.AddField(
            model_name='representative',
            name='name_of_person_responsible_for_treatment',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of Person Responsible for Treatment'),
        ),
        migrations.AddField(
            model_name='representative',
            name='phone_number_local_guardian',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='Phone Number of Local Guardian'),
        ),
        migrations.AddField(
            model_name='representative',
            name='phone_number_person_responsible',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='Phone Number of Person Responsible for Treatment'),
        ),
        migrations.AddField(
            model_name='representative',
            name='relationship_with_patient',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Relationship with Patient'),
        ),
    ]
