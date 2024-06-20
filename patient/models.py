from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length=100)
	admission_date = models.DateField()
	release_date = models.DateField(blank=True, null=True)
	date_of_birth = models.DateField()
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
	occupation = models.CharField(max_length=100)
	qualification = models.CharField(max_length=100)
	
	MARRIED = 'Married'
	UNMARRIED = 'Unmarried'
	MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Married'),
        (UNMARRIED, 'Unmarried'),
    ]
	marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)

	HINDU = 'Hindu'
	MUSLIM = 'Muslim'
	CHRISTIAN = 'Christian'
	OTHER = 'Other'
	RELIGION_CHOICES = [
		(HINDU, 'Hindu'),
		(MUSLIM, 'Muslim'),
		(CHRISTIAN, 'Christian'),
		(OTHER, 'Other'),
	]

	religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)
	income_pm = models.DecimalField(max_digits=10, decimal_places=2)
	language_spoken = models.CharField(max_length=100)
	phone_number = models.IntegerField(max_length=10)
	whatsapp_number = models.IntegerField(max_length=10)
	email_id = models.EmailField()
	details_of_id_proof_recieved = models.TextField()
	cut_mark_detail = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Representative(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)
	address = models.TextField()
	name_of_local_guardian = models.CharField(max_length=100)
	address_of_local_guardian = models.TextField()
	name_of_person_responsible_for_treatment = models.CharField(max_length=100)
	address_2 = models.CharField(max_length=100)
	# guardian_photo = models.ImageField(upload_to='representative_images/',blank=True, null=True)
	# local_guardian_photo = models.ImageField()
	detail_of_id_proof_recieved = models.TextField()

	def __str__(self) -> str:
		return self.patient.name

class Declaration(models.Model):
	YES = 'Yes'
	NO = 'No'
	NOT_SURE = 'Not Sure'
	CHOICES = [
		(YES, 'Yes'),
		(NO, 'No'),
		(NOT_SURE, 'Not Sure'),
	]
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	verbal_abuse = models.CharField(max_length=10, choices=CHOICES, help_text="Verbal abuse towards other")
	physical_abuse = models.CharField(max_length=10, choices=CHOICES, help_text="Physical abuse towards others")
	breaking_articles = models.CharField(max_length=10, choices=CHOICES, help_text="Breaking articles")
	antisocial_activities = models.CharField(max_length=10, choices=CHOICES, help_text="Involvement in antisocial activities")
	law_suits = models.CharField(max_length=10, choices=CHOICES, help_text="Pending law suit including complaint and grievancelodged under any authority against the patient")
	abnormal_tendencies = models.CharField(max_length=10, choices=CHOICES, help_text="Have you seen any depression, social isolation, self-harm or suicidal tendency within last 30 days in the patient")
	abnormal_romatic_involment = models.CharField(max_length=10, choices=CHOICES, help_text="Any abnormality during intimate romantic involvement")
	high_risk_behavior = models.CharField(max_length=10, choices=CHOICES, help_text="Exposure to high risk behavior")
	unreasonable_anger = models.CharField(max_length=10, choices=CHOICES, help_text="Unreasonable anger outburst")
	irresponsible_aspects = models.CharField(max_length=10, choices=CHOICES, help_text="Irresponsible toward life and familial aspects")

	def __str__(self) -> str:
		return self.patient.name