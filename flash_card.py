import random
import time

from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.animation import Animation
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import Rotate
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from sistem import BackButton, get_media_lvl


class FlashCardScreen(Screen):
    temp_aim = ''
    round_sentences = []
    sentences_pair = {}
    viewing_card = []
    failed_cards = []
    all_mistakes_count = 0
    start_time = time.time()
    passed_cards = 0

    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.round_sentences = [['Они не будут работающими  (продолжительное не будет длиться)',
                                 'hey won\'t have been working']]
        self.deck_for_repeat = self.round_sentences.copy()
        self.viewing_card = self.get_random_place()
        self.flash_card = FlashCard(self.viewing_card)
        self.add_widget(self.flash_card)
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.x = 0
        self.y = 0
        self.add_back_btn()

    def choose_a_deck(self, aim):
        self.temp_aim = aim
        self.sentences_pair = self.lang_data.get_sentences_pair()
        self.round_sentences = []
        if 'FT' not in aim and 'NT' not in aim and 'PT' not in aim:
            aim += 'FTNTPT'
        if '+' not in aim and '-' not in aim and '?' not in aim:
            aim += '+-?'
        if 'i' not in aim and 'c' not in aim and 'p' not in aim and 'PC' not in aim:
            aim += 'icpPC'
        if 'i' in aim:
            self.chose_tense_type('Indefinite', aim)
        if 'c' in aim:
            self.chose_tense_type('Continuous', aim)
        if 'p' in aim:
            self.chose_tense_type('Perfect', aim)
        if 'PC' in aim:
            self.chose_tense_type('PerfectContinuous', aim)
        self.deck_for_repeat = self.round_sentences.copy()
        self.viewing_card = self.get_random_place()
        self.passed_cards = 0
        self.all_mistakes_count = 0
        self.start_time = time.time()
        self.next_card()

    def card_was_failed(self):
        self.failed_cards.append(self.viewing_card)

    def load_old_deck(self):
        self.round_sentences = self.deck_for_repeat.copy()
        self.viewing_card = self.get_random_place()
        self.clear_widgets()
        self.flash_card = FlashCard(self.viewing_card)
        self.add_widget(self.flash_card)
        self.start_time = time.time()
        self.passed_cards = 0
        self.all_mistakes_count = 0

    def get_random_place(self):
        place = self.round_sentences[random.randint(0, len(self.round_sentences) - 1)]
        index = self.round_sentences.index(place)
        place = self.round_sentences[index]
        self.round_sentences.pop(index)
        return place

    def chose_tense_type(self, some_sentences_pair, aim):
        if 'NT' in aim:
            self.get_tense_type(self.sentences_pair['Present' + some_sentences_pair], aim)
        if 'PT' in aim:
            self.get_tense_type(self.sentences_pair['Past' + some_sentences_pair], aim)
        if 'FT' in aim:
            self.get_tense_type(self.sentences_pair['Future' + some_sentences_pair], aim)

    def get_tense_type(self, some_sentences_pair, aim):
        if '+' in aim:
            for s in some_sentences_pair['+']:
                self.round_sentences.append(s)
        if '-' in aim:
            for s in some_sentences_pair['-']:
                self.round_sentences.append(s)
        if '?' in aim:
            for s in some_sentences_pair['?']:
                self.round_sentences.append(s)

    def next_card(self, animation='', rotate=''):
        self.passed_cards += 1
        self.x = 0
        self.y = self.width * 2
        self.clear_widgets()
        self.flash_card = FlashCard(self.viewing_card)
        self.add_widget(self.flash_card)
        self.add_back_btn()
        animation = Animation(y=0, duration=0.1)
        animation.start(self)
        if len(self.round_sentences) > 0:
            self.viewing_card = self.get_random_place()
        elif len(self.failed_cards):
            self.all_mistakes_count += len(self.failed_cards)
            for f_cards in self.failed_cards:
                self.round_sentences.append(f_cards)
            self.failed_cards = []
            self.viewing_card = self.get_random_place()
        else:
            pass_time = round(time.time() - self.start_time, 1)
            result_screen = ResultsCard(self.lang_data,
                                        self.screen_manager,
                                        self.all_mistakes_count,
                                        pass_time,
                                        self.passed_cards)
            self.clear_widgets()
            self.add_widget(result_screen)

    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.99, 'top': 0.99})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'
