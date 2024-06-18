from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from drf_extra_fields.fields import Base64ImageField
from .models import Patient, Representative

class PatientForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    image_data = Base64ImageField(required=False)
    release_date = forms.DateField(required=False)
    class Meta:
        model = Patient
        fields = ['name', 'admission_date','release_date', 'date_of_birth', 'father_name', 'mother_name', 'image', 
                  'occupation', 'qualification', 'marital_status', 'religion', 
                  'income_pm', 'language_spoken', 'phone_number', 'whatsapp_number', 
                  'email_id', 'details_of_id_proof_recieved', 'cut_mark_detail']
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'details_of_id_proof_recieved': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cut_mark_detail': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    
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