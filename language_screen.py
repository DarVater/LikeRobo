from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.spinner import Spinner

from sistem import BackButton

# Example mapping of interface text to different languages



class LanguageData():
    text_map = {
        'Русский': {
            'mein_menu_title': 'Главное меню',
            'settings_title': 'Настройки',
            'bind_title': 'Загружать\n   навык',
            'run_round_title': 'Запустить раунд',
            'exit_title': 'Выход',
            'sentences_pair': {
                'PresentContinuous': {
                    '+': [
                        ['я работаю (состояние)', 'I am working', 'I am + V1+ing'],
                        ['Мы работаем (состояние)', 'We are working', 'We are + V1+ing'],
                        ['Они работают (состояние)', 'They are working', 'They are + V1+ing'],
                        ['Ты работаешь (состояние)', 'You are working', 'You are + V1+ing'],
                        ['Он работает (состояние)', 'He is working', 'He is + V1+ing'],
                        ['Она работает (состояние)', 'She is working', 'She is + V1+ing'],
                        ['Это работает (состояние)', 'It is working', 'It is + V1+ing'],
                    ],
                    '-': [
                        ['я не работаю (состояние)', 'I amn\'t working', 'I + am + V1+ing'],
                        ['Мы не работаем (состояние)', 'We aren\'t working', 'We + are + V1+ing'],
                        ['Они не работают (состояние)', 'They aren\'t working', 'They + are + V1+ing'],
                        ['Ты не работаешь (состояние)', 'You aren\'t working', 'You + are + V1+ing'],
                        ['Он не работает (состояние)', 'He isn\'t working', 'He + is + V1+ing'],
                        ['Она не работает (состояние)', 'She isn\'t working', 'She + is + V1+ing'],
                        ['Это не работает (состояние)', 'It isn\'t working', 'It + is + V1+ing'],
                    ],
                    '?': [
                        ['Я работаю? (состояние)', 'Am I working', 'Am I + V1+ing'],
                        ['Мы работаем? (состояние)', 'Are we working', 'Are we + V1+ing'],
                        ['Они работают? (состояние)', 'Are they working', 'Are they + V1+ing'],
                        ['Ты работаешь? (состояние)', 'Are you working', 'Are you + V1+ing'],
                        ['Он работает? (состояние)', 'Is he working', 'Is he + V1+ing'],
                        ['Она работает? (состояние)', 'Is she working', 'Is she + V1+ing'],
                        ['Это работает? (состояние)', 'Is it working', 'Is it + V1+ing'],
                    ],
                },
                'PastContinuous': {
                    '+': [
                        ['я работал (состояние)', 'I was working', 'I was + V1+ing'],
                        ['Мы работали (состояние)', 'We were working', 'We were + V1+ing'],
                        ['Они работали (состояние)', 'They were working', 'They were + V1+ing'],
                        ['Ты работал (состояние)', 'You were working', 'You were + V1+ing'],
                        ['Он работал (состояние)', 'He was working', 'He was + V1+ing'],
                        ['Она работала (состояние)', 'She was working', 'She was + V1+ing'],
                        ['Это работало (состояние)', 'It was working', 'It was + V1+ing'],
                    ],
                    '-': [
                        ['я не работал (состояние)', 'I wasn\'t working', 'I was +n\'t + V1+ing'],
                        ['Мы не работали (состояние)', 'We weren\'t working', 'We were +n\'t + V1+ing'],
                        ['Они не работали (состояние)', 'They weren\'t working', 'They were +n\'t + V1+ing'],
                        ['Ты не работал (состояние)', 'You weren\'t working', 'You were +n\'t + V1+ing'],
                        ['Он не работал (состояние)', 'He wasn\'t working', 'He was +n\'t + V1+ing'],
                        ['Она не работала (состояние)', 'She wasn\'t working', 'She was +n\'t + V1+ing'],
                        ['Это не работало (состояние)', 'It wasn\'t working', 'It was +n\'t + V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (состояние)', 'Was I working', 'Was I + V1+ing'],
                        ['Мы работали? (состояние)', 'Were we working', 'Were we + V1+ing'],
                        ['Они работали? (состояние)', 'Were they working', 'Were they + V1+ing'],
                        ['Ты работал? (состояние)', 'Were you working', 'Were you + V1+ing'],
                        ['Он работал? (состояние)', 'Was he working', 'Was he + V1+ing'],
                        ['Она работала? (состояние)', 'Was she working', 'Was she + V1+ing'],
                        ['Это работало? (состояние)', 'Was it working', 'Was it + V1+ing'],
                    ],
                },
                'FutureContinuous': {
                    '+': [
                        ['Я буду работать (состояние)', 'I will be working', 'I will be + V1+ing'],
                        ['Ты будешь работать (состояние)', 'You will be working', 'You will be + V1+ing'],
                        ['Они будут работать (состояние)', 'They will be working', 'They will be + V1+ing'],
                        ['Мы будем работать (состояние)', 'We will be working', 'We will be + V1+ing'],
                        ['Он будет работать (состояние)', 'He will be working', 'He will be + V1+ing'],
                        ['Она будет работать (состояние)', 'She will be working', 'She will be + V1+ing'],
                        ['Это будет работать (состояние)', 'It will be working', 'It will be + V1+ing'],
                    ],
                    '-': [
                        ['Я не буду работать (состояние)', 'I won\'t be working', 'I won\'t be + V1+ing'],
                        ['Ты не будешь работать (состояние)', 'You won\'t be working', 'You won\'t be + V1+ing'],
                        ['Они не будут работать (состояние)', 'They won\'t be working', 'They won\'t be + V1+ing'],
                        ['Мы не будем работать (состояние)', 'We won\'t be working', 'We won\'t be + V1+ing'],
                        ['Он не будет работать (состояние)', 'He won\'t be working', 'He won\'t be + V1+ing'],
                        ['Она не будет работать (состояние)', 'She won\'t be working', 'She won\'t be + V1+ing'],
                        ['Это не будет работать (состояние)', 'It won\'t be working', 'It won\'t be + V1+ing'],
                    ],
                    '?': [
                        ['Я буду работать? (состояние)', 'Will I be working', 'Will I be + V1+ing'],
                        ['Ты будешь работать? (состояние)', 'Will you be working', 'Will you be + V1+ing'],
                        ['Они будут работать? (состояние)', 'Will they be working', 'Will they be + V1+ing'],
                        ['Мы будем работать? (состояние)', 'Will we be working', 'Will we be + V1+ing'],
                        ['Он будет работать? (состояние)', 'Will he be working', 'Will he be + V1+ing'],
                        ['Она будет работать? (состояние)', 'Will she be working', 'Will she be + V1+ing'],
                        ['Это будет работать? (состояние)', 'Will it be working', 'Will it be + V1+ing'],
                    ],
                },

                'PresentIndefinite': {
                    '+': [
                        ['я работаю (повторяющееся)', 'I work', 'I + V1'],
                        ['Мы работаем (повторяющееся)', 'We work', 'We + V1'],
                        ['Они работают (повторяющееся)', 'They work', 'They + V1'],
                        ['Ты работаешь (повторяющееся)', 'You work', 'You + V1'],
                        ['Он работает (повторяющееся)', 'He works', 'He + V1+s'],
                        ['Она работает (повторяющееся)', 'She works', 'She + V1+s'],
                        ['Это работает (повторяющееся)', 'It works', 'It + V1+s'],
                    ],
                    '-': [
                        ['я не работаю (повторяющееся)', 'I don\'t work', 'I don\'t + V1'],
                        ['Мы не работаем (повторяющееся)', 'We don\'t work', 'We don\'t + V1'],
                        ['Они не работают (повторяющееся)', 'They don\'t work', 'They don\'t + V1'],
                        ['Ты не работаешь (повторяющееся)', 'You don\'t work', 'You don\'t + V1'],
                        ['Он не работает (повторяющееся)', 'He doesn\'t work', 'He doesn\'t + V1'],
                        ['Она не работает (повторяющееся)', 'She doesn\'t work', 'She doesn\'t + V1'],
                        ['Это не работает (повторяющееся)', 'It doesn\'t work', 'It doesn\'t + V1'],
                    ],
                    '?': [
                        ['я работаю? (повторяющееся)', 'Do I work', 'Do + I + V1'],
                        ['Мы работаем? (повторяющееся)', 'Do we work', 'Do + we + V1'],
                        ['Они работают? (повторяющееся)', 'Do they work', 'Do + they + V1'],
                        ['Ты работаешь? (повторяющееся)', 'Do you work', 'Do + you + V1'],
                        ['Он работает? (повторяющееся)', 'Does he work', 'Does + he + V1'],
                        ['Она работает? (повторяющееся)', 'Does she work', 'Does + she + V1'],
                        ['Это работает? (повторяющееся)', 'Does it work', 'Does + it + V1'],
                    ],
                },
                'PastIndefinite': {
                    '+': [
                        ['я работал (повторяющееся)', 'I worked', 'I + V2'],
                        ['Он работал (повторяющееся)', 'He worked', 'He + V2'],
                        ['Мы работали (повторяющееся)', 'We worked', 'We + V2'],
                        ['Они работали (повторяющееся)', 'They worked', 'They + V2'],
                        ['Ты работал (повторяющееся)', 'You worked', 'You + V2'],
                        ['Она работала (повторяющееся)', 'She worked', 'She + V2'],
                        ['Это работало (повторяющееся)', 'It worked', 'It + V2'],
                    ],
                    '-': [
                        ['Я не работал (повторяющееся)', 'I didn\'t work', 'I + didn\'t + V1'],
                        ['Мы не работали (повторяющееся)', 'We didn\'t work', 'We + didn\'t + V1'],
                        ['Они не работали (повторяющееся)', 'They didn\'t work', 'They + didn\'t + V1'],
                        ['Ты не работал (повторяющееся)', 'You didn\'t work', 'You + didn\'t + V1'],
                        ['Он не работал (повторяющееся)', 'He didn\'t work', 'He + didn\'t + V1'],
                        ['Она не работала (повторяющееся)', 'She didn\'t work', 'She + didn\'t + V1'],
                        ['Это не работало (повторяющееся)', 'It didn\'t work', 'It + didn\'t + V1'],
                    ],
                    '?': [
                        ['я работал? (повторяющееся)', 'Did I work', 'Did I + V1'],
                        ['Мы работали? (повторяющееся)', 'Did we work', 'Did we + V1'],
                        ['Они работали? (повторяющееся)', 'Did they work', 'Did they + V1'],
                        ['Ты работал? (повторяющееся)', 'Did you work', 'Did you + V1'],
                        ['Он работал? (повторяющееся)', 'Did he work', 'Did he + V1'],
                        ['Она работала? (повторяющееся)', 'Did she work', 'Did she + V1'],
                        ['Это работало? (повторяющееся)', 'Did it work', 'Did it + V1'],
                    ],
                },
                'FutureIndefinite': {
                    '+': [
                        ['Я буду работать (повторяющееся)', 'I will work', 'I will + V1'],
                        ['Мы будем работать (повторяющееся)', 'We will work', 'We will + V1'],
                        ['Они буду работать (повторяющееся)', 'They will work', 'They will + V1'],
                        ['Ты будешь работать (повторяющееся)', 'You will work', 'You will + V1'],
                        ['Он будет работать (повторяющееся)', 'He will work', 'He will + V1'],
                        ['Она будет работать (повторяющееся)', 'She will work', 'She will + V1'],
                        ['Это будет работать (повторяющееся)', 'It will work', 'It will + V1'],
                    ],
                    '-': [
                        ['Я не буду работать (повторяющееся)', 'I won\'t work', 'I won\'t + V1'],
                        ['Мы не будем работать (повторяющееся)', 'We won\'t work', 'We won\'t + V1'],
                        ['Они не буду работать (повторяющееся)', 'They won\'t work', 'They won\'t + V1'],
                        ['Ты не будешь работать (повторяющееся)', 'You won\'t work', 'You won\'t + V1'],
                        ['Он не будет работать (повторяющееся)', 'He won\'t work', 'He won\'t + V1'],
                        ['Она не будет работать (повторяющееся)', 'She won\'t work', 'She won\'t + V1'],
                        ['Это не будет работать (повторяющееся)', 'It won\'t work', 'It won\'t + V1'],
                    ],
                    '?': [
                        ['Я буду работать? (повторяющееся)', 'Will I work', 'Will I + V1'],
                        ['Мы будем работать? (повторяющееся)', 'Will we work', 'Will we + V1'],
                        ['Они буду работать? (повторяющееся)', 'Will they work', 'Will they + V1'],
                        ['Ты будешь работать? (повторяющееся)', 'Will you work', 'Will you + V1'],
                        ['Он будет работать? (повторяющееся)', 'Will he work', 'Will he + V1'],
                        ['Она будет работать? (повторяющееся)', 'Will she work', 'Will she + V1'],
                        ['Это будет работать? (повторяющееся)', 'Will it work', 'Will it + V1'],
                    ],
                },

                'PresentPerfect': {
                    '+': [
                        ['Я работал (есть опыт)', 'I have worked', 'I have V2'],
                        ['Мы работали (есть опыт)', 'We have worked', 'We have V2'],
                        ['Ты работал (есть опыт)', 'You have worked', 'You have V2'],
                        ['Они работали (есть опыт)', 'They have worked', 'They have V2'],
                        ['Он работал (есть опыт)', 'He has worked', 'He has V2'],
                        ['Она работала (есть опыт)', 'She has worked', 'She has V2'],
                        ['Это работало (есть опыт)', 'It has worked', 'It has V2'],
                    ],
                    '-': [
                        ['Я не работал (нет опыта)', 'I haven\'t worked', 'I haven\'t V2'],
                        ['Мы не работали (нет опыта)', 'We haven\'t worked', 'We haven\'t V2'],
                        ['Ты не работал (нет опыта)', 'You haven\'t worked', 'You haven\'t V2'],
                        ['Они не работали (нет опыта)', 'They haven\'t worked', 'They haven\'t V2'],
                        ['Он не работал (нет опыта)', 'He hasn\'t worked', 'He hasn\'t V2'],
                        ['Она не работала (нет опыта)', 'She hasn\'t worked', 'She hasn\'t V2'],
                        ['Это не работало (нет опыта)', 'It hasn\'t worked', 'It hasn\'t V2'],
                    ],
                    '?': [
                        ['Я работал? (есть опыт)', 'Have I worked', 'Have I V2'],
                        ['Мы работали? (есть опыт)', 'Have we worked', 'Have we V2'],
                        ['Ты работал? (есть опыт)', 'Have you worked', 'Have you V2'],
                        ['Они работали? (есть опыт)', 'Have they worked', 'Have they V2'],
                        ['Он работал? (есть опыт)', 'Has he worked', 'Has he V2'],
                        ['Она работала? (есть опыт)', 'Has she worked', 'Has she V2'],
                        ['Это работало? (есть опыт)', 'Has it worked', 'Has it V2'],
                    ],
                },
                'PastPerfect': {
                    '+': [
                        ['Я работал (позапрошлое)', 'I had worked', 'I had V2'],
                        ['Мы работали (позапрошлое)', 'We had worked', 'We had V2'],
                        ['Ты работал (позапрошлое)', 'You had worked', 'You had V2'],
                        ['Они работали (позапрошлое)', 'They had worked', 'They had V2'],
                        ['Он работал (позапрошлое)', 'He had worked', 'He had V2'],
                        ['Она работала (позапрошлое)', 'She had worked', 'She had V2'],
                        ['Это работало (позапрошлое)', 'It had worked', 'It had V2'],
                    ],
                    '-': [
                        ['Я не работал (позапрошлое)', 'I hadn\'t worked', 'I hadn\'t V2'],
                        ['Мы не работали (позапрошлое)', 'We hadn\'t worked', 'We hadn\'t V2'],
                        ['Ты не работал (позапрошлое)', 'You hadn\'t worked', 'You hadn\'t V2'],
                        ['Они не работали (позапрошлое)', 'They hadn\'t worked', 'They hadn\'t V2'],
                        ['Он не работал (позапрошлое)', 'He hadn\'t worked', 'He hadn\'t V2'],
                        ['Она не работала (позапрошлое)', 'She hadn\'t worked', 'She hadn\'t V2'],
                        ['Это не работало (позапрошлое)', 'It hadn\'t worked', 'It hadn\'t V2'],
                    ],
                    '?': [
                        ['Я работал? (позапрошлое)', 'Had I worked', 'Had I V2'],
                        ['Мы работали? (позапрошлое)', 'Had we worked', 'Had we V2'],
                        ['Ты работал? (позапрошлое)', 'Had you worked', 'Had you V2'],
                        ['Они работали? (позапрошлое)', 'Had they worked', 'Had they V2'],
                        ['Он работал? (позапрошлое)', 'Had he worked', 'Had he V2'],
                        ['Она работала? (позапрошлое)', 'Had she worked', 'Had she V2'],
                        ['Это работало? (позапрошлое)', 'Had it worked', 'Had it V2'],
                    ],
                },
                'FuturePerfect': {
                    '+': [
                        ['Я буду работать (к тому времени)', 'I will have worked', 'I will have V2'],
                        ['Мы будем работать (к тому времени)', 'We will have worked', 'We will have V2'],
                        ['Ты будешь работать (к тому времени)', 'You will have worked', 'You will have V2'],
                        ['Они буду работать (к тому времени)', 'They will have worked', 'They will have V2'],
                        ['Он будет работать (к тому времени)', 'He will have worked', 'He will have V2'],
                        ['Она будет работать (к тому времени)', 'She will have worked', 'She will have V2'],
                        ['Это будет работать (к тому времени)', 'It will have worked', 'It will have V2'],
                    ],
                    '-': [
                        ['Я не буду работать (к тому времени)', 'I won\'t have worked', 'I won\'t have V2'],
                        ['Мы не будем работать (к тому времени)', 'We won\'t have worked', 'We won\'t have V2'],
                        ['Ты не будешь работать (к тому времени)', 'You won\'t have worked', 'You won\'t have V2'],
                        ['Они не буду работать (к тому времени)', 'They won\'t have worked', 'They won\'t have V2'],
                        ['Он не будет работать (к тому времени)', 'He won\'t have worked', 'He won\'t have V2'],
                        ['Она не будет работать (к тому времени)', 'She won\'t have worked', 'She won\'t have V2'],
                        ['Это не будет работать (к тому времени)', 'It won\'t have worked', 'It won\'t have V2'],
                    ],
                    '?': [
                        ['Я буду работать? (к тому времени)', 'Will I have worked', 'Will I have V2'],
                        ['Мы будем работать? (к тому времени)', 'Will we have worked', 'Will we have V2'],
                        ['Ты будешь работать? (к тому времени)', 'Will you have worked', 'Will you have V2'],
                        ['Они буду работать? (к тому времени)', 'Will they have worked', 'Will they have V2'],
                        ['Он будет работать? (к тому времени)', 'Will he have worked', 'Will he have V2'],
                        ['Она будет работать? (к тому времени)', 'Will she have worked', 'Will she have V2'],
                        ['Это будет работать? (к тому времени)', 'Will it have worked', 'Will it have V2'],
                    ],
                },

                'PresentPerfectContinuous': {
                    '+': [
                        ['Я работал (длится по сейчас)', 'I have been working', 'I have been V1+ing'],
                        ['Мы работали (длится по сейчас)', 'We have been working', 'We have been V1+ing'],
                        ['Ты работал (длится по сейчас)', 'You have been working', 'You have been V1+ing'],
                        ['Они работали (длится по сейчас)', 'They have been working', 'They have been V1+ing'],
                        ['Он работал (длится по сейчас)', 'He has been working', 'He has been V1+ing'],
                        ['Она работала (длится по сейчас)', 'She has been working', 'She has been V1+ing'],
                        ['Это работало (длится по сейчас)', 'It has been working', 'It has been V1+ing'],
                    ],
                    '-': [
                        ['Я не работал (не длилось по сейчас)', 'I haven\'t been working', 'I haven\'t been V1+ing'],
                        ['Мы не работали (не длилось по сейчас)', 'We haven\'t been working', 'We haven\'t been V1+ing'],
                        ['Ты не работал (не длилось по сейчас)', 'You haven\'t been working', 'You haven\'t been V1+ing'],
                        ['Они не работали (не длилось по сейчас)', 'They haven\'t been working', 'They haven\'t been V1+ing'],
                        ['Он не работал (не длилось по сейчас)', 'He hasn\'t been working', 'He hasn\'t been V1+ing'],
                        ['Она не работала (не длилось по сейчас)', 'She hasn\'t been working', 'She hasn\'t been V1+ing'],
                        ['Это не работало (не длилось по сейчас)', 'It hasn\'t been working', 'It hasn\'t been V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (длится по сейчас)', 'Have I been working', 'Have I been V1+ing'],
                        ['Мы работали? (длится по сейчас)', 'Have we been working', 'Have we been V1+ing'],
                        ['Ты работал? (длится по сейчас)', 'Have you been working', 'Have you been V1+ing'],
                        ['Они работали? (длится по сейчас)', 'Have they been working', 'Have they been V1+ing'],
                        ['Он работал? (длится по сейчас)', 'Has he been working', 'Has he been V1+ing'],
                        ['Она работала? (длится по сейчас)', 'Has she been working', 'Has she been V1+ing'],
                        ['Это работало? (длится по сейчас)', 'Has it been working', 'Has it been V1+ing'],
                    ],
                },
                'PastPerfectContinuous': {
                    '+': [
                        ['Я работал (продолжительное прозапрошлое)', 'I had been working', 'I had been V1+ing'],
                        ['Мы работали (продолжительное прозапрошлое)', 'We had been working', 'We had been V1+ing'],
                        ['Ты работал (продолжительное прозапрошлое)', 'You had been working', 'You had been V1+ing'],
                        ['Они работали (продолжительное прозапрошлое)', 'They had been working', 'They had been V1+ing'],
                        ['Он работал (продолжительное прозапрошлое)', 'He had been working', 'He had been V1+ing'],
                        ['Она работала (продолжительное прозапрошлое)', 'She had been working', 'She had been V1+ing'],
                        ['Это работало (продолжительное прозапрошлое)', 'It had been working', 'It had been V1+ing'],
                    ],
                    '-': [
                        ['Я не работал (продолжительное прозапрошлое)', 'I hadn\'t been working', 'I hadn\'t been V1+ing'],
                        ['Мы не работали (продолжительное прозапрошлое)', 'We hadn\'t been working', 'We hadn\'t been V1+ing'],
                        ['Ты не работал (продолжительное прозапрошлое)', 'You hadn\'t been working', 'You hadn\'t been V1+ing'],
                        ['Они не работали (продолжительное прозапрошлое)', 'They hadn\'t been working', 'They hadn\'t been V1+ing'],
                        ['Он не работал (продолжительное прозапрошлое)', 'He hadn\'t been working', 'He hadn\'t been V1+ing'],
                        ['Она не работала (продолжительное прозапрошлое)', 'She hadn\'t been working', 'She hadn\'t been V1+ing'],
                        ['Это не работало (продолжительное прозапрошлое)', 'It hadn\'t been working', 'It hadn\'t been V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (продолжительное прозапрошлое)', 'Had I been working', 'Had I been V1+ing'],
                        ['Мы работали? (продолжительное прозапрошлое)', 'Had we been working', 'Had we been V1+ing'],
                        ['Ты работал? (продолжительное прозапрошлое)', 'Had you been working', 'Had you been V1+ing'],
                        ['Они работали? (продолжительное прозапрошлое)', 'Had they been working', 'Had they been V1+ing'],
                        ['Он работал? (продолжительное прозапрошлое)', 'Had he been working', 'Had he been V1+ing'],
                        ['Она работала? (продолжительное прозапрошлое)', 'Had she been working', 'Had she been V1+ing'],
                        ['Это работало? (продолжительное прозапрошлое)', 'Had it been working', 'Had it been V1+ing'],
                    ],
                },
                'FuturePerfectContinuous': {
                    '+': [
                        ['Я буду работающим (продолжительное будет длиться)', 'I will have been working', 'I will have been V1+ing'],
                        ['Мы будем работающими (продолжительное будет длиться)', 'We will have been working', 'We will have been V1+ing'],
                        ['Ты будешь работающим (продолжительное будет длиться)', 'You will have been working', 'You will have been V1+ing'],
                        ['Они будут работающими (продолжительное будет длиться)', 'They will have been working', 'They will have been V1+ing'],
                        ['Он будует работающим (продолжительное будет длиться)', 'He will have been working', 'He will have been V1+ing'],
                        ['Она будует работающей (продолжительное будет длиться)', 'She will have been working', 'She will have been V1+ing'],
                        ['Это будет работающим (продолжительное будет длиться)', 'It will have been working', 'It will have been V1+ing'],
                    ],
                    '-': [
                        ['Я не буду работающим  (продолжительное не будет длиться)', 'I won\'t have been working', 'I won\'t have been V1+ing'],
                        ['Мы не будем работающими  (продолжительное не будет длиться)', 'We won\'t have been working', 'We won\'t have been V1+ing'],
                        ['Ты не будешь работающим  (продолжительное не будет длиться)', 'You won\'t have been working', 'You won\'t have been V1+ing'],
                        ['Они не будут работающими  (продолжительное не будет длиться)', 'They won\'t have been working','They won\'t have been V1+ing'],
                        ['Он не будует работающим  (продолжительное не будет длиться)', 'He won\'t have been working', 'He won\'t have been V1+ing'],
                        ['Она не будует работающей  (продолжительное не будет длиться)', 'She won\'t have been working','She won\'t have been V1+ing'],
                        ['Это не будет работающим (продолжительное не будет длиться)', 'It won\'t have been working', 'It won\'t have been V1+ing'],
                    ],
                    '?': [
                        ['Я буду работающим? (продолжительное будет длиться)', 'Will I have been working', 'Will I have been V1+ing'],
                        ['Мы будем работающими? (продолжительное будет длиться)', 'Will we have been working', 'Will We have been V1+ing'],
                        ['Ты будешь работающим? (продолжительное будет длиться)', 'Will you have been working', 'Will You have been V1+ing'],
                        ['Они будут работающими? (продолжительное будет длиться)', 'Will they have been working', 'Will They have been V1+ing'],
                        ['Он будует работающим? (продолжительное будет длиться)', 'Will he have been working', 'Will He have been V1+ing'],
                        ['Она будует работающей? (продолжительное будет длиться)', 'Will she have been working', 'Will She have been V1+ing'],
                        ['Это будет работающим? (продолжительное будет длиться)', 'Will it have been working', 'Will It have been V1+ing'],
                    ],
                },
            }
        },
        'Украинский': {
            'mein_menu_title': 'Главне меню',
            'bind_title': 'Загружать\n навичку',
            'settings_title': 'Настройки',
            'run_round_title': 'Запустити раунд',
            'exit_title': 'Вихід',
            'sentences_pair': {
                'PresentContinuous': {
                    '+': [
                        ['я работаю (состояние)', 'I am working', 'I am + V1+ing'],
                        ['Мы работаем (состояние)', 'We are working', 'We are + V1+ing'],
                        ['Они работают (состояние)', 'They are working', 'They are + V1+ing'],
                        ['Ты работаешь (состояние)', 'You are working', 'You are + V1+ing'],
                        ['Он работает (состояние)', 'He is working', 'He is + V1+ing'],
                        ['Она работает (состояние)', 'She is working', 'She is + V1+ing'],
                        ['Это работает (состояние)', 'It is working', 'It is + V1+ing'],
                    ],
                    '-': [
                        ['я не работаю (состояние)', 'I amn\'t working', 'I + am + V1+ing'],
                        ['Мы не работаем (состояние)', 'We aren\'t working', 'We + are + V1+ing'],
                        ['Они не работают (состояние)', 'They aren\'t working', 'They + are + V1+ing'],
                        ['Ты не работаешь (состояние)', 'You aren\'t working', 'You + are + V1+ing'],
                        ['Он не работает (состояние)', 'He isn\'t working', 'He + is + V1+ing'],
                        ['Она не работает (состояние)', 'She isn\'t working', 'She + is + V1+ing'],
                        ['Это не работает (состояние)', 'It isn\'t working', 'It + is + V1+ing'],
                    ],
                    '?': [
                        ['Я работаю? (состояние)', 'Am I working', 'Am I + V1+ing'],
                        ['Мы работаем? (состояние)', 'Are we working', 'Are we + V1+ing'],
                        ['Они работают? (состояние)', 'Are they working', 'Are they + V1+ing'],
                        ['Ты работаешь? (состояние)', 'Are you working', 'Are you + V1+ing'],
                        ['Он работает? (состояние)', 'Is he working', 'Is he + V1+ing'],
                        ['Она работает? (состояние)', 'Is she working', 'Is she + V1+ing'],
                        ['Это работает? (состояние)', 'Is it working', 'Is it + V1+ing'],
                    ],
                },
                'PastContinuous': {
                    '+': [
                        ['я работал (состояние)', 'I was working', 'I was + V1+ing'],
                        ['Мы работали (состояние)', 'We were working', 'We were + V1+ing'],
                        ['Они работали (состояние)', 'They were working', 'They were + V1+ing'],
                        ['Ты работал (состояние)', 'You were working', 'You were + V1+ing'],
                        ['Он работал (состояние)', 'He was working', 'He was + V1+ing'],
                        ['Она работала (состояние)', 'She was working', 'She was + V1+ing'],
                        ['Это работало (состояние)', 'It was working', 'It was + V1+ing'],
                    ],
                    '-': [
                        ['я не работал (состояние)', 'I wasn\'t working', 'I was +n\'t + V1+ing'],
                        ['Мы не работали (состояние)', 'We weren\'t working', 'We were +n\'t + V1+ing'],
                        ['Они не работали (состояние)', 'They weren\'t working', 'They were +n\'t + V1+ing'],
                        ['Ты не работал (состояние)', 'You weren\'t working', 'You were +n\'t + V1+ing'],
                        ['Он не работал (состояние)', 'He wasn\'t working', 'He was +n\'t + V1+ing'],
                        ['Она не работала (состояние)', 'She wasn\'t working', 'She was +n\'t + V1+ing'],
                        ['Это не работало (состояние)', 'It wasn\'t working', 'It was +n\'t + V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (состояние)', 'Was I working', 'Was I + V1+ing'],
                        ['Мы работали? (состояние)', 'Were we working', 'Were we + V1+ing'],
                        ['Они работали? (состояние)', 'Were they working', 'Were they + V1+ing'],
                        ['Ты работал? (состояние)', 'Were you working', 'Were you + V1+ing'],
                        ['Он работал? (состояние)', 'Was he working', 'Was he + V1+ing'],
                        ['Она работала? (состояние)', 'Was she working', 'Was she + V1+ing'],
                        ['Это работало? (состояние)', 'Was it working', 'Was it + V1+ing'],
                    ],
                },
                'FutureContinuous': {
                    '+': [
                        ['Я буду работать (состояние)', 'I will be working', 'I will be + V1+ing'],
                        ['Ты будешь работать (состояние)', 'You will be working', 'You will be + V1+ing'],
                        ['Они будут работать (состояние)', 'They will be working', 'They will be + V1+ing'],
                        ['Мы будем работать (состояние)', 'We will be working', 'We will be + V1+ing'],
                        ['Он будет работать (состояние)', 'He will be working', 'He will be + V1+ing'],
                        ['Она будет работать (состояние)', 'She will be working', 'She will be + V1+ing'],
                        ['Это будет работать (состояние)', 'It will be working', 'It will be + V1+ing'],
                    ],
                    '-': [
                        ['Я не буду работать (состояние)', 'I won\'t be working', 'I won\'t be + V1+ing'],
                        ['Ты не будешь работать (состояние)', 'You won\'t be working', 'You won\'t be + V1+ing'],
                        ['Они не будут работать (состояние)', 'They won\'t be working', 'They won\'t be + V1+ing'],
                        ['Мы не будем работать (состояние)', 'We won\'t be working', 'We won\'t be + V1+ing'],
                        ['Он не будет работать (состояние)', 'He won\'t be working', 'He won\'t be + V1+ing'],
                        ['Она не будет работать (состояние)', 'She won\'t be working', 'She won\'t be + V1+ing'],
                        ['Это не будет работать (состояние)', 'It won\'t be working', 'It won\'t be + V1+ing'],
                    ],
                    '?': [
                        ['Я буду работать? (состояние)', 'Will I be working', 'Will I be + V1+ing'],
                        ['Ты будешь работать? (состояние)', 'Will you be working', 'Will you be + V1+ing'],
                        ['Они будут работать? (состояние)', 'Will they be working', 'Will they be + V1+ing'],
                        ['Мы будем работать? (состояние)', 'Will we be working', 'Will we be + V1+ing'],
                        ['Он будет работать? (состояние)', 'Will he be working', 'Will he be + V1+ing'],
                        ['Она будет работать? (состояние)', 'Will she be working', 'Will she be + V1+ing'],
                        ['Это будет работать? (состояние)', 'Will it be working', 'Will it be + V1+ing'],
                    ],
                },

                'PresentIndefinite': {
                    '+': [
                        ['я работаю (повторяющееся)', 'I work', 'I + V1'],
                        ['Мы работаем (повторяющееся)', 'We work', 'We + V1'],
                        ['Они работают (повторяющееся)', 'They work', 'They + V1'],
                        ['Ты работаешь (повторяющееся)', 'You work', 'You + V1'],
                        ['Он работает (повторяющееся)', 'He works', 'He + V1+s'],
                        ['Она работает (повторяющееся)', 'She works', 'She + V1+s'],
                        ['Это работает (повторяющееся)', 'It works', 'It + V1+s'],
                    ],
                    '-': [
                        ['я не работаю (повторяющееся)', 'I don\'t work', 'I don\'t + V1'],
                        ['Мы не работаем (повторяющееся)', 'We don\'t work', 'We don\'t + V1'],
                        ['Они не работают (повторяющееся)', 'They don\'t work', 'They don\'t + V1'],
                        ['Ты не работаешь (повторяющееся)', 'You don\'t work', 'You don\'t + V1'],
                        ['Он не работает (повторяющееся)', 'He doesn\'t work', 'He doesn\'t + V1'],
                        ['Она не работает (повторяющееся)', 'She doesn\'t work', 'She doesn\'t + V1'],
                        ['Это не работает (повторяющееся)', 'It doesn\'t work', 'It doesn\'t + V1'],
                    ],
                    '?': [
                        ['я работаю? (повторяющееся)', 'Do I work', 'Do + I + V1'],
                        ['Мы работаем? (повторяющееся)', 'Do we work', 'Do + we + V1'],
                        ['Они работают? (повторяющееся)', 'Do they work', 'Do + they + V1'],
                        ['Ты работаешь? (повторяющееся)', 'Do you work', 'Do + you + V1'],
                        ['Он работает? (повторяющееся)', 'Does he work', 'Does + he + V1'],
                        ['Она работает? (повторяющееся)', 'Does she work', 'Does + she + V1'],
                        ['Это работает? (повторяющееся)', 'Does it work', 'Does + it + V1'],
                    ],
                },
                'PastIndefinite': {
                    '+': [
                        ['я работал (повторяющееся)', 'I worked', 'I + V2'],
                        ['Он работал (повторяющееся)', 'He worked', 'He + V2'],
                        ['Мы работали (повторяющееся)', 'We worked', 'We + V2'],
                        ['Они работали (повторяющееся)', 'They worked', 'They + V2'],
                        ['Ты работал (повторяющееся)', 'You worked', 'You + V2'],
                        ['Она работала (повторяющееся)', 'She worked', 'She + V2'],
                        ['Это работало (повторяющееся)', 'It worked', 'It + V2'],
                    ],
                    '-': [
                        ['Я не работал (повторяющееся)', 'I didn\'t work', 'I + didn\'t + V1'],
                        ['Мы не работали (повторяющееся)', 'We didn\'t work', 'We + didn\'t + V1'],
                        ['Они не работали (повторяющееся)', 'They didn\'t work', 'They + didn\'t + V1'],
                        ['Ты не работал (повторяющееся)', 'You didn\'t work', 'You + didn\'t + V1'],
                        ['Он не работал (повторяющееся)', 'He didn\'t work', 'He + didn\'t + V1'],
                        ['Она не работала (повторяющееся)', 'She didn\'t work', 'She + didn\'t + V1'],
                        ['Это не работало (повторяющееся)', 'It didn\'t work', 'It + didn\'t + V1'],
                    ],
                    '?': [
                        ['я работал? (повторяющееся)', 'Did I work', 'Did I + V1'],
                        ['Мы работали? (повторяющееся)', 'Did we work', 'Did we + V1'],
                        ['Они работали? (повторяющееся)', 'Did they work', 'Did they + V1'],
                        ['Ты работал? (повторяющееся)', 'Did you work', 'Did you + V1'],
                        ['Он работал? (повторяющееся)', 'Did he work', 'Did he + V1'],
                        ['Она работала? (повторяющееся)', 'Did she work', 'Did she + V1'],
                        ['Это работало? (повторяющееся)', 'Did it work', 'Did it + V1'],
                    ],
                },
                'FutureIndefinite': {
                    '+': [
                        ['Я буду работать (повторяющееся)', 'I will work', 'I will + V1'],
                        ['Мы будем работать (повторяющееся)', 'We will work', 'We will + V1'],
                        ['Они буду работать (повторяющееся)', 'They will work', 'They will + V1'],
                        ['Ты будешь работать (повторяющееся)', 'You will work', 'You will + V1'],
                        ['Он будет работать (повторяющееся)', 'He will work', 'He will + V1'],
                        ['Она будет работать (повторяющееся)', 'She will work', 'She will + V1'],
                        ['Это будет работать (повторяющееся)', 'It will work', 'It will + V1'],
                    ],
                    '-': [
                        ['Я не буду работать (повторяющееся)', 'I won\'t work', 'I won\'t + V1'],
                        ['Мы не будем работать (повторяющееся)', 'We won\'t work', 'We won\'t + V1'],
                        ['Они не буду работать (повторяющееся)', 'They won\'t work', 'They won\'t + V1'],
                        ['Ты не будешь работать (повторяющееся)', 'You won\'t work', 'You won\'t + V1'],
                        ['Он не будет работать (повторяющееся)', 'He won\'t work', 'He won\'t + V1'],
                        ['Она не будет работать (повторяющееся)', 'She won\'t work', 'She won\'t + V1'],
                        ['Это не будет работать (повторяющееся)', 'It won\'t work', 'It won\'t + V1'],
                    ],
                    '?': [
                        ['Я буду работать? (повторяющееся)', 'Will I work', 'Will I + V1'],
                        ['Мы будем работать? (повторяющееся)', 'Will we work', 'Will we + V1'],
                        ['Они буду работать? (повторяющееся)', 'Will they work', 'Will they + V1'],
                        ['Ты будешь работать? (повторяющееся)', 'Will you work', 'Will you + V1'],
                        ['Он будет работать? (повторяющееся)', 'Will he work', 'Will he + V1'],
                        ['Она будет работать? (повторяющееся)', 'Will she work', 'Will she + V1'],
                        ['Это будет работать? (повторяющееся)', 'Will it work', 'Will it + V1'],
                    ],
                },

                'PresentPerfect': {
                    '+': [
                        ['Я работал (есть опыт)', 'I have worked', 'I have V2'],
                        ['Мы работали (есть опыт)', 'We have worked', 'We have V2'],
                        ['Ты работал (есть опыт)', 'You have worked', 'You have V2'],
                        ['Они работали (есть опыт)', 'They have worked', 'They have V2'],
                        ['Он работал (есть опыт)', 'He has worked', 'He has V2'],
                        ['Она работала (есть опыт)', 'She has worked', 'She has V2'],
                        ['Это работало (есть опыт)', 'It has worked', 'It has V2'],
                    ],
                    '-': [
                        ['Я не работал (нет опыта)', 'I haven\'t worked', 'I haven\'t V2'],
                        ['Мы не работали (нет опыта)', 'We haven\'t worked', 'We haven\'t V2'],
                        ['Ты не работал (нет опыта)', 'You haven\'t worked', 'You haven\'t V2'],
                        ['Они не работали (нет опыта)', 'They haven\'t worked', 'They haven\'t V2'],
                        ['Он не работал (нет опыта)', 'He hasn\'t worked', 'He hasn\'t V2'],
                        ['Она не работала (нет опыта)', 'She hasn\'t worked', 'She hasn\'t V2'],
                        ['Это не работало (нет опыта)', 'It hasn\'t worked', 'It hasn\'t V2'],
                    ],
                    '?': [
                        ['Я работал? (есть опыт)', 'Have I worked', 'Have I V2'],
                        ['Мы работали? (есть опыт)', 'Have we worked', 'Have we V2'],
                        ['Ты работал? (есть опыт)', 'Have you worked', 'Have you V2'],
                        ['Они работали? (есть опыт)', 'Have they worked', 'Have they V2'],
                        ['Он работал? (есть опыт)', 'Has he worked', 'Has he V2'],
                        ['Она работала? (есть опыт)', 'Has she worked', 'Has she V2'],
                        ['Это работало? (есть опыт)', 'Has it worked', 'Has it V2'],
                    ],
                },
                'PastPerfect': {
                    '+': [
                        ['Я работал (позапрошлое)', 'I had worked', 'I had V2'],
                        ['Мы работали (позапрошлое)', 'We had worked', 'We had V2'],
                        ['Ты работал (позапрошлое)', 'You had worked', 'You had V2'],
                        ['Они работали (позапрошлое)', 'They had worked', 'They had V2'],
                        ['Он работал (позапрошлое)', 'He had worked', 'He had V2'],
                        ['Она работала (позапрошлое)', 'She had worked', 'She had V2'],
                        ['Это работало (позапрошлое)', 'It had worked', 'It had V2'],
                    ],
                    '-': [
                        ['Я не работал (позапрошлое)', 'I hadn\'t worked', 'I hadn\'t V2'],
                        ['Мы не работали (позапрошлое)', 'We hadn\'t worked', 'We hadn\'t V2'],
                        ['Ты не работал (позапрошлое)', 'You hadn\'t worked', 'You hadn\'t V2'],
                        ['Они не работали (позапрошлое)', 'They hadn\'t worked', 'They hadn\'t V2'],
                        ['Он не работал (позапрошлое)', 'He hadn\'t worked', 'He hadn\'t V2'],
                        ['Она не работала (позапрошлое)', 'She hadn\'t worked', 'She hadn\'t V2'],
                        ['Это не работало (позапрошлое)', 'It hadn\'t worked', 'It hadn\'t V2'],
                    ],
                    '?': [
                        ['Я работал? (позапрошлое)', 'Had I worked', 'Had I V2'],
                        ['Мы работали? (позапрошлое)', 'Had we worked', 'Had we V2'],
                        ['Ты работал? (позапрошлое)', 'Had you worked', 'Had you V2'],
                        ['Они работали? (позапрошлое)', 'Had they worked', 'Had they V2'],
                        ['Он работал? (позапрошлое)', 'Had he worked', 'Had he V2'],
                        ['Она работала? (позапрошлое)', 'Had she worked', 'Had she V2'],
                        ['Это работало? (позапрошлое)', 'Had it worked', 'Had it V2'],
                    ],
                },
                'FuturePerfect': {
                    '+': [
                        ['Я буду работать (к тому времени)', 'I will have worked', 'I will have V2'],
                        ['Мы будем работать (к тому времени)', 'We will have worked', 'We will have V2'],
                        ['Ты будешь работать (к тому времени)', 'You will have worked', 'You will have V2'],
                        ['Они буду работать (к тому времени)', 'They will have worked', 'They will have V2'],
                        ['Он будет работать (к тому времени)', 'He will have worked', 'He will have V2'],
                        ['Она будет работать (к тому времени)', 'She will have worked', 'She will have V2'],
                        ['Это будет работать (к тому времени)', 'It will have worked', 'It will have V2'],
                    ],
                    '-': [
                        ['Я не буду работать (к тому времени)', 'I won\'t have worked', 'I won\'t have V2'],
                        ['Мы не будем работать (к тому времени)', 'We won\'t have worked', 'We won\'t have V2'],
                        ['Ты не будешь работать (к тому времени)', 'You won\'t have worked', 'You won\'t have V2'],
                        ['Они не буду работать (к тому времени)', 'They won\'t have worked', 'They won\'t have V2'],
                        ['Он не будет работать (к тому времени)', 'He won\'t have worked', 'He won\'t have V2'],
                        ['Она не будет работать (к тому времени)', 'She won\'t have worked', 'She won\'t have V2'],
                        ['Это не будет работать (к тому времени)', 'It won\'t have worked', 'It won\'t have V2'],
                    ],
                    '?': [
                        ['Я буду работать? (к тому времени)', 'Will I have worked', 'Will I have V2'],
                        ['Мы будем работать? (к тому времени)', 'Will we have worked', 'Will we have V2'],
                        ['Ты будешь работать? (к тому времени)', 'Will you have worked', 'Will you have V2'],
                        ['Они буду работать? (к тому времени)', 'Will they have worked', 'Will they have V2'],
                        ['Он будет работать? (к тому времени)', 'Will he have worked', 'Will he have V2'],
                        ['Она будет работать? (к тому времени)', 'Will she have worked', 'Will she have V2'],
                        ['Это будет работать? (к тому времени)', 'Will it have worked', 'Will it have V2'],
                    ],
                },

                'PresentPerfectContinuous': {
                    '+': [
                        ['Я работал (длится по сейчас)', 'I have been working', 'I have been V1+ing'],
                        ['Мы работали (длится по сейчас)', 'We have been working', 'We have been V1+ing'],
                        ['Ты работал (длится по сейчас)', 'You have been working', 'You have been V1+ing'],
                        ['Они работали (длится по сейчас)', 'They have been working', 'They have been V1+ing'],
                        ['Он работал (длится по сейчас)', 'He has been working', 'He has been V1+ing'],
                        ['Она работала (длится по сейчас)', 'She has been working', 'She has been V1+ing'],
                        ['Это работало (длится по сейчас)', 'It has been working', 'It has been V1+ing'],
                    ],
                    '-': [
                        ['Я не работал (не длилось по сейчас)', 'I haven\'t been working', 'I haven\'t been V1+ing'],
                        ['Мы не работали (не длилось по сейчас)', 'We haven\'t been working', 'We haven\'t been V1+ing'],
                        ['Ты не работал (не длилось по сейчас)', 'You haven\'t been working', 'You haven\'t been V1+ing'],
                        ['Они не работали (не длилось по сейчас)', 'They haven\'t been working', 'They haven\'t been V1+ing'],
                        ['Он не работал (не длилось по сейчас)', 'He hasn\'t been working', 'He hasn\'t been V1+ing'],
                        ['Она не работала (не длилось по сейчас)', 'She hasn\'t been working', 'She hasn\'t been V1+ing'],
                        ['Это не работало (не длилось по сейчас)', 'It hasn\'t been working', 'It hasn\'t been V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (длится по сейчас)', 'Have I been working', 'Have I been V1+ing'],
                        ['Мы работали? (длится по сейчас)', 'Have we been working', 'Have we been V1+ing'],
                        ['Ты работал? (длится по сейчас)', 'Have you been working', 'Have you been V1+ing'],
                        ['Они работали? (длится по сейчас)', 'Have they been working', 'Have they been V1+ing'],
                        ['Он работал? (длится по сейчас)', 'Has he been working', 'Has he been V1+ing'],
                        ['Она работала? (длится по сейчас)', 'Has she been working', 'Has she been V1+ing'],
                        ['Это работало? (длится по сейчас)', 'Has it been working', 'Has it been V1+ing'],
                    ],
                },
                'PastPerfectContinuous': {
                    '+': [
                        ['Я работал (продолжительное прозапрошлое)', 'I had been working', 'I had been V1+ing'],
                        ['Мы работали (продолжительное прозапрошлое)', 'We had been working', 'We had been V1+ing'],
                        ['Ты работал (продолжительное прозапрошлое)', 'You had been working', 'You had been V1+ing'],
                        ['Они работали (продолжительное прозапрошлое)', 'They had been working', 'They had been V1+ing'],
                        ['Он работал (продолжительное прозапрошлое)', 'He had been working', 'He had been V1+ing'],
                        ['Она работала (продолжительное прозапрошлое)', 'She had been working', 'She had been V1+ing'],
                        ['Это работало (продолжительное прозапрошлое)', 'It had been working', 'It had been V1+ing'],
                    ],
                    '-': [
                        ['Я не работал (продолжительное прозапрошлое)', 'I hadn\'t been working', 'I hadn\'t been V1+ing'],
                        ['Мы не работали (продолжительное прозапрошлое)', 'We hadn\'t been working', 'We hadn\'t been V1+ing'],
                        ['Ты не работал (продолжительное прозапрошлое)', 'You hadn\'t been working', 'You hadn\'t been V1+ing'],
                        ['Они не работали (продолжительное прозапрошлое)', 'They hadn\'t been working', 'They hadn\'t been V1+ing'],
                        ['Он не работал (продолжительное прозапрошлое)', 'He hadn\'t been working', 'He hadn\'t been V1+ing'],
                        ['Она не работала (продолжительное прозапрошлое)', 'She hadn\'t been working', 'She hadn\'t been V1+ing'],
                        ['Это не работало (продолжительное прозапрошлое)', 'It hadn\'t been working', 'It hadn\'t been V1+ing'],
                    ],
                    '?': [
                        ['Я работал? (продолжительное прозапрошлое)', 'Had I been working', 'Had I been V1+ing'],
                        ['Мы работали? (продолжительное прозапрошлое)', 'Had we been working', 'Had we been V1+ing'],
                        ['Ты работал? (продолжительное прозапрошлое)', 'Had you been working', 'Had you been V1+ing'],
                        ['Они работали? (продолжительное прозапрошлое)', 'Had they been working', 'Had they been V1+ing'],
                        ['Он работал? (продолжительное прозапрошлое)', 'Had he been working', 'Had he been V1+ing'],
                        ['Она работала? (продолжительное прозапрошлое)', 'Had she been working', 'Had she been V1+ing'],
                        ['Это работало? (продолжительное прозапрошлое)', 'Had it been working', 'Had it been V1+ing'],
                    ],
                },
                'FuturePerfectContinuous': {
                    '+': [
                        ['Я буду работающим (продолжительное будет длиться)', 'I will have been working', 'I will have been V1+ing'],
                        ['Мы будем работающими (продолжительное будет длиться)', 'We will have been working', 'We will have been V1+ing'],
                        ['Ты будешь работающим (продолжительное будет длиться)', 'You will have been working', 'You will have been V1+ing'],
                        ['Они будут работающими (продолжительное будет длиться)', 'They will have been working', 'They will have been V1+ing'],
                        ['Он будует работающим (продолжительное будет длиться)', 'He will have been working', 'He will have been V1+ing'],
                        ['Она будует работающей (продолжительное будет длиться)', 'She will have been working', 'She will have been V1+ing'],
                        ['Это будет работающим (продолжительное будет длиться)', 'It will have been working', 'It will have been V1+ing'],
                    ],
                    '-': [
                        ['Я не буду работающим  (продолжительное не будет длиться)', 'I won\'t have been working', 'I won\'t have been V1+ing'],
                        ['Мы не будем работающими  (продолжительное не будет длиться)', 'We won\'t have been working', 'We won\'t have been V1+ing'],
                        ['Ты не будешь работающим  (продолжительное не будет длиться)', 'You won\'t have been working', 'You won\'t have been V1+ing'],
                        ['Они не будут работающими  (продолжительное не будет длиться)', 'They won\'t have been working','They won\'t have been V1+ing'],
                        ['Он не будует работающим  (продолжительное не будет длиться)', 'He won\'t have been working', 'He won\'t have been V1+ing'],
                        ['Она не будует работающей  (продолжительное не будет длиться)', 'She won\'t have been working','She won\'t have been V1+ing'],
                        ['Это не будет работающим (продолжительное не будет длиться)', 'It won\'t have been working', 'It won\'t have been V1+ing'],
                    ],
                    '?': [
                        ['Я буду работающим? (продолжительное будет длиться)', 'Will I have been working', 'Will I have been V1+ing'],
                        ['Мы будем работающими? (продолжительное будет длиться)', 'Will we have been working', 'Will We have been V1+ing'],
                        ['Ты будешь работающим? (продолжительное будет длиться)', 'Will you have been working', 'Will You have been V1+ing'],
                        ['Они будут работающими? (продолжительное будет длиться)', 'Will they have been working', 'Will They have been V1+ing'],
                        ['Он будует работающим? (продолжительное будет длиться)', 'Will he have been working', 'Will He have been V1+ing'],
                        ['Она будует работающей? (продолжительное будет длиться)', 'Will she have been working', 'Will She have been V1+ing'],
                        ['Это будет работающим? (продолжительное будет длиться)', 'Will it have been working', 'Will It have been V1+ing'],
                    ],
                },
            }
        }
    }
    languages = ['Украинский', 'Русский']
    selected_language = 'Русский'

    def update_language(self, text):
        self.selected_language = text

    def get_text_from_map(self, title):
        return self.text_map[self.selected_language][title]

    def get_sentences_pair(self):
        return self.text_map[self.selected_language]['sentences_pair']

class LanguageScreen(Screen):
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.spinner = Spinner(
            text=lang_data.selected_language,
            values=lang_data.languages,
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.add_widget(self.spinner)
        self.add_back_btn()

    def update_language(self):
        self.lang_data.selected_language = self.spinner.text
        self.screen_manager.rebuild(self.spinner.text)

    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.99, 'top': 0.99})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)


    def goto_main(self, instance):
        self.update_language()
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'
