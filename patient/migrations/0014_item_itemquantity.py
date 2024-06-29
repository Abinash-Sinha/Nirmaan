# Generated by Django 5.0.6 on 2024-06-27 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_remove_mou_admission_date_remove_mou_guardian_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ItemQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.item')),
            ],
        ),
    ]