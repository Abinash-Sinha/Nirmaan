# Generated by Django 5.0.6 on 2024-06-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='cut_mark_detail',
            field=models.CharField(default='asdads', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='details_of_id_proof_recieved',
            field=models.TextField(default='asdasd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='email_id',
            field=models.EmailField(default='user@mail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='income_pm',
            field=models.DecimalField(decimal_places=2, default=12222, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='language_spoken',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], default='unmarried', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='occupation',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(default=12334, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='qualification',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='religion',
            field=models.CharField(choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Other', 'Other')], default='Hindu', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='whatsapp_number',
            field=models.IntegerField(default=1233321, max_length=10),
            preserve_default=False,
        ),
    ]