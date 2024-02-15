from django import forms
from home.ClientQuestionsList import QUESTIONS


# **


class ClientQuestionForDate(forms.Form):
    """Класс родитель для создания компонентов даты в формах"""

    quest_number = 0

    def __init__(self, quest_number):
        self.quest_number = quest_number

    # **

    def get_date_field_for_last_visit(self):
        return forms.DateField(
            widget=forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'required': '',
                }
            )
        )

    def get_quest_number_from_hidden_field(self):
        return forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'value': self.quest_number,
            'type': 'hidden',
            'required': ''}))


# **


# вопрос №1
class ClientQuestion1Form(forms.Form):
    question_title = "Рассчет ИМТ (индекс массы тела)"

    # рост
    form1_height = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш рост в см, например: 180',
        'min': 100,
        'max': 250,
        'required': ''}))

    # вес
    form1_weight = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш вес в кг, например: 80',
        'min': 40,
        'max': 350,
        'required': ''}))

    quest_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'value': 1,
        'type': 'hidden',
        'required': ''}))


# вопрос №2
class ClientQuestion2Form(forms.Form):
    question_title = "Рассчет АД (артериального давления)"

    # максимальне давление
    form2_max = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Верхнее давление, например: 120',
        'min': 70,
        'max': 250,
        'required': ''}))

    # минимальное давление
    form2_min = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Нижнее давление, например: 80',
        'min': 40,
        'max': 200,
        'required': ''}))

    quest_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'value': 2,
        'type': 'hidden',
        'required': ''}))


# вопрос №3
class ClientQuestion3Form(forms.Form):
    question_title = "Рассчет холестирина"

    # холестирин
    form3_cholesterol = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш показатель холестирина, например: 3.5',
        'min': 2.5,
        'max': 15.5,
        'required': ''}))

    quest_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'value': 3,
        'type': 'hidden',
        'required': ''}))


# вопрос №4
class ClientQuestion4Form(forms.Form):
    question_title = "Рассчет глюкозы"

    # Глюкоза
    form4_glucose = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш показатель глюкозы, например: 5.5',
        'min': 2.5,
        'max': 15.5,
        'required': ''}))

    quest_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'value': 4,
        'type': 'hidden',
        'required': ''}))


# вопрос №5
class ClientQuestion5Form(forms.Form):
    for_date = ClientQuestionForDate(5)
    question_title = QUESTIONS[5-1][1]

    # Онкологические заболевания
    form5_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №6 - холестирин
class ClientQuestion6Form(forms.Form):
    for_date = ClientQuestionForDate(6)
    question_title = QUESTIONS[6-1][1]

    # Ишемическая болезнь сердца
    form6_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №7
class ClientQuestion7Form(forms.Form):
    for_date = ClientQuestionForDate(7)
    question_title = QUESTIONS[7-1][1]

    # Заболевания сосудов головного мозга
    form7_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №8
class ClientQuestion8Form(forms.Form):
    for_date = ClientQuestionForDate(8)
    question_title = QUESTIONS[8-1][1]

    # Заболевания почек
    form8_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №9
class ClientQuestion9Form(forms.Form):
    for_date = ClientQuestionForDate(9)
    question_title = QUESTIONS[9-1][1]

    # Заболевания печени
    form9_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №10
class ClientQuestion10Form(forms.Form):
    for_date = ClientQuestionForDate(10)
    question_title = QUESTIONS[10-1][1]

    # Заболевания суставов
    form10_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №11
class ClientQuestion11Form(forms.Form):
    for_date = ClientQuestionForDate(11)
    question_title = QUESTIONS[11-1][1]

    # Заболевания суставов
    form11_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# вопрос №12
class ClientQuestion12Form(forms.Form):
    for_date = ClientQuestionForDate(12)
    question_title = QUESTIONS[12-1][1]

    # Заболевания позвоночника
    form12_date_of_the_last_visit = for_date.get_date_field_for_last_visit()
    quest_number = for_date.get_quest_number_from_hidden_field()


# **


class ClientFeedback(forms.Form):
    title = "Запись на прием к врачу"

    name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'client_feedback_name',
        'class': 'form-control',
        'placeholder': 'Ваше имя (только Русский буквы)',
        'max': 20,
        'required': ''}))

    surname = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'client_feedback_surname',
        'class': 'form-control',
        'placeholder': 'Ваша фамилия (только Русский буквы)',
        'max': 20,
        'required': ''}))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'client_feedback_phone',
        'class': 'form-control',
        'pattern': '^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$/',
        'required': ''}))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите комментарий (более подробно о вашей проблеме)',
        'rows': 6,
        'required': ''}))

    terms_conditions = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'value': 1}),
        required=True
    )
