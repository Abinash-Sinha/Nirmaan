from django.db import models

class Patient(models.Model):
	name = models.CharField(name="Name of Patient", max_length=100)
	admission_date = models.DateField(name="Date of Admission", blank=True, null=True)
	release_date = models.DateField(name="Date of Release", blank=True, null=True)
	date_of_birth = models.DateField(name="Date of Birth", blank=True, null=True)
	father_name = models.CharField(name="Name of Father", blank=True, null=True, max_length=100)
	mother_name = models.CharField(name="Name of Mother", blank=True, null=True, max_length=100)
	image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
	occupation = models.CharField(name="Occupation", blank=True, null=True, max_length=100)
	qualification = models.CharField(name="Qualification", blank=True, null=True, max_length=100)
	
	MARRIED = 'Married'
	UNMARRIED = 'Unmarried'
	MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Married'),
        (UNMARRIED, 'Unmarried'),
    ]
	marital_status = models.CharField(name="Marital Status", blank=True, null=True, max_length=50, choices=MARITAL_STATUS_CHOICES)

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

	religion = models.CharField(name="Religion", blank=True, null=True, max_length=100, choices=RELIGION_CHOICES)
	income_pm = models.DecimalField(name="Income Per Month", blank=True, null=True, max_digits=10, decimal_places=2)
	language_spoken = models.CharField(name="Language(s) Spoken", blank=True, null=True, max_length=100)
	phone_number_1 = models.IntegerField(name="Phone Number (1)", blank=True, null=True, max_length=10)
	phone_number_2 = models.IntegerField(name="Phone Number (2)", blank=True, null=True, max_length=10)
	whatsapp_number = models.IntegerField(name="Whatsapp Number", blank=True, null=True, max_length=10)
	email_id = models.EmailField(name="Email Address", blank=True, null=True)
	details_of_id_proof_recieved = models.TextField(name="Details of ID Proof Recieved", blank=True, null=True)
	cut_mark_detail = models.CharField(name="Cut Mark Details", blank=True, null=True, max_length=100)

	CONDITIONS = [
        ('substance_abuse', 'Substance Abuse'),
        ('psychological_disturbance', 'Psychological Disturbance'),
        ('vindictiveness', 'Vindictiveness'),
        ('behavioural_disfunctions', 'Behavioural Disfunction'),
        ('prediagnosed_mental_condition', 'Pre-Diagnosed Mental Health Condition'),
    ]

	substance_abuse = models.BooleanField(default=False)
	psychological_disturbance = models.BooleanField(default=False)
	vindictiveness = models.BooleanField(default=False)
	behavioural_disfunctions = models.BooleanField(default=False)
	prediagnosed_mental_condition = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Representative(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	name_of_local_guardian = models.CharField(name="Name of Local Guardian", blank=True, null=True, max_length=100)
	address_of_local_guardian = models.TextField(name="Address of Local Guardian", blank=True, null=True)
	phone_number_local_guardian = models.IntegerField(name="Phone Number of Local Guardian", blank=True, null=True, max_length=10)
	name_of_person_responsible_for_treatment = models.CharField(name="Name of Person Responsible for Treatment", blank=True, null=True, max_length=100)
	relationship_with_patient = models.CharField(name="Relationship with Patient", blank=True, null=True, max_length=100)
	address__of_person_responsible = models.CharField(name="Address of Person Responsible for Treatment", blank=True, null=True, max_length=100)
	phone_number_person_responsible = models.IntegerField(name="Phone Number of Person Responsible for Treatment", blank=True, null=True, max_length=10)
	detail_of_id_proof_recieved = models.TextField(name="Details of ID Proof Recieved", blank=True, null=True)

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
	verbal_abuse = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Verbal abuse towards other")
	physical_abuse = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Physical abuse towards others")
	breaking_articles = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Breaking articles")
	antisocial_activities = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Involvement in antisocial activities")
	law_suits = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Pending law suit including complaint and grievancelodged under any authority against the patient")
	abnormal_tendencies = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Have you seen any depression, social isolation, self-harm or suicidal tendency within last 30 days in the patient")
	abnormal_romatic_involment = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Any abnormality during intimate romantic involvement")
	high_risk_behavior = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Exposure to high risk behavior")
	unreasonable_anger = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Unreasonable anger outburst")
	irresponsible_aspects = models.CharField(blank=False, null=True, default=None, max_length=10, choices=CHOICES, help_text="Irresponsible toward life and familial aspects")

	def __str__(self) -> str:
		return self.patient.name
	

class MOU(models.Model):
    CONDITIONS = [
        ('narcotics_drugs_abuse', 'Narcotics Drugs Abuse'),
        ('psychotropic_substance_abuse', 'Psychotropic Substance Abuse'),
        ('controlled_substance_abuse', 'Controlled Substance Abuse'),
        ('alcohol_beyond_permissible_limits', 'Alcohol beyond permissible limits'),
        ('behavioural_psychological_condition', 'Associated Underlying Behavioural and Psychological Condition'),
        ('mental_health_issue', 'Pre-Diagnosed Mental Health Issue'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	# Patient Conditions
    narcotics_drugs_abuse = models.BooleanField(default=False)
    psychotropic_substance_abuse = models.BooleanField(default=False)
    controlled_substance_abuse = models.BooleanField(default=False)
    alcohol_beyond_permissible_limits = models.BooleanField(default=False)
    behavioural_psychological_condition = models.BooleanField(default=False)
    mental_health_issue = models.BooleanField(default=False)

    # Fee Information
    monthly_fee_first_month = models.DecimalField(max_digits=10, decimal_places=2)
    lab_charge = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_fee_second_month = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_fee_third_month = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"MOU for Patient: {self.patient.name}"