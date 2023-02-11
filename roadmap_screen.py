from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.animation import Animation


class RoadmapScreen(Screen):
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source='imgs/roadmap_background.png', allow_stretch=True, keep_ratio=False))
        self.indicator_grid = GridLayout(rows=25, row_default_height=20, row_force_default=True,
                                                size_hint=[0.2, .2],
                                                pos_hint={'center_x':  0.9, 'center_y': 0.65})
        for i in range(20):
            self.indicator_grid.add_widget(Button(text='Indicator %d' % (i + 1),
                                         size_hint=[0.1, .2], width = 30))
            if (i+1) % 4 == 0:
                self.indicator_grid.add_widget(Label(text=''))

        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.add_widget(self.indicator_grid)
        self.add_back_btn()
        self.add_widget(Label(text='Roadmap', font_size='30sp',
                             pos_hint={'center_x':  0.2, 'center_y': 0.87}))

    def add_back_btn(self):
        self.button = Button(text=self.lang_data.get_text_from_map('mein_menu_title'),
                             size_hint=[1, .1],
                             pos_hint={'right': 1, 'top': 1})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'
