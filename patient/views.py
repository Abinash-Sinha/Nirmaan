from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm

@login_required()
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_patients'))
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})

@login_required()
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_patients'))
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_edit.html', {'form': form, 'patient': patient})

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
    return render(request, 'patient_details.html', {'patient': patient})