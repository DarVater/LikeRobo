from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.animation import Animation

from sistem import BackButton, StartButton


class RoadmapScreen(Screen):
    road_points = { 'i': [  'NTi+',    'NTi-',    'NTi?',    'NTi',
                            'PTi+',    'PTi-',    'PTi?',    'PTi',
                            'FTi+',    'FTi-',    'FTi?',    'FTi',
                            'i+',    'i-',    'i?',    'i'],
                    'c': [  'NTc+',    'NTc-',    'NTc?',    'NTc',
                            'PTc+',    'PTc-',    'PTc?',    'PTc',
                            'FTc+',    'FTc-',    'FTc?',    'FTc',
                            'c+',    'c-',    'c?',   'c'
                            ],
                    'p': [  'pNT+',    'pNT-',    'pNT?',    'pNT',
                            'pPT+',    'pPT-',    'pPT?',    'pPT',
                            'pFT+',    'pFT-',    'pFT?',    'pFT',
                            'p+',    'p-',    'p?',    'p'
                            ],
                    'PC': [ 'PCNT+',    'PCNT-',    'PCNT?',    'PCNT',
                            'PCPT+',    'PCPT-',    'PCPT?',    'PCPT',
                            'PCFT+',    'PCFT-',    'PCFT?',    'PCFT',
                            'PC+',    'PC-',    'PC?',    'PC'
                            ],
                    '':    ['+', '-', '?',  ''
                            ]
    }
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.aim = ''
        self.aim_types = ''
        ['road_map_data']
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        self.add_widget(Image(source='imgs/background_statistic.png', allow_stretch=True, keep_ratio=False))
        self.add_indicators()
        self.add_back_btn()
        self.add_start_btn()
        self.wait_progress = False

    def put_to_store(self, road_map_data):
        store = JsonStore('mystore.json')
        app_data = store.get('app_data')
        store.put('app_data', selected_language=app_data['selected_language'], road_map=road_map_data)

    def get_store(self):
        store = JsonStore('mystore.json')
        app_data = store.get('app_data')
        return app_data['road_map']

    def save_progress(self):
        if self.wait_progress:
            self.road_map_data[self.aim] = True
            self.put_to_store(self.road_map_data)
        self.add_indicators()
    def add_indicators(self):
        road_map_data = self.get_store()
        if road_map_data == {}:
            for point_types in self.road_points:
                for point in self.road_points[point_types]:
                    road_map_data[point] = False
            self.put_to_store(road_map_data)
        self.road_map_data = self.get_store()
        self.indicator_grid = GridLayout(rows=25, size_hint=[0.07, 0.58],
                                         pos_hint={'center_x': 0.90, 'center_y': 0.45})
        self.add_widget(self.indicator_grid)
        self.write_indicators()
        self.wait_progress = False

    def write_indicators(self):
        aim = ''
        for point_types in ['i', 'c', 'p', 'PC', '']:
            if point_types == 'p':
                indicator_types = GridLayout(cols=4, size_hint=[0.25, 0.31])
            else:
                indicator_types = GridLayout(cols=4, size_hint=[0.25, 0.25])
            self.indicator_grid.add_widget(indicator_types)
            for point in self.road_points[point_types]:
                if self.road_map_data[point] == False:
                    if aim == '':
                        aim = point
                        self.aim_types = point_types
                    imb_indicator = 'imgs/indicator.png'
                else:
                    imb_indicator = 'imgs/indicator_passed.png'
                result_widget = Image(source=imb_indicator, allow_stretch=True, keep_ratio=False,
                                      size_hint=(1, 1),
                                   )
                indicator_types.add_widget(result_widget)
                if '+' not in point and '-' not in point and '?' not in point:
                    for i in range(4):
                        indicator_types.add_widget(Label(text='', size_hint=(1, 1),
                                               pos_hint={'top': 1, 'center_x': 0.5}))
            if point_types == '':
                for i in range(11):
                    indicator_types.add_widget(Label(text='', size_hint=(1, 3),
                                           pos_hint={'top': 1, 'center_x': 0.5}))
            if point_types == 'p':
                for i in range(4):
                    indicator_types.add_widget(Label(text='', size_hint=(1, 3),
                                           pos_hint={'top': 1, 'center_x': 0.5}))
            indicator_types.add_widget(Label(text='', size_hint=(1, 3),
                                       pos_hint={'top': 1, 'center_x': 0.5}))
        self.aim = aim

    def add_start_btn(self):
        self.button = Button(background_normal='imgs/start_road_btn_normal.png', border=(0, 0, 0, 0),
                             background_down='imgs/start_road_btn_down.png',
                            size_hint=[0.2, 0.04], pos_hint={'center_x': 0.5, 'center_y': 0.18})
        self.button.bind(on_release=self.goto_round, on_press=self.screen_manager.play_start)
        self.add_widget(self.button)

    def add_back_btn(self):
        self.button = BackButton(size_hint=[.2, .1], size=(80, 80), pos_hint={'right': 0.95, 'top': 0.90})
        self.button.bind( on_press=self.screen_manager.play_button, on_release=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'

    def goto_round(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.wait_progress = True
        self.screen_manager.get_screen('screen3').ids['fcs'].choose_a_deck(self.aim)
        self.screen_manager.current = 'screen3'
