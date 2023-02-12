from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window

from sistem import BackButton, StartButton


class RoadmapScreen(Screen):
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source='imgs/background_statistic.png', allow_stretch=True, keep_ratio=False))
        self.indicator_grid = GridLayout(rows=25, row_default_height=20, row_force_default=True,
                                                size_hint=[0.2, .2],
                                                pos_hint={'center_x':  0.9, 'center_y': 0.65})
        # for i in range(20):
        #     self.indicator_grid.add_widget(Button(text='Indicator %d' % (i + 1),
        #                                  size_hint=[0.1, .2], width = 30))
        #     if (i+1) % 4 == 0:
        #         self.indicator_grid.add_widget(Label(text=''))

        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.add_widget(self.indicator_grid)
        self.add_back_btn()
        self.add_start_btn()
    def add_start_btn(self): # .3, .05
        self.button = Button(background_normal='imgs/start_road_btn_normal.png',
                             background_down='imgs/start_road_btn_down.png', size=(140, 40),
            size_hint=[None, None], pos_hint={'center_x': 0.5, 'center_y': 0.18})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.95, 'top': 0.90})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'
