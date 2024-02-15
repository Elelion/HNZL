from datetime import datetime, timedelta
from typing import Final

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from Project_Dj_hnzlru import settings
from home.forms import *
from home.notification_codes import NOTIFICATION_CODES
from patients.models import COPDPatients


# TODO: сделать в дальнейшем выводы из БД!!!
class HomeListView(ListView):
    model = COPDPatients
    context_object_name = 'COPDPatients'
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        portfolio_numbers = [
            'gallery-1.jpg',
            'gallery-2.jpg',
            'gallery-3.jpg',
            'gallery-4.jpg',
            'gallery-5.jpg',
            'gallery-6.jpg',
        ]

        context['portfolio_numbers'] = portfolio_numbers
        return context


class ClientQuestions(TemplateView):
    CURRENT_DATE: Final = datetime.now().date()
    template_name = 'home/client_questions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # получаем номер запроса который должен прийти и в зависимости от
        # запроса рендерим форму
        if self.request.GET.get('quest_number') is None:
            quest_number = 1
        else:
            quest_number = int(self.request.GET.get('quest_number'))

        context['form'] = self._get_forms(str(quest_number))
        context['quest_number'] = quest_number
        context['questions'] = QUESTIONS

        return context

    def post(self, request, *args, **kwargs):
        question_handlers = {
            1: self._handle_quest1,
            2: self._handle_quest2,
            3: self._handle_quest3,
            4: self._handle_quest4,
            5: self._handle_quest5,
            6: self._handle_quest6,
            7: self._handle_quest7,
            8: self._handle_quest8,
            9: self._handle_quest9,
            10: self._handle_quest10,
            11: self._handle_quest11,
            12: self._handle_quest12,
        }

        if 'user_answers' not in request.session:
            request.session['user_answers'] = {}

        for quest_number, handler in question_handlers.items():
            if quest_number == int(request.POST['quest_number']):  # 1, 2,... n
                handler(request, quest_number)
                break

        # **

        # Перенаправление на следующий вопрос
        next_quest_number = int(quest_number) + 1

        if next_quest_number > len(QUESTIONS):
            # конец опроса, переход на результат
            return HttpResponseRedirect(reverse('home:client_results'))
        else:
            # идем дальше по вопросам
            return HttpResponseRedirect(reverse(
                'home:client_questions') + f'?quest_number={next_quest_number}')

    # **

    # Возвращает класс формы в зависимости от номера вопроса
    def _get_forms(self, form_number):
        form_list = {
            '1': ClientQuestion1Form(),
            '2': ClientQuestion2Form(),
            '3': ClientQuestion3Form(),
            '4': ClientQuestion4Form(),
            '5': ClientQuestion5Form(),
            '6': ClientQuestion6Form(),
            '7': ClientQuestion7Form(),
            '8': ClientQuestion8Form(),
            '9': ClientQuestion9Form(),
            '10': ClientQuestion10Form(),
            '11': ClientQuestion11Form(),
            '12': ClientQuestion12Form(),
        }

        return form_list.get(form_number, forms.Form)

    # **

    # рассчет ИМТ (веса)
    def _handle_quest1(self, request, quest_number):
        height = request.POST['form1_height']
        weight = request.POST['form1_weight']

        # рассчитываем индекс массы тела (пример: 185/88 => 88/1,85^2=25.7)
        # True: bmi > 30 and False: bmi <= 30
        height_in_meters = int(height) / 100  # Преобразуем высоту в метры
        body_mass_index = int(weight) / (height_in_meters ** 2)
        bmi = round(body_mass_index, 1)  # один знак после запятой

        # session
        request.session['user_answers'][quest_number] = f'{bmi}/{height}/{weight}'
        request.session.save()

    # рассчет АТ (давления: blood pressure)
    def _handle_quest2(self, request, quest_number):
        up_pressure = int(request.POST['form2_max'])
        down_pressure = int(request.POST['form2_min'])

        request.session['user_answers'][quest_number] = f'{up_pressure}/{down_pressure}'
        request.session.save()

    # холестирин
    def _handle_quest3(self, request, quest_number):
        cholesterol = float(request.POST['form3_cholesterol'])

        request.session['user_answers'][quest_number] = cholesterol
        request.session.save()

    # глюкоза
    def _handle_quest4(self, request, quest_number):
        glucose = float(request.POST['form4_glucose'])

        request.session['user_answers'][quest_number] = glucose
        request.session.save()

    # онкология
    def _handle_quest5(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 5)

    # ишемия
    def _handle_quest6(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 6)

    # сосуды головного мозга
    def _handle_quest7(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 7)

    # заболевания почек
    def _handle_quest8(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 8)

    # заболевания печени
    def _handle_quest9(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 9)

    # заболевания суставов
    def _handle_quest10(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 10)

    # Заболевания щитовидной железы
    def _handle_quest11(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 11)

    # Заболевания позвоночника
    def _handle_quest12(self, request, quest_number):
        self._last_visit_calculate(request, quest_number, 12)

    # **

    def _last_visit_calculate(self, request, quest_number, form_number):
        last_visit_str = request.POST[f'form{form_number}_date_of_the_last_visit']
        last_visit = datetime.strptime(last_visit_str, '%Y-%m-%d').date()
        time_difference_in_days = abs((self.CURRENT_DATE - last_visit).days)

        request.session['user_answers'][quest_number] = time_difference_in_days
        request.session.save()


