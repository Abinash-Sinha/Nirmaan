from mimetypes import init
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
import base64
from .models import Patient, Representative, Declaration, MOU, ItemQuantity, ReportFindings, TemporaryRelease
from .forms import PatientForm, RepresentativeForm, DeclarationForm, MOUForm, ItemQuantityFormSet, ReportFindingsForm, TemporaryReleaseFormSet

@login_required()
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        representative_form = RepresentativeForm(request.POST)
        declaration_form = DeclarationForm(request.POST)
        mou_form = MOUForm(request.POST)
        report_findings_form = ReportFindingsForm(request.POST)

        item_quantity_formset = ItemQuantityFormSet(request.POST, prefix='item_quantity_formset')
        temporary_release_formset = TemporaryReleaseFormSet(request.POST, prefix='temporary_release_formset')

        # print(form.is_valid())
        if form.is_valid() and representative_form.is_valid() and declaration_form.is_valid() and mou_form.is_valid() and item_quantity_formset.is_valid() and report_findings_form.is_valid() and temporary_release_formset.is_valid():
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

            # Save report_findings forms
            report_findings = report_findings_form.save(commit=False)
            report_findings.patient = patient
            report_findings.save()

            # Save item formset
            item_quantity = item_quantity_formset.save(commit=False)
            for form in item_quantity:
                form.patient = patient
                form.save()
            
            temporary_release_list = temporary_release_formset.save(commit=False)
            for temporary_release in temporary_release_list:
                temporary_release.patient = patient
                temporary_release.save()

            return redirect('get_patients')
    else:
        form = PatientForm()
        representative_form = RepresentativeForm()
        declaration_form = DeclarationForm()
        mou_form = MOUForm()
        report_findings_form = ReportFindingsForm()
        item_quantity_formset = ItemQuantityFormSet(queryset=ItemQuantity.objects.none(), prefix='item_quantity_formset')
        temporary_release_formset = TemporaryReleaseFormSet(queryset=TemporaryRelease.objects.none(), prefix='temporary_release_formset')
        
    context = {'form': form, 
               'representative_form': representative_form, 
               'declaration_form': declaration_form, 
               'mou_form': mou_form,
               'report_findings_form': report_findings_form,
               'item_quantity_formset': item_quantity_formset,
               'temporary_release_formset': temporary_release_formset,
               }

    return render(request, 'patient_add.html', context=context)

@login_required()
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    representative = Representative.objects.filter(patient=patient).first()
    declaration = Declaration.objects.filter(patient=patient).first()
    mou = MOU.objects.filter(patient=patient).first()
    reports = ReportFindings.objects.filter(patient=patient).first()
    item_quantities = ItemQuantity.objects.filter(patient=patient)
    temporary_releases = TemporaryRelease.objects.filter(patient=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        representative_form = RepresentativeForm(request.POST, instance=representative)
        declaration_form = DeclarationForm(request.POST, instance=declaration)
        mou_form = MOUForm(request.POST, instance=mou)
        reports_form = ReportFindingsForm(request.POST, instance=reports)
        item_quantity_formset = ItemQuantityFormSet(request.POST, prefix='item_quantity_formset')
        temporary_release_formset = TemporaryReleaseFormSet(request.POST, prefix='temporary_release_formset')

        if form.is_valid() and representative_form.is_valid() and declaration_form.is_valid() and mou_form.is_valid() and reports_form.is_valid() and item_quantity_formset.is_valid() and temporary_release_formset.is_valid():
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
                form.save()
            representative_form.save()
            declaration_form.save()
            mou_form.save()
            reports_form.save()
            item_quantity_list = item_quantity_formset.save(commit=False)
            for item_quantity in item_quantity_list:
                item_quantity.patient = patient
                item_quantity.save()
            temporary_release_list = temporary_release_formset.save(commit=False)
            for temporary_release in temporary_release_list:
                temporary_release.patient = patient
                temporary_release.save()

            return HttpResponseRedirect(reverse('view_patient', kwargs={'patient_id': patient.id}))
        else:
            return JsonResponse({'success': False, 'errors': temporary_release_formset.errors})
    else:
        form = PatientForm(instance=patient)
        representative_form = RepresentativeForm(instance=representative)
        declaration_form = DeclarationForm(instance=declaration)
        mou_form = MOUForm(instance=mou)
        reports_form = ReportFindingsForm(instance=reports)
        item_quantity_formset = ItemQuantityFormSet(queryset=item_quantities, prefix='item_quantity_formset')
        temporary_release_formset = TemporaryReleaseFormSet(queryset=temporary_releases, prefix='temporary_release_formset')

    context = {
        'form': form,
        'representative_form': representative_form,
        'declaration_form': declaration_form,
        'mou_form': mou_form,
        'reports_form': reports_form,
        'item_quantity_formset': item_quantity_formset,
        'temporary_release_formset': temporary_release_formset,
        'patient': patient
    }

    return render(request, 'patient_edit.html', context=context)

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
    representative = Representative.objects.filter(patient=patient).first()
    declaration = Declaration.objects.filter(patient=patient).first()
    mou = MOU.objects.filter(patient=patient).first()
    item_quantities = ItemQuantity.objects.filter(patient=patient)
    reports = ReportFindings.objects.filter(patient=patient).first()
    temporary_releases = TemporaryRelease.objects.filter(patient=patient)

    context = {}

    patient_form = PatientForm(instance=patient)
    representative_form = RepresentativeForm(instance=representative)
    declaration_form = DeclarationForm(instance=declaration)
    mou_form = MOUForm(instance=mou)
    reports_form = ReportFindingsForm(instance=reports)

    context["patient_form"] = patient_form
    context["representative_form"] = representative_form
    context["declaration_form"] = declaration_form
    context["mou_form"] = mou_form
    context["item_quantities"] = list(item_quantities)
    context["reports_form"] = reports_form
    context["temporary_releases"] = list(temporary_releases)
    context["patient"] = patient
    return render(request, 'patient_details.html', context=context)


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