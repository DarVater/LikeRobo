from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
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
        self.mode_grid = GridLayout(rows=25, size=Window.size, size_hint=(.8, .8),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.485})

        self.add_widget(Image(source='imgs/background_mode.png', allow_stretch=True, keep_ratio=False))
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
                    self.tense_type1 = ToggleButton( border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_simple_normal.png',
                                      background_down='imgs/toogle_simple_down.png',
                        text='', group='tense_type', state='down')
                    self.tense_type.add_widget(self.tense_type1)
                    self.tense_type2 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_continuous_normal.png',
                                      background_down='imgs/toogle_continuous_down.png')
                    self.tense_type.add_widget(self.tense_type2)
                    self.tense_type3 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_perfect_normal.png',
                                      background_down='imgs/toogle_perfect_down.png')
                    self.tense_type.add_widget(self.tense_type3)
                    self.tense_type4 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_perfect_continuous_normal.png',
                                      background_down='imgs/toogle_perfect_continuous_down.png')
                    self.tense_type.add_widget(self.tense_type4)
                self.group1.add_widget(self.tense_type)
                self.sentence_type = GridLayout(cols=33)
                if 1:  # sentence type
                    self.sentence_type.add_widget(Label(size_hint=[.5, 1]))
                    self.sentence_type1 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_positive_normal.png',
                              background_down='imgs/toogle_positive_down.png', state='down')
                    self.sentence_type.add_widget(self.sentence_type1)
                    self.sentence_type2 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_question_normal.png',
                                      background_down='imgs/toogle_question_down.png')
                    self.sentence_type.add_widget(self.sentence_type2)
                    self.sentence_type3 = ToggleButton( border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_negative_normal.png',
                                      background_down='imgs/toogle_negative_down.png')
                    self.sentence_type.add_widget(self.sentence_type3)
                    self.sentence_type.add_widget(Label(size_hint=[.5, 1]))
                self.group1.add_widget(self.sentence_type)

                self.sentence_time = GridLayout(cols=33)
                if 1:  # sentence time
                    self.sentence_time.add_widget(Label(size_hint=[.5, 1]))
                    self.tense1 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_present_normal.png',
                                      background_down='imgs/toogle_present_down.png', state='down' )
                    self.sentence_time.add_widget(self.tense1)
                    self.tense2 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_future_normal.png',
                                      background_down='imgs/toogle_future_down.png')
                    self.sentence_time.add_widget(self.tense2)
                    self.tense3 = ToggleButton(border=(0, 0, 0, 0),
                                      background_normal='imgs/toogle_past_normal.png',
                                      background_down='imgs/toogle_past_down.png')
                    self.sentence_time.add_widget(self.tense3)
                    self.sentence_time.add_widget(Label(size_hint=[.5, 1]))
                self.group1.add_widget(self.sentence_time)

            self.mode_grid.add_widget(self.group1)


    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.99, 'top': 0.99},
                                  border=(0, 0, 0, 0),)
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def add_run_round_btn(self):
        self.button = Button(border=(0, 0, 0, 0),
                                      background_normal='imgs/start_road_btn_normal.png',
                                      background_down='imgs/start_road_btn_down.png',
                                     size_hint=[.3, .05],
                                     pos_hint={'center_x': 0.5, 'center_y': .05})
        self.button.bind(on_press=self.run_round)
        self.add_widget(self.button)


    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'

    def run_round(self, instance):
        print(self.tense_type1.state)
        ans = ''
        if self.tense_type1.state =='down':
            ans += 'i'
        if self.tense_type2.state =='down':
            ans += 'c'
        if self.tense_type3.state =='down':
            ans += 'p'
        if self.tense_type4.state =='down':
            ans += 'PC'

        if self.sentence_type1.state =='down':
            ans += '+'
        if self.sentence_type2.state =='down':
            ans += '?'
        if self.sentence_type3.state =='down':
            ans += '-'

        if self.tense1.state =='down':
            ans += 'NT'
        if self.tense2.state =='down':
            ans += 'FT'
        if self.tense3.state =='down':
            ans += 'PT'
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.get_screen('screen2').wait_progress = False
        self.screen_manager.get_screen('screen3').ids['fcs'].choose_a_deck(ans)
        self.screen_manager.current = 'screen3'
