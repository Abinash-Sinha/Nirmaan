from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios
from drf_extra_fields.fields import Base64ImageField
from .models import Patient, Representative, Declaration, MOU

class PatientForm(forms.ModelForm):
    image_data = Base64ImageField(required=False)
    release_date = forms.DateField(required=False)
    
    class Meta:
        model = Patient
        fields = ['Name of Patient', 'Date of Admission','Date of Release', 'Date of Birth', 'Name of Father', 'Name of Mother', 
                  'Occupation', 'Qualification', 'Marital Status', 'Religion', 
                  'Income Per Month', 'Language(s) Spoken', 'Phone Number (1)','Phone Number (2)', 
                  'Whatsapp Number', 'Email Address', 'Details of ID Proof Recieved', 'Cut Mark Details']
        widgets = {
            'Date of Admission': forms.DateInput(attrs={'type': 'date'}),
            'Date of Release': forms.DateInput(attrs={'type': 'date'}),
            'Date of Birth': forms.DateInput(attrs={'type': 'date'}),
            'Marital Status': forms.Select(attrs={'class': 'form-control'}),
            'Religion': forms.Select(attrs={'class': 'form-control'}),
            'Phone Number (1)': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'Phone Number (2)': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'Whatsapp Number': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'Email Address': forms.EmailInput(attrs={'class': 'form-control'}),
            'Details of ID Proof Recieved': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'Cut Mark Details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Row(
                Column('Name of Patient', css_class='form-group col-md-6 mb-0'),
                Column('Date of Admission', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Date of Release', css_class='form-group col-md-6 mb-0'),
                Column('Date of Birth', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Name of Father', css_class='form-group col-md-6 mb-0'),
                Column('Name of Mother', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Occupation', css_class='form-group col-md-6 mb-0'),
                Column('Qualification', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Marital Status', css_class='form-group col-md-6 mb-0'),
                Column('Religion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Income Per Month', css_class='form-group col-md-6 mb-0'),
                Column('Language(s) Spoken', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Phone Number (1)', css_class='form-group col-md-4 mb-0'),
                Column('Phone Number (2)', css_class='form-group col-md-4 mb-0'),
                Column('Whatsapp Number', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Email Address', css_class='form-group col-md-6 mb-0'),
                Column('Cut Mark Details', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Details of ID Proof Recieved', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )
    
class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = [
            'father_name', 
            'mother_name', 
            'address', 
            'name_of_local_guardian', 
            'address_of_local_guardian', 
            'name_of_person_responsible_for_treatment', 
            'address_2', 
            'detail_of_id_proof_recieved'
        ]
        widgets = {
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'name_of_local_guardian': forms.TextInput(attrs={'class': 'form-control'}),
            'address_of_local_guardian': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'name_of_person_responsible_for_treatment': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'detail_of_id_proof_recieved': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(RepresentativeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('father_name', css_class='form-group col-md-6 mb-0'),
                Column('mother_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('name_of_local_guardian', css_class='form-group col-md-6 mb-0'),
                Column('address_of_local_guardian', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('name_of_person_responsible_for_treatment', css_class='form-group col-md-6 mb-0'),
                Column('address_2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('detail_of_id_proof_recieved', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )

class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration
        fields = [
            'verbal_abuse',
            'physical_abuse',
            'breaking_articles',
            'antisocial_activities',
            'law_suits',
            'abnormal_tendencies',
            'abnormal_romatic_involment',
            'high_risk_behavior',
            'unreasonable_anger',
            'irresponsible_aspects'
        ]
        widgets = {
            'verbal_abuse': forms.RadioSelect(choices=Declaration.CHOICES),
            'physical_abuse': forms.RadioSelect(choices=Declaration.CHOICES),
            'breaking_articles': forms.RadioSelect(choices=Declaration.CHOICES),
            'antisocial_activities': forms.RadioSelect(choices=Declaration.CHOICES),
            'law_suits': forms.RadioSelect(choices=Declaration.CHOICES),
            'abnormal_tendencies': forms.RadioSelect(choices=Declaration.CHOICES),
            'abnormal_romatic_involment': forms.RadioSelect(choices=Declaration.CHOICES),
            'high_risk_behavior': forms.RadioSelect(choices=Declaration.CHOICES),
            'unreasonable_anger': forms.RadioSelect(choices=Declaration.CHOICES),
            'irresponsible_aspects': forms.RadioSelect(choices=Declaration.CHOICES)
        }

    def __init__(self, *args, **kwargs):
        super(DeclarationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column(InlineRadios('verbal_abuse'), css_class='form-group col-md-6 mb-0'),
                Column(InlineRadios('physical_abuse'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('breaking_articles'), css_class='form-group col-md-6 mb-0'),
                Column(InlineRadios('antisocial_activities'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('law_suits'), css_class='form-group col-md-6 mb-0'),
                Column(InlineRadios('abnormal_tendencies'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('abnormal_romatic_involment'), css_class='form-group col-md-6 mb-0'),
                Column(InlineRadios('high_risk_behavior'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('unreasonable_anger'), css_class='form-group col-md-6 mb-0'),
                Column(InlineRadios('irresponsible_aspects'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

class MOUForm(forms.ModelForm):
    class Meta:
        model = MOU
        fields = [
            'narcotics_drugs_abuse', 
            'psychotropic_substance_abuse', 
            'controlled_substance_abuse', 
            'alcohol_beyond_permissible_limits', 
            'behavioural_psychological_condition', 
            'mental_health_issue', 
            'guardian_name', 
            'admission_date', 
            'monthly_fee_first_month', 
            'lab_charge', 
            'monthly_fee_second_month', 
            'monthly_fee_third_month'
        ]
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'monthly_fee_first_month': forms.NumberInput(attrs={'step': '0.01'}),
            'lab_charge': forms.NumberInput(attrs={'step': '0.01'}),
            'monthly_fee_second_month': forms.NumberInput(attrs={'step': '0.01'}),
            'monthly_fee_third_month': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'narcotics_drugs_abuse': 'Narcotics Drugs Abuse',
            'psychotropic_substance_abuse': 'Psychotropic Substance Abuse',
            'controlled_substance_abuse': 'Controlled Substance Abuse',
            'alcohol_beyond_permissible_limits': 'Alcohol beyond permissible limits',
            'behavioural_psychological_condition': 'Associated Underlying Behavioural and Psychological Condition',
            'mental_health_issue': 'Pre-Diagnosed Mental Health Issue',
            'guardian_name': 'Name of Local Guardian',
            'admission_date': 'Date of Admission',
            'monthly_fee_first_month': 'Monthly Fee for the first month',
            'lab_charge': 'Lab Charge',
            'monthly_fee_second_month': 'Monthly Fee for the second month',
            'monthly_fee_third_month': 'Monthly Fee for the third month',
        }

    def __init__(self, *args, **kwargs):
        super(MOUForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('narcotics_drugs_abuse', css_class='form-group col-md-6 mb-0'),
                Column('psychotropic_substance_abuse', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('controlled_substance_abuse', css_class='form-group col-md-6 mb-0'),
                Column('alcohol_beyond_permissible_limits', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('behavioural_psychological_condition', css_class='form-group col-md-6 mb-0'),
                Column('mental_health_issue', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('guardian_name', css_class='form-group col-md-6 mb-0'),
                Column('admission_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('monthly_fee_first_month', css_class='form-group col-md-6 mb-0'),
                Column('lab_charge', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('monthly_fee_second_month', css_class='form-group col-md-6 mb-0'),
                Column('monthly_fee_third_month', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )