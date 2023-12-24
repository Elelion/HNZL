from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from patients.forms import PatientAddForm, PatientEditForm
from patients.models import COPDPatients
from django.contrib import messages
from patients.models_choices import DISPENSARY_OBSERVATION_STATUS


@login_required
def browse(request, page_number=1):
    current_site = request.get_host()

    breadcrumb_data = [
        {'label': current_site, 'url': current_site},
        {'label': 'Пациенты', 'url': '#'},
    ]

    patients_status_counts = {}
    for key, val in DISPENSARY_OBSERVATION_STATUS:
        patients_status_counts[val] = COPDPatients.objects.filter(
            dispensary_observation_status=key).count()

    patients = COPDPatients.objects.all()
    items_per_page = 10
    paginator = Paginator(patients, items_per_page)
    patients_paginator = paginator.page(page_number)

    # **

    context = {
        'breadcrumb_data': breadcrumb_data,
        'COPDPatients': patients_paginator,
        'patients_status_counts': patients_status_counts,
        'current_url': request.path,
    }

    return render(request, 'patients/browse.html', context)


@login_required()
def search(request):
    current_site = request.get_host()

    breadcrumb_data = [
        {'label': current_site, 'url': current_site},
        {'label': 'Поиск', 'url': '#'},
    ]

    # **

    query = request.GET.get('patients_search', '')

    if query:
        results = COPDPatients.objects.filter(Q(patronymic__icontains=query) | Q(name__icontains=query))
    else:
        return HttpResponseRedirect(reverse('patients:browse'))

    context = {
        'breadcrumb_data': breadcrumb_data,
        'COPDPatients': results,
        'patients_status_counts': results.count(),
        'current_url': request.path,
    }

    return render(request, 'patients/browse.html', context)


@login_required
def add(request):
    current_site = request.get_host()

    breadcrumb_data = [
        {'label': current_site, 'url': current_site},
        {'label': 'Пациенты', 'url': HttpResponseRedirect(reverse('patients:browse'))},
        {'label': 'Добавить', 'url': '#'},
    ]

    # **

    if request.method == 'POST':
        form = PatientAddForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Пациент успешно добавлен в БД')

            return HttpResponseRedirect(reverse('patients:browse'))

    else:
        form = PatientAddForm()

    # **

    context = {
        'form': form,
        'breadcrumb_data': breadcrumb_data,
        'add_url': reverse('patients:add')
    }

    return render(request, 'patients/add_edit.html', context)


@login_required
def edit(request, patient_id):
    # Получите данные пациента по ID из базы данных
    patient = COPDPatients.objects.get(pk=patient_id)

    current_site = request.get_host()

    breadcrumb_data = [
        {'label': current_site, 'url': current_site},
        {'label': 'Пациенты', 'url': HttpResponseRedirect(reverse('patients:browse'))},
        {'label': f'Редактирование ID: {patient_id} ({patient.patronymic} {patient.name} {patient.surname})', 'url': '#'},
    ]

    # **

    if request.method == 'POST':

        # Передайте данные пациента в форму для редактирования
        form = PatientEditForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                f'ID: {patient_id} ('
                f'{patient.patronymic} {patient.name} {patient.surname}'
                f') - изменен')

            return HttpResponseRedirect(reverse('patients:browse'))
    else:
        form = PatientEditForm(instance=patient)

    # **

    context = {
        'form': form,
        'breadcrumb_data': breadcrumb_data,
        'patient': patient,
    }

    return render(request, 'patients/add_edit.html', context)


@login_required
def delete(request, patient_id):
    patient = COPDPatients.objects.get(id=patient_id)
    patient.delete()

    messages.warning(
        request,
        f'ID: {patient_id} ('
        f'{patient.patronymic} {patient.name} {patient.surname}'
        f') - успешно удален')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
