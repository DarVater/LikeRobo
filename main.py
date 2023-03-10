from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

from language_screen import LanguageScreen, LanguageData
from roadmap_screen import RoadmapScreen
from flash_card import FlashWrapperScreen
from mode_screen import ModeScreen
from kivy.config import Config

Config.set('kivy','window_icon','imgs/icon.png')

# Window.size = (500, 1000)
# add repid button to result screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        global lang_data
        super().__init__(**kwargs)
        self.add_widget(Image(source='imgs/background_main.png', allow_stretch=True, keep_ratio=False))
        self.button_grid = GridLayout(cols=1, size_hint=(0.35, 0.23), pos_hint={'center_x': 0.5, 'center_y': 0.16}, orientation='rl-bt')
        self.add_button_to_screen(lang_data.get_text_from_map(title='exit_title'), self.exit_app)
        self.add_button_to_screen(lang_data.get_text_from_map(title='settings_title'), self.goto_screen4)
        self.add_button_to_screen(lang_data.get_text_from_map(title='mode_title'), self.goto_screen3)
        self.add_button_to_screen(lang_data.get_text_from_map(title='campaign_title'), self.goto_screen2)
        self.add_widget(self.button_grid)

    def add_button_to_screen(self, title, foo):
        button2 = Button(border=(0, 0, 0, 0), text='[color=000]'+title+'[/color]', font_size='17sp',
                                      background_normal='imgs/main_button_normal.png', markup=True,
                                      background_down='imgs/main_button_down.png',)
        button2.bind(on_press=foo)
        self.button_grid.add_widget(button2)

    def goto_screen2(self, instance):
        screen_manager.current = 'screen2'

    def goto_screen3(self, instance):
        screen_manager.current = 'mode_screen'

    def goto_screen4(self, instance):
        screen_manager.current = 'screen4'

    def exit_app(self, instance):
        App.get_running_app().stop()

screen_manager = ScreenManager()

def screen_manager_rebuild(selected_language):
    global app_data, store
    screen_manager.clear_widgets()
    lang_data.update_language(selected_language)
    store.put('app_data', selected_language=selected_language, road_map=app_data['road_map'])
    create_widget_screens()

def create_widget_screens():
    screen_manager.add_widget(LanguageScreen(lang_data, screen_manager, name='screen4'))
    screen_manager.add_widget(MainScreen(name='screen1'))
    screen_manager.add_widget(RoadmapScreen(lang_data, screen_manager, name='screen2'))
    screen_manager.add_widget(FlashWrapperScreen(lang_data, screen_manager, name='screen3'))
    screen_manager.add_widget(ModeScreen(lang_data, screen_manager, name='mode_screen'))

store = JsonStore('mystore.json')
if 'app_data' in store:
    app_data = store.get('app_data')
    selected_language = app_data['selected_language']
else:
    store.put('app_data', selected_language='??????????????', road_map={})
    app_data = store.get('app_data')
    selected_language = '??????????????'

lang_data = LanguageData()
lang_data.update_language(selected_language)
create_widget_screens()
screen_manager.current = 'screen1'

screen_manager.rebuild = screen_manager_rebuild


class MyApp(App):
    def build(self):
        self.icon = 'imgs/icon.png'
        self.loaded = 'imgs/background_main.png'
        return screen_manager

if __name__ == '__main__':
    MyApp().run()
