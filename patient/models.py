from django.db import models
import datetime

class Patient(models.Model):	
	uuid = models.CharField(max_length=10, blank=True, null=True)
	name = models.CharField(name='name', verbose_name="Name of Patient", max_length=100)
	admission_date = models.DateField(name='admission_date', verbose_name="Date of Admission", blank=True, null=True)
	release_date = models.DateField(name='release_date', verbose_name="Date of Release", blank=True, null=True)
	date_of_birth = models.DateField(name='date_of_birth', verbose_name="Date of Birth", blank=True, null=True)
	father_name = models.CharField(name='father_name', verbose_name="Name of Father", blank=True, null=True, max_length=100)
	mother_name = models.CharField(name='mother_name', verbose_name="Name of Mother", blank=True, null=True, max_length=100)
	image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
	occupation = models.CharField(name='occupation', verbose_name="Occupation", blank=True, null=True, max_length=100)
	qualification = models.CharField(name='qualification', verbose_name="Qualification", blank=True, null=True, max_length=100)
	
	MARRIED = 'Married'
	UNMARRIED = 'Unmarried'
	MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Married'),
        (UNMARRIED, 'Unmarried'),
    ]
	marital_status = models.CharField(name='marital_status', verbose_name="Marital Status", blank=True, null=True, max_length=50, choices=MARITAL_STATUS_CHOICES)

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

	religion = models.CharField(name='religion', verbose_name="Religion", blank=True, null=True, max_length=100, choices=RELIGION_CHOICES)
	income_pm = models.DecimalField(name='income_pm', verbose_name="Income Per Month", blank=True, null=True, max_digits=10, decimal_places=2)
	language_spoken = models.CharField(name='language_spoken', verbose_name="Language(s) Spoken", blank=True, null=True, max_length=100)
	phone_number_1 = models.IntegerField(name='phone_number_1', verbose_name="Phone Number (1)", blank=True, null=True, max_length=10)
	phone_number_2 = models.IntegerField(name='phone_number_2', verbose_name="Phone Number (2)", blank=True, null=True, max_length=10)
	whatsapp_number = models.IntegerField(name='whatsapp_number', verbose_name="Whatsapp Number", blank=True, null=True, max_length=10)
	email_id = models.EmailField(name='email_id', verbose_name="Email Address", blank=True, null=True)
	details_of_id_proof_recieved = models.TextField(name='details_of_id_proof_recieved', verbose_name="Details of ID Proof Recieved", blank=True, null=True)
	cut_mark_detail = models.CharField(name="cut_mark_detail", verbose_name="Cut Mark Details", blank=True, null=True, max_length=100)

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

	def save(self, *args, **kwargs):
		super(Patient, self).save(*args, **kwargs)
		if not self.uuid:
			self.uuid = f'{datetime.datetime.now().year}_{self.id}'
		super(Patient, self).save()

class Representative(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	name_of_local_guardian = models.CharField(name='name_of_local_guardian', verbose_name="Name of Local Guardian", blank=True, null=True, max_length=100)
	address_of_local_guardian = models.TextField(name='address_of_local_guardian', verbose_name="Address of Local Guardian", blank=True, null=True)
	phone_number_local_guardian = models.IntegerField(name='phone_number_local_guardian', verbose_name="Phone Number of Local Guardian", blank=True, null=True, max_length=10)
	name_of_person_responsible_for_treatment = models.CharField(name='name_of_person_responsible_for_treatment', verbose_name="Name of Person Responsible for Treatment", blank=True, null=True, max_length=100)
	relationship_with_patient = models.CharField(name='relationship_with_patient', verbose_name="Relationship with Patient", blank=True, null=True, max_length=100)
	address_of_person_responsible = models.CharField(name='address_of_person_responsible', verbose_name="Address of Person Responsible for Treatment", blank=True, null=True, max_length=100)
	phone_number_person_responsible = models.IntegerField(name='phone_number_person_responsible', verbose_name="Phone Number of Person Responsible for Treatment", blank=True, null=True, max_length=10)
	detail_of_id_proof_recieved = models.TextField(name='detail_of_id_proof_recieved', verbose_name="Details of ID Proof Recieved", blank=True, null=True)

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
    monthly_fee_first_month = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    lab_charge = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    monthly_fee_second_month = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    monthly_fee_third_month = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"MOU for Patient: {self.patient.name}"

class ItemQuantity(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	item = models.CharField(max_length=255, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	
	def __str__(self):
		return f"{self.item} - {self.quantity}"
	
class ReportFindings(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    chief_complaints = models.TextField(verbose_name="Chief Complaints", blank=True, null=True)
    frame_of_reference = models.TextField(verbose_name="Frame of Reference", blank=True, null=True)
    learning_disability_findings = models.TextField(verbose_name="Learning Disability Findings", blank=True, null=True)
    relevant_history_childhood_findings = models.TextField(verbose_name="Relevant History and Childhood Findings", blank=True, null=True)
    depression_anxiety_findings = models.TextField(verbose_name="Depression & Anxiety Findings", blank=True, null=True)
    findings_on_needle_condom_awareness = models.TextField(verbose_name="Findings on Needle and Condom Awareness", blank=True, null=True)
    findings_over_trauma = models.TextField(verbose_name="Findings over Trauma", blank=True, null=True)
    aspects_traits_of_personality = models.TextField(verbose_name="Aspects and Traits of Personality", blank=True, null=True)
    summary = models.TextField(verbose_name="Summary", blank=True, null=True)

    def __str__(self):
        return f"Report Findings for {self.patient.name}"

class TemporaryRelease(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date_of_taking_over = models.DateField(name='date_of_taking_over', verbose_name="Date of Taking Over", blank=True, null=True)
	reason = models.CharField(max_length=255, blank=True, null=True)
	date_of_return = models.DateField(name='date_of_return', verbose_name="Date of Return", blank=True, null=True)

	def __str__(self):
		return f"{self.patient.name} - {self.reason}"

class JudicialProceedings(models.Model):
	YES = 'Yes'
	NO = 'No'
	CHOICES = [
		(YES, 'Yes'),
		(NO, 'No'),
	]
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date_of_hearing = models.DateField(name='date_of_hearing', verbose_name="Date of Hearing", blank=True, null=True)
	case_no = models.CharField(max_length=255, blank=True, null=True)
	allowed_to_attend = models.CharField(name='allowed_to_attend', max_length=255, verbose_name="Allowed to Attend", blank=True, null=True, choices=CHOICES)

	def __str__(self):
		return f"{self.patient.name} - {self.case_no_}"