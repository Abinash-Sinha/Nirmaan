from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'father_name', 'mother_name', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
    image_data = forms.FileField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))