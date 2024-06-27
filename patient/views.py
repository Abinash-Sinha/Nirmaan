from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
import base64
from .models import Patient, Representative, Declaration, MOU
from .forms import PatientForm, RepresentativeForm, DeclarationForm, MOUForm

@login_required()
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        representative_form = RepresentativeForm(request.POST)
        declaration_form = DeclarationForm(request.POST)
        mou_form = MOUForm(request.POST)

        # print(form.is_valid())
        if form.is_valid() and representative_form.is_valid() and declaration_form.is_valid() and mou_form.is_valid():
            image_data = request.POST.get('image_data')  # Get the base64-encoded image data from the form
            if image_data:
                # Decode base64 data and save as a file in the media directory
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]
                image_filename = f'patient_image_{request.POST.get("name")}.{ext}'
                image_path = os.path.join('media', 'patient_images', image_filename)
                
                # Decode base64 and write to file
                with open(image_path, 'wb') as f:
                    f.write(base64.b64decode(imgstr))
                
                # Save form with image path to the database
                patient = form.save(commit=False)
                patient.image = os.path.join('patient_images', image_filename)
                patient.save()
            else:
                patient = form.save()
            
            # Save representative form
            representative = representative_form.save(commit=False)
            representative.patient = patient
            representative.save()

            # Save declaration form
            declaration = declaration_form.save(commit=False)
            declaration.patient = patient
            declaration.save()

            # Save mou form
            mou = mou_form.save(commit=False)
            mou.patient = patient
            mou.save()

            return redirect('get_patients')
    else:
        form = PatientForm()
        representative_form = RepresentativeForm()
        declaration_form = DeclarationForm()
        mou_form = MOUForm()

    return render(request, 'patient_add.html', {'form': form, 'representative_form': representative_form, 'declaration_form': declaration_form, 'mou_form': mou_form})

@login_required()
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    representative = get_object_or_404(Representative, patient=patient)
    declaration = get_object_or_404(Declaration, patient=patient)
    mou = get_object_or_404(MOU, patient=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        representative_form = RepresentativeForm(request.POST, instance=representative)
        declaration_form = DeclarationForm(request.POST, instance=declaration)
        mou_form = MOUForm(request.POST, instance=mou)

        if form.is_valid() and representative_form.is_valid() and declaration_form.is_valid() and mou_form.is_valid():
            form.save()
            representative_form.save()
            declaration_form.save()
            mou_form.save()
            return HttpResponseRedirect(reverse('get_patients'))
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PatientForm(instance=patient)
        representative_form = RepresentativeForm(instance=representative)
        declaration_form = DeclarationForm(instance=declaration)
        mou_form = MOUForm(instance=mou)

    return render(request, 'patient_edit.html', {'form': form, 'representative_form': representative_form, 'declaration_form': declaration_form, 'mou_form': mou_form, 'patient': patient})

@login_required()
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        patient.delete()
        return HttpResponseRedirect(reverse('get_patients'))
    return HttpResponseRedirect(reverse('get_patients'))

@login_required()
def get_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

@login_required()
def view_patient_details(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    representative = get_object_or_404(Representative, patient=patient)
    declaration = get_object_or_404(Declaration, patient=patient)

    return render(request, 'patient_details.html', {'patient': patient, 'representative': representative, 'declaration': declaration})

def view_representative(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    representative = get_object_or_404(Representative, patient=patient)
    return render(request, 'view_representative.html', {'patient': patient, 'representative': representative})

@login_required
def search_patients(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_search.html', {'patients': patients, 'query': query})