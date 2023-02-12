from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

from sistem import BackButton


class ModeScreen(Screen):
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.tense_type1 = None
        self.tense_type2 = None
        self.tense_type3 = None
        self.tense_type4 = None
        self.tense_type5 = None
        self.sentence_type1 = None
        self.sentence_type2 = None
        self.sentence_type3 = None
        self.sentence_type4 = None
        self.tense1 = None
        self.tense2 = None
        self.tense3 = None
        self.tense4 = None
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.mode_grid = GridLayout(rows=25, size=Window.size, size_hint=(.8, .5),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_back_btn()
        self.add_mode()
        self.add_run_round_btn()
        self.add_widget(self.mode_grid)

    def add_mode(self):
        if 1:  # mode
            self.group1 = GridLayout(rows=33)
            if 1:  # tense type and form
                self.tense_type = GridLayout(cols=33)
                if 1:  # tense type
                    self.tense_type1 = ToggleButton(text='Simple', group='tense_type', state='down')
                    self.tense_type.add_widget(self.tense_type1)
                    self.tense_type2 = ToggleButton(text='Continues', group='tense_type')
                    self.tense_type.add_widget(self.tense_type2)
                    self.tense_type3 = ToggleButton(text='Perfect', group='tense_type')
                    self.tense_type.add_widget(self.tense_type3)
                    self.tense_type4 = ToggleButton(text='PerfectContinues', group='tense_type')
                    self.tense_type.add_widget(self.tense_type4)
                    self.tense_type5 = ToggleButton(text='ALL', group='tense_type')
                    self.tense_type.add_widget(self.tense_type5)
                self.group1.add_widget(self.tense_type)
                self.sentence_type = GridLayout(cols=33)
                if 1:  # sentence type
                    self.sentence_type1 = ToggleButton(text='+', group='type' , state='down')
                    self.sentence_type.add_widget(self.sentence_type1)
                    self.sentence_type2 = ToggleButton(text='?', group='type')
                    self.sentence_type.add_widget(self.sentence_type2)
                    self.sentence_type3 = ToggleButton(text='-', group='type')
                    self.sentence_type.add_widget(self.sentence_type3)
                    self.sentence_type4 = ToggleButton(text='ALL', group='type')
                    self.sentence_type.add_widget(self.sentence_type4)
                self.group1.add_widget(self.sentence_type)

                self.sentence_time = GridLayout(cols=33)
                if 1:  # sentence time
                    self.tense1 = ToggleButton(text='Present', group='tense', state='down' )
                    self.sentence_time.add_widget(self.tense1)
                    self.tense2 = ToggleButton(text='Future', group='tense')
                    self.sentence_time.add_widget(self.tense2)
                    self.tense3 = ToggleButton(text='Past', group='tense' )
                    self.sentence_time.add_widget(self.tense3)
                    self.tense4 = ToggleButton(text='ALL', group='tense' )
                    self.sentence_time.add_widget(self.tense4)
                self.group1.add_widget(self.sentence_time)

            self.mode_grid.add_widget(self.group1)


    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.99, 'top': 0.99})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def add_run_round_btn(self):
        self.button = Button(text=self.lang_data.get_text_from_map('run_round_title'),
                             size_hint=[1, .1],
                             pos_hint={'right': 1, 'bottom': 1})
        self.button.bind(on_press=self.run_round)
        self.add_widget(self.button)


    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'

    def run_round(self, instance):
        print(self.tense_type1.state)
        ans = ''
        if self.tense_type5.state =='down':
            ans += 'icpPC'
        else:
            if self.tense_type1.state =='down':
                ans += 'i'
            if self.tense_type2.state =='down':
                ans += 'c'
            if self.tense_type3.state =='down':
                ans += 'p'
            if self.tense_type4.state =='down':
                ans += 'PC'

        if self.sentence_type4.state =='down':
            ans += '+-?'
        else:
            if self.sentence_type1.state =='down':
                ans += '+'
            if self.sentence_type2.state =='down':
                ans += '?'
            if self.sentence_type3.state =='down':
                ans += '-'
        if self.tense4.state =='down':
            ans += 'FTNTPT'
        else:
            if self.tense1.state =='down':
                ans += 'NT'
            if self.tense2.state =='down':
                ans += 'FT'
            if self.tense3.state =='down':
                ans += 'PT'
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.get_screen('screen3').choose_a_deck(ans)
        self.screen_manager.current = 'screen3'