class FlashCard(FloatLayout, DragBehavior):

    def __init__(self, viewing_card,  **kwargs):
        super().__init__(**kwargs)
        self.viewing_card = viewing_card

        self.front = self.create_new_card('fleshcard_new.png', self.adapt_text(viewing_card[0], 20))
        self.back = self.create_new_card('fleshcard_know.png', self.adapt_text(viewing_card[1], 20))
        self.fail = self.create_new_card('fleshcard_fail.png', '')
        self.add_widget(self.front)
        self.is_back_card = False

    def adapt_text(self, text, max_sing):
        new_text = ''
        sing_pass = 0

        for row in text.split('('):
            if len(new_text) != 0:
                new_text += '\n('
            for word in row.split(' '):
                sing_pass += len(word)
                if max_sing < sing_pass:
                    sing_pass = 0
                    new_text += '\n'
                new_text += ' ' + word
                print(new_text)
        if '(\n ' in new_text:
            new_text = new_text.replace('(\n ', '(')
        return new_text

    def create_new_card(self, src, text):
        result_widget = Image(source='imgs/'+src, allow_stretch=True, keep_ratio=False, size_hint=(0.8, 0.8),
                           pos_hint={'center_x': 0.9, 'center_y': 0.9})

        result_widget.add_widget(Label(text=text, font_size='20sp', size_hint=(1, 1),
                                    pos=[Window.size[0]/2.5, Window.size[1]/3]))
        with result_widget.canvas.before:
            PushMatrix()
            result_widget.rot = Rotate()
            result_widget.rot.angle = 0
            result_widget.rot.origin = [Window.size[0]/2, Window.size[1]/2]
            result_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            result_widget.rot.axis = (0, 0, 1)
        with result_widget.canvas.after:
            PopMatrix()
        return result_widget

    def on_touch_down(self, touch):
        touch.touch_down_x = touch.x
        if self.collide_point(*touch.pos):

            # if the touch collides with our widget, let's grab it
            touch.grab(self)

            # and accept the touch.
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            if touch.x > touch.touch_down_x:
                if self.is_back_card:
                    animation = Animation(x=(self.parent.width + self.width), duration=0.1)
                    animation.bind(on_complete=self.parent.next_card)
                    animation.start(self.parent)
                else:
                    # Shift to the left
                    animation = Animation(angle=-360, duration=0.1)
                    animation.bind(on_complete=self.change_card_side)
                    animation.start(self.front.rot)
                    self.is_back_card = True

            elif touch.x < touch.touch_down_x:

                self.clear_widgets()
                self.add_widget(self.fail)
                # self.rot.angle -= 20
                # Shift to the right
                self.parent.card_was_failed()
                animation = Animation(x=-1*(self.parent.width + self.width), duration=0.1)
                animation.bind(on_complete=self.parent.next_card)
                animation.start(self.parent)
            touch.ungrab(self)

            return 1
        return super().on_touch_up(touch)

    def change_card_side(self, animation, rotate):
        self.clear_widgets()
        self.add_widget(self.back)


class ResultsCard(Screen):

    def __init__(self, lang_data, screen_manager, mistakes, pass_time, passed_cards,  **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        result_widget = Image(source='imgs/background_result.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(result_widget)
        self.result_grid = GridLayout(rows=25, size=Window.size, size_hint=(.5, .170),
                                         pos_hint={'center_x': 0.56, 'center_y': 0.305})
        self.add_widget(self.result_grid)
        self.passed_cards = Label(text=str(passed_cards), font_size='15sp')
        self.result_grid.add_widget(self.passed_cards)
        self.mistakes = Label(text=str(mistakes), font_size='15sp')
        self.result_grid.add_widget(self.mistakes)
        self.round_result = round(pass_time / (passed_cards - mistakes), 1)
        if self.round_result < 3:
            self.time_color = (115, 43, 93)
            self.continue_btn()
            self.screen_manager.get_screen('screen2').save_progress()
        else:
            self.time_color = (10, 84, 89)
            self.repeat_btn()
        self.passed_cards = Label(text=str(self.round_result), color=self.time_color, font_size='15sp')
        self.result_grid.add_widget(self.passed_cards)
        self.add_back_btn()

    def continue_btn(self):

        self.continue_button = Button(size_hint=[.42, .055], border=(0, 0, 0, 0),
                                      background_normal='imgs/continue_normal.png',
                                      background_down='imgs/continue_down.png',
                                      pos_hint={'center_x': 0.50, 'top': 0.185})
        self.continue_button.bind(on_press=self.continue_road_map)
        self.add_widget(self.continue_button)

    def repeat_btn(self):
        self.continue_button = Button(size_hint=[.42, .055], border=(0, 0, 0, 0),
                                      background_normal='imgs/repeat_normal.png',
                                      background_down='imgs/repeat_down.png',
                                      pos_hint={'center_x': 0.50, 'top': 0.185})
        self.continue_button.bind(on_press=self.repeat_deck)

        self.add_widget(self.continue_button)

    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.90, 'top': 0.95},
                                  border=(0, 0, 0, 0),)
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'

    def repeat_deck(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.parent.load_old_deck()

    def continue_road_map(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen2'