class ClientResults(TemplateView):
    ALERT_OK: Final = '[Ок]'
    ALERT_PROBLEM: Final = '[Есть проблемы]'
    CURRENT_DATE: Final = datetime.now().date()

    results = {}

    template_name = 'home/client_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self._processing_results(self.request.session['user_answers'])

        context['form_feedback'] = ClientFeedback()
        context['user_answers'] = self.results
        context['questions'] = QUESTIONS

        return context

    def _processing_results(self, user_answers):
        self.results.clear()

        check_processings = {
            1: self._check_processing1,
            2: self._check_processing2,
            3: self._check_processing3,
            4: self._check_processing4,
            5: self._check_processing5,
            6: self._check_processing6,
            7: self._check_processing7,
            8: self._check_processing8,
            9: self._check_processing9,
            10: self._check_processing10,
            11: self._check_processing11,
            12: self._check_processing12,
        }

        for key_answer, val_answer in user_answers.items():
            for key_question, val_question in QUESTIONS:
                if int(key_answer) == int(key_question):
                    # TODO: рбочий код - не ктрогать пока что !!!
                    # print(val_question, val_answer)
                    # self.results[val_question] = val_answer

                    for number, processing in check_processings.items():
                        if number == int(key_answer):
                            self.results[val_question] = processing(val_answer)
                            break

    # **

    def _check_processing1(self, value):
        BMI_MAX = 30.0
        val_str = str(value)
        bmi, height, weight = val_str.split('/')

        bmi = float(bmi)
        height = int(height)
        weight = int(weight)

        if bmi >= BMI_MAX:
            return f'индекс {bmi}, при росте {height}, весе {weight} {self.ALERT_PROBLEM}'
        else:
            return f'индекс {bmi}, при росте {height}, весе {weight} {self.ALERT_OK}'

    def _check_processing2(self, value):
        BP_UP_MAX = 140
        BP_DOWN_MIN = 90

        val_str = str(value)
        up_pressure_str, down_pressure_str = val_str.split('/')

        up_pressure = int(up_pressure_str)
        down_pressure = int(down_pressure_str)

        if up_pressure >= BP_UP_MAX or down_pressure >= BP_DOWN_MIN:
            return f'{val_str} {self.ALERT_PROBLEM}'
        else:
            return f'{val_str} {self.ALERT_OK}'

    def _check_processing3(self, value):
        CHOLESTEROL_MAX = 5.2
        val = float(value)

        if val > CHOLESTEROL_MAX:
            return f'{val} {self.ALERT_PROBLEM}'
        else:
            return f'{val} {self.ALERT_OK}'

    def _check_processing4(self, value):
        GLUCOSE_MAX = 6.2
        val = float(value)

        if val > GLUCOSE_MAX:
            return f'{val} {self.ALERT_PROBLEM}'
        else:
            return f'{val} {self.ALERT_OK}'

    def _check_processing5(self, value):
        return self._last_visit_calculate(value)

    def _check_processing6(self, value):
        return self._last_visit_calculate(value)

    def _check_processing7(self, value):
        return self._last_visit_calculate(value)

    def _check_processing8(self, value):
        return self._last_visit_calculate(value)

    def _check_processing9(self, value):
        return self._last_visit_calculate(value)

    def _check_processing10(self, value):
        return self._last_visit_calculate(value)

    def _check_processing11(self, value):
        return self._last_visit_calculate(value)

    def _check_processing12(self, value):
        return self._last_visit_calculate(value)

    # **

    def _last_visit_calculate(self, value):
        months_ago = 6 * 30
        val = int(value)
        month_ago = round(val/30, 1)

        date_of_visit = self.CURRENT_DATE - timedelta(days=val)

        if val > months_ago:
            return f'визит {val} дн. назад ({month_ago} мес), от {date_of_visit} {self.ALERT_PROBLEM}'
        else:
            return f'визит {val} дн. назад ({month_ago} мес), от {date_of_visit} {self.ALERT_OK}'


def send_email_health_check(request):
    if request.method == 'POST':
        form = ClientFeedback(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            user_answers = request.POST['user_answers']

            send_mail('Заявка с сайта hnzl.ru',
                      'Новая заявка с сайта:\n\n'
                      f'Имя: {name}\n'
                      f'Фамилия: {surname}\n'
                      f'Телефон: {phone}\n'
                      f'Сообщение: {message}\n\n'
                      f'{user_answers}',
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_RECIPIENT_1],
                      fail_silently=False)

            return HttpResponseRedirect(reverse(
                'home:notification',
                args=('mail_success',)
            ))


def notification(request, code):
    icon_html = ''
    message = ''
    sub_message = ''

    for key, val in NOTIFICATION_CODES.items():
        if key == code:
            icon_html, message, sub_message = val.split('|')

    context = {
        'icon_html': icon_html,
        'message': message,
        'sub_message': sub_message,
    }

    return render(request, 'home/notification.html', context)
