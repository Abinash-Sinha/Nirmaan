# Generated by Django 5.0.6 on 2024-06-26 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_declaration'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narcotics_drugs_abuse', models.BooleanField(default=False)),
                ('psychotropic_substance_abuse', models.BooleanField(default=False)),
                ('controlled_substance_abuse', models.BooleanField(default=False)),
                ('alcohol_beyond_permissible_limits', models.BooleanField(default=False)),
                ('behavioural_psychological_condition', models.BooleanField(default=False)),
                ('mental_health_issue', models.BooleanField(default=False)),
                ('guardian_name', models.CharField(max_length=255)),
                ('admission_date', models.DateField()),
                ('monthly_fee_first_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lab_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_fee_second_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_fee_third_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
