from django import forms
from patients.models import COPDPatients
from patients.models_choices import *


class PatientAddForm(forms.ModelForm):
    # 2.1 - Имя
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'required': ''
            }
        )
    )

    # 3 - Дата рождения
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'required': '',
            }
        )
    )

    # 2.2 - Отчество
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество',
                'required': '',
            }
        )
    )

    # 4 - Возраст
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '33',
                'required': '',
            }
        )
    )

    # 2.3 - Фамилия
    patronymic = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
                'required': '',
            }
        )
    )

    # 5 - Адрес
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес проживания пациента',
                'required': ''
            }
        )
    )

    # **

    # 6 - МО прикрепления
    medical_organization_attachments = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите МО прикрепления',
                'rows': 2,
                'required': ''
            }
        )
    )

    # 7 - Год установления диагноза	ХОБЛ
    year_of_diagnosis_of_COPD = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'required': '',
            }
        )
    )

    # 8 - Инвалидность
    disability = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'p-switch-style',
                'type': 'checkbox',
            }
        ),
        initial=False,
        required=False
    )

    # 9 - Госпитализации в течении 12 мес с кодом по МКБ
    hospitalization_with_year_with_ICD = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите госп-ции в за 12 мес с кодом по МКБ',
                # 'maxlength': '10',
                'required': '',
            }
        )
    )

    # 10 - Количество обращений по поводу ХОБЛ за год
    requests_number_COPD = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '0',
                'required': '',
            }
        )
    )

    # 11 - Количество обращений по поводу ХОБЛ за год - по поводу обострений
    requests_number_COPD_with_aggravation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '0',
                'required': '',
            }
        )
    )

    # 12 - Лечение амбулаторных обострений
    outpatient_exacerbations = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите лечение амбулаторных обострений',
                'required': '',
            }
        )
    )

    # 13 - Вакцинация против (гриппа, пневмококка)
    vaccination = forms.ChoiceField(
        choices=VACCINATION_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 14 - ОФВ/ФЖЕЛ после бронходилатации
    FEV_FVC_after_bronchodilation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ОФВ/ФЖЕЛ после бронходилатации',
                'required': '',
            }
        )
    )

    # 15 - ОФВ1 после бронходилатации
    OFV1_after_bronchodilation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ОФВ1 после бронходилатации',
                'required': '',
            }
        )
    )

    # 16 - Эозинофилы крови кл/мкл
    blood_eosinophils = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '1.0',
                'step': 'any',  # Позволяет вводить числа с плавающей точкой
                'required': '',
            }
        )
    )

    # 17 - Сатурация
    saturation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '0',
                'required': '',
            }
        )
    )

    # 18 - mMRC
    m_MRC = forms.ChoiceField(
        choices=M_MRC_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 19 - Коротко действующие бронходилататоры, кол-во ингаляторов год
    salbutamol = forms.ChoiceField(
        choices=SALBUTAMOL_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 20 - ДДБА/ДДАХП
    DDBA_DDAHP = forms.ChoiceField(
        choices=DDBA_DDAHP_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 21 - ИГКС/ДДБА указать МНН
    IGCS_DDBA = forms.ChoiceField(
        choices=IGCS_DDBA_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 22 - ДДАХП
    DDAHP = forms.ChoiceField(
        choices=DDAHP_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 23 - Тройные фиксированные комбинации
    triple_fixed_combinations = forms.ChoiceField(
        choices=TRIPLE_FIXED_COMBINATIONS_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 24 - посев мокроты: результат микробиологического анализа
    sputum_sowing = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите посев мокроты: результат микробиологического анализа',
                'required': '',
            }
        )
    )

    # 25 - сопутствующие заболевания: код МКБ
    ICD = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'value': '0',
                'required': '',
            }
        )
    )

    # 26 - Дата поступления на учет
    consists_under_DN = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'required': '',
            }
        )
    )

    # 27 - Исход заболевания за год
    diseases_per_year = forms.ChoiceField(
        choices=DISEASES_PER_YEAR_CHOICES,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    # 28 - Непосредственная причина смерти
    cause_of_death = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите непосредственную причину смерти',
                'required': '',
            }
        )
    )

    # **

    # 29 - Диспансерное наблюдение с датой (это статус)
    dispensary_observation_status = forms.ChoiceField(
        choices=DISPENSARY_OBSERVATION_STATUS,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    dispensary_observation_date_status = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'required': '',
            }
        )
    )

    # **

    class Meta:
        model = COPDPatients
        fields = '__all__'


# -----------------------------------------------------------------------------


class PatientEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    birthday = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    patronymic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    # **

    medical_organization_attachments = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 2}))

    year_of_diagnosis_of_COPD = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    disability = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'p-switch-style',
                'type': 'checkbox'
            }
        ),
        required=False
    )

    hospitalization_with_year_with_ICD = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    requests_number_COPD = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    requests_number_COPD_with_aggravation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    outpatient_exacerbations = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    vaccination = forms.ChoiceField(
        choices=VACCINATION_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    FEV_FVC_after_bronchodilation = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    OFV1_after_bronchodilation = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    blood_eosinophils = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 'any'}))

    saturation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    m_MRC = forms.ChoiceField(
        choices=M_MRC_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    salbutamol = forms.ChoiceField(
        choices=SALBUTAMOL_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    DDBA_DDAHP = forms.ChoiceField(
        choices=DDBA_DDAHP_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    IGCS_DDBA = forms.ChoiceField(
        choices=IGCS_DDBA_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    DDAHP = forms.ChoiceField(
        choices=DDAHP_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    triple_fixed_combinations = forms.ChoiceField(
        choices=TRIPLE_FIXED_COMBINATIONS_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    sputum_sowing = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    ICD = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    consists_under_DN = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    diseases_per_year = forms.ChoiceField(
        choices=DISEASES_PER_YEAR_CHOICES, widget=forms.Select(
            attrs={'class': 'form-select'}))

    cause_of_death = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    # **

    dispensary_observation_status = forms.ChoiceField(
        choices=DISPENSARY_OBSERVATION_STATUS, widget=forms.Select(
            attrs={'class': 'form-select'}))

    dispensary_observation_date_status = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    # для примера
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py4', 'readonly': True}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py4', 'readonly': True}))

    # **

    class Meta:
        model = COPDPatients
        fields = '__all__'


# -----------------------------------------------------------------------------


class PatientSearchForm(forms.ModelForm):
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    # **

    class Meta:
        model = COPDPatients
        fields = '__all__'