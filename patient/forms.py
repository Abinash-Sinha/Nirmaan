from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, Submit
from crispy_forms.bootstrap import InlineRadios
from drf_extra_fields.fields import Base64ImageField
from .models import Patient, Representative, Declaration, MOU, ItemQuantity, ReportFindings, TemporaryRelease

class PatientForm(forms.ModelForm):
    image_data = Base64ImageField(required=False)
    
    class Meta:
        model = Patient
        fields = [
            'name', 'admission_date', 'release_date', 'date_of_birth', 'father_name', 'mother_name',
            'image', 'occupation', 'qualification', 'marital_status', 'religion', 'income_pm',
            'language_spoken', 'phone_number_1', 'phone_number_2', 'whatsapp_number', 'email_id',
            'details_of_id_proof_recieved', 'cut_mark_detail', 'substance_abuse', 'psychological_disturbance',
            'vindictiveness', 'behavioural_disfunctions', 'prediagnosed_mental_condition'
        ]
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'phone_number_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'details_of_id_proof_recieved': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cut_mark_detail': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'substance_abuse': 'Substance Abuse',
            'psychological_disturbance':'Psychological Disturbance',
            'vindictiveness': 'Vindictiveness',
            'behavioural_disfunctions': 'Behavioural Disfunction',
            'prediagnosed_mental_condition': 'Pre-Diagnosed Mental Health Condition'
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('admission_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('release_date', css_class='form-group col-md-6 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('father_name', css_class='form-group col-md-6 mb-0'),
                Column('mother_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('occupation', css_class='form-group col-md-6 mb-0'),
                Column('qualification', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('marital_status', css_class='form-group col-md-6 mb-0'),
                Column('religion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('income_pm', css_class='form-group col-md-6 mb-0'),
                Column('language_spoken', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number_1', css_class='form-group col-md-4 mb-0'),
                Column('phone_number_2', css_class='form-group col-md-4 mb-0'),
                Column('whatsapp_number', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email_id', css_class='form-group col-md-6 mb-0'),
                Column('cut_mark_detail', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('details_of_id_proof_recieved', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('substance_abuse', css_class='form-group col-md-6 mb-0'),
                Column('psychological_disturbance', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('vindictiveness', css_class='form-group col-md-6 mb-0'),
                Column('behavioural_disfunctions', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('prediagnosed_mental_condition', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
    
class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = [
            'name_of_local_guardian', 
            'address_of_local_guardian',
            'phone_number_local_guardian',
            'name_of_person_responsible_for_treatment',
            'relationship_with_patient',
            'address_of_person_responsible', 
            'phone_number_person_responsible', 
            'detail_of_id_proof_recieved'
        ]
        widgets = {
            'name_of_local_guardian': forms.TextInput(attrs={'class': 'form-control'}),
            'address_of_local_guardian': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone_number_local_guardian': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_of_person_responsible_for_treatment': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship_with_patient': forms.TextInput(attrs={'class': 'form-control'}),
            'address_of_person_responsible': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone_number_person_responsible': forms.NumberInput(attrs={'class': 'form-control'}),
            'detail_of_id_proof_recieved': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(RepresentativeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('name_of_local_guardian', css_class='form-group col-md-6 mb-0'),
                Column('phone_number_local_guardian', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address_of_local_guardian', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('name_of_person_responsible_for_treatment', css_class='form-group col-md-6 mb-0'),
                Column('phone_number_person_responsible', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('relationship_with_patient', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address_of_person_responsible', css_class='form-group col-md-12 mb-0'),
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
            'monthly_fee_first_month', 
            'lab_charge', 
            'monthly_fee_second_month', 
            'monthly_fee_third_month'
        ]
        widgets = {
            'monthly_fee_first_month': forms.NumberInput(attrs={'step': '0.01'}),
            'lab_charge': forms.NumberInput(attrs={'step': '0.01'}),
            'monthly_fee_second_month': forms.NumberInput(attrs={'step': '0.01'}),
            'monthly_fee_third_month': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'narcotics_drugs_abuse': 'Narcotics Drugs Abuse',
            'psychotropic_substance_abuse': 'Psychotropic Substance Abuse',
            'controlled_substance_abuse': 'Controlled Substance Abuse',
            'alcohol_beyond_permissible_limits': 'Consumption of Alcohol beyond permissible limits',
            'behavioural_psychological_condition': 'Associated Underlying Behavioural and Psychological Condition',
            'mental_health_issue': 'Pre-Diagnosed Mental Health Issue',
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

class ItemQuantityForm(forms.ModelForm):
    class Meta:
        model = ItemQuantity
        fields = ['item', 'quantity']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemQuantityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('item', css_class='form-group col-md-6 mb-0'),
                Column('quantity', css_class='form-group col-md-6 mb-0'),
            ),
        )

from django.forms import modelformset_factory

ItemQuantityFormSet = modelformset_factory(ItemQuantity, form=ItemQuantityForm, extra=1, can_delete=True)

class ReportFindingsForm(forms.ModelForm):
    class Meta:
        model = ReportFindings
        fields = [
            'chief_complaints',
            'frame_of_reference',
            'learning_disability_findings',
            'relevant_history_childhood_findings',
            'depression_anxiety_findings',
            'findings_on_needle_condom_awareness',
            'findings_over_trauma',
            'aspects_traits_of_personality',
            'summary'
        ]
        widgets = {
            'chief_complaints': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'frame_of_reference': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'learning_disability_findings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'relevant_history_childhood_findings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'depression_anxiety_findings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'findings_on_needle_condom_awareness': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'findings_over_trauma': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'aspects_traits_of_personality': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'chief_complaints': 'Chief Complaints',
            'frame_of_reference': 'Frame of Reference',
            'learning_disability_findings': 'Learning Disability Findings',
            'relevant_history_childhood_findings': 'Relevant History and Childhood Findings',
            'depression_anxiety_findings': 'Depression & Anxiety Findings',
            'findings_on_needle_condom_awareness': 'Findings on Needle and Condom Awareness',
            'findings_over_trauma': 'Findings over Trauma',
            'aspects_traits_of_personality': 'Aspects and Traits of Personality',
            'summary': 'Summary'
        }

    def __init__(self, *args, **kwargs):
        super(ReportFindingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('chief_complaints', css_class='form-group col-md-6 mb-0'),
                Column('frame_of_reference', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('learning_disability_findings', css_class='form-group col-md-6 mb-0'),
                Column('relevant_history_childhood_findings', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('depression_anxiety_findings', css_class='form-group col-md-6 mb-0'),
                Column('findings_on_needle_condom_awareness', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('findings_over_trauma', css_class='form-group col-md-6 mb-0'),
                Column('aspects_traits_of_personality', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('summary', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
        )

class TemporaryReleaseForm(forms.ModelForm):
    class Meta:
        model = TemporaryRelease
        fields = [
            'date_of_taking_over',
            'reason',
            'date_of_return'
        ]
        widgets = {
            'date_of_taking_over': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_return': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'date_of_taking_over': 'Date of Taking Over',
            'reason': 'Reason',
            'date_of_return': 'Date of Return'
        }

    def __init__(self, *args, **kwargs):
        super(TemporaryReleaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('date_of_taking_over', css_class='form-group col-md-6 mb-0'),
                Column('date_of_return', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('reason', css_class='form-group col-md-12 mb-0'),
            ),
        )

TemporaryReleaseFormSet = modelformset_factory(
    TemporaryRelease,
    form=TemporaryReleaseForm,
    extra=1,  # Number of extra forms to display
    can_delete=True  # Allow deleting forms
)