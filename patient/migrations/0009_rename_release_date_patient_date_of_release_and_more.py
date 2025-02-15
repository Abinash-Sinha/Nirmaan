# Generated by Django 5.0.6 on 2024-06-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_mou'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='release_date',
            new_name='Date of Release',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='Name of Patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admission_date',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='cut_mark_detail',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='income_pm',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='language_spoken',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='whatsapp_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='Cut Mark Details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Date of Admission',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Date of Birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Email Address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Income Per Month',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Language(s) Spoken',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Marital Status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Name of Father',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Name of Mother',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Phone Number (1)',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Phone Number (2)',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Whatsapp Number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='details_of_id_proof_recieved',
            field=models.TextField(blank=True, null=True, verbose_name='Details of ID Proof Recieved'),
        ),
        migrations.AddField(
            model_name='patient',
            name='Occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Religion',
            field=models.CharField(blank=True, choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
