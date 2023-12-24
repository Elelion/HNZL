from datetime import date
from django.db import models

from patients.models_choices import *


class COPDPatients(models.Model):
    class Meta:
        db_table = 'COPD_patients'
        verbose_name = "пациента"
        verbose_name_plural = "Пациенты ХОБЛ"

    # 1 - номер - это ID по умолчанию

    # 2.1 - имя
    name = models.CharField(max_length=20)

    # 2.2 - отчество
    surname = models.CharField(max_length=30)

    # 2.3 - фамилия
    patronymic = models.CharField(max_length=30)

    # 3 - дата рождения
    # birthday = models.DateField()
    birthday = models.CharField(max_length=30)

    # 4 - возраст
    age = models.PositiveSmallIntegerField(default=0)

    # 5 - адрес
    address = models.CharField(max_length=150)

    # **

    # 6 - МО прикрепления
    medical_organization_attachments = models.CharField(max_length=200)

    # 7 - Год установления диагноза	ХОБЛ
    year_of_diagnosis_of_COPD = models.DateField(default=date.today)

    # 8 - Инвалидность
    disability = models.BooleanField(default=False)

    # 9 - Госпитализации в течении 12 мес с кодом по МКБ
    hospitalization_with_year_with_ICD = models.CharField(max_length=30)

    # 10 - Количество обращений по поводу ХОБЛ за год
    requests_number_COPD = models.PositiveSmallIntegerField(default=0)

    # 11 - Количество обращений по поводу ХОБЛ за год - по поводу обострений
    requests_number_COPD_with_aggravation = models.PositiveSmallIntegerField(default=0)

    # 12 - Лечение амбулаторных обострений
    outpatient_exacerbations = models.CharField(max_length=20)

    # 13 - Вакцинация против (гриппа, пневмококка)
    vaccination = models.CharField(
        max_length=1,
        choices=VACCINATION_CHOICES,
        default=1,
    )

    # 14 - ОФВ/ФЖЕЛ после бронходилатации
    FEV_FVC_after_bronchodilation = models.CharField(max_length=10)

    # 15 - ОФВ1 после бронходилатации
    OFV1_after_bronchodilation = models.CharField(max_length=200)

    # 16 - Эозинофилы крови кл/мкл
    blood_eosinophils = models.FloatField(default=1.0)

    # 17 - Сатурация
    saturation = models.PositiveSmallIntegerField(default=0)

    # 18 - mMRC
    m_MRC = models.PositiveSmallIntegerField(choices=M_MRC_CHOICES, default=1)


    # 19 - Коротко действующие бронходилататоры, кол-во ингаляторов год
    salbutamol = models.CharField(
        max_length=1,
        choices=SALBUTAMOL_CHOICES,
        default=1,
    )

    # 20 - ДДБА/ДДАХП
    DDBA_DDAHP = models.CharField(
        max_length=1,
        choices=DDBA_DDAHP_CHOICES,
        default=5,
    )

    # 21 - ИГКС/ДДБА указать МНН
    IGCS_DDBA = models.CharField(
        max_length=1,
        choices=IGCS_DDBA_CHOICES,
        default=1,
    )

    # 22 - ДДАХП
    DDAHP = models.CharField(
        max_length=1,
        choices=DDAHP_CHOICES,
        default=1,
    )

    # 23 - Тройные фиксированные комбинации
    triple_fixed_combinations = models.CharField(
        max_length=1,
        choices=TRIPLE_FIXED_COMBINATIONS_CHOICES,
        default=1,
    )

    # 24 - посев мокроты: результат микробиологического анализа
    sputum_sowing = models.CharField(max_length=200)


    # 25 - сопутствующие заболевания: код МКБ
    ICD = models.PositiveSmallIntegerField(default=0)


    # 26 - Дата поступления на учет
    consists_under_DN = models.DateField()

    # 27 - Исход заболевания за год
    diseases_per_year = models.CharField(
        max_length=1,
        choices=DISEASES_PER_YEAR_CHOICES,
        default=1,
    )

    # 28 - Непосредственная причина смерти
    cause_of_death = models.TextField()

    # **

    # 29 - Диспансерное наблюдение с датой (это статус)
    # выбыл / переехал / умер
    dispensary_observation_status = models.CharField(
        max_length=1,
        choices=DISPENSARY_OBSERVATION_STATUS,
        default=1,
    )

    dispensary_observation_date_status = models.DateField()

    def __str__(self):
        return f"id: {self.id} | ФИО: {self.name}"
