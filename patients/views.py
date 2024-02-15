from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from patients.forms import PatientAddForm, PatientEditForm
from patients.models import COPDPatients
from django.contrib import messages
from patients.models_choices import DISPENSARY_OBSERVATION_STATUS


class PatientsListView(ListView):
    model = COPDPatients
    context_object_name = 'COPDPatients'
    paginate_by = 10
    template_name = 'patients/browse.html'

    current_date = datetime.now().date()
    date_ago = current_date - timedelta(days=6*30)

    def get_queryset(self):
        """get_queryset родительского класса"""
        queryset = super(PatientsListView, self).get_queryset()
        return queryset

    def get_dispensary_patients_count(self, dispensary=False):
        dispensary_counts = {}

        for key, val in DISPENSARY_OBSERVATION_STATUS:
            queryset = self.model.objects.filter(dispensary_observation_status=key)

            if dispensary:
                queryset = queryset.filter(
                    dispensary_observation_date_status__lt=self.date_ago,
                    dispensary_observation_status=key
                )

            dispensary_counts[val] = queryset.count()

        return dispensary_counts

    # аналогично выражению ниже
    # current_date = datetime.now().date()
    # date_ago = current_date - timedelta(days=6*30)
    # patients = COPDPatients.objects.filter(dispensary_observation_date_status__lt=date_ago)
    def get_alert_dispensary_patients(self):
        patients = self.get_queryset()
        dispensary_alert = False

        for patient in patients:
            # Получаем разницу между текущей датой и датой наблюдения пациента
            difference = self.current_date - patient.dispensary_observation_date_status

            # Если хотя бы у одного пациента разница больше 6 месяцев...
            if difference > timedelta(days=6*30):
                dispensary_alert = True
                break

        return dispensary_alert


class BrowseListView(PatientsListView):
    def get_context_data(self, **kwargs):
        context = super(BrowseListView, self).get_context_data()

        current_site = self.request.get_host()
        breadcrumb_data = [
            {'label': current_site, 'url': current_site},
            {'label': 'Пациенты', 'url': '#'},
        ]

        # **

        context['breadcrumb_data'] = breadcrumb_data
        context['patients_count'] = self.get_queryset().count()
        context['patients_dispensary'] = self.get_dispensary_patients_count()
        context['dispensary_alert'] = self.get_alert_dispensary_patients()
        return context


class DispensaryListView(PatientsListView):
    def get_queryset(self):
        """get_queryset перегруженный в классе DispensaryListView"""
        queryset = super(DispensaryListView, self).get_queryset()
        return queryset.filter(dispensary_observation_date_status__lt=self.date_ago)

    def get_context_data(self, **kwargs):
        context = super(DispensaryListView, self).get_context_data()

        current_site = self.request.get_host()
        breadcrumb_data = [
            {'label': current_site, 'url': current_site},
            {'label': 'Диспансеризация', 'url': '#'},
        ]

        # **

        context['breadcrumb_data'] = breadcrumb_data
        context['patients_count'] = self.get_queryset().count()
        context['patients_dispensary'] = self.get_dispensary_patients_count(True)
        context['dispensary_alert'] = self.get_alert_dispensary_patients()
        return context


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
        'patients_dispensary': results.count(),
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
