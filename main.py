from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

from language_screen import LanguageScreen, LanguageData
from roadmap_screen import RoadmapScreen
from flash_card import FlashCardScreen
from mode_screen import ModeScreen

Window.size = (500, 1000)
# add repid button to result screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        global lang_data
        super().__init__(**kwargs)
        self.add_widget(Image(source='imgs/background.png', allow_stretch=True, keep_ratio=False))
        button_grid = GridLayout(cols=1, size_hint=(0.3, 0.5), pos_hint={'right': 1, 'center_y': 0.5}, orientation='rl-bt')
        button1 = Button(text="Road Map")
        button1.bind(on_press=self.goto_screen2)

        button2 = Button(text=lang_data.get_text_from_map(title='bind_title'))
        button2.bind(on_press=self.goto_screen3)

        button3 = Button(text=lang_data.get_text_from_map('settings_title'))
        button3.bind(on_press=self.goto_screen4)

        button_grid.add_widget(Button(text=lang_data.get_text_from_map('exit_title')
                                      , on_press=self.exit_app))
        button_grid.add_widget(button3)
        button_grid.add_widget(button2)
        button_grid.add_widget(button1)
        self.add_widget(button_grid)

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
    global lang_data, store
    screen_manager.clear_widgets()
    lang_data.update_language(selected_language)
    store.put('app_data', selected_language=selected_language, road_map=app_data['road_map'])
    create_widget_screens()

def create_widget_screens():
    screen_manager.add_widget(LanguageScreen(lang_data, screen_manager, name='screen4'))
    screen_manager.add_widget(MainScreen(name='screen1'))
    screen_manager.add_widget(RoadmapScreen(lang_data, screen_manager, name='screen2'))
    screen_manager.add_widget(FlashCardScreen(lang_data, screen_manager, name='screen3'))
    screen_manager.add_widget(ModeScreen(lang_data, screen_manager, name='mode_screen'))

store = JsonStore('mystore.json')
if 'app_data' in store:
    app_data = store.get('app_data')
    selected_language = app_data['selected_language']
else:
    store.put('app_data', selected_language='Русский', road_map={})
    selected_language = 'Русский'

lang_data = LanguageData()
lang_data.update_language(selected_language)
create_widget_screens()
screen_manager.current = 'screen1'

screen_manager.rebuild = screen_manager_rebuild


class MyApp(App):
    def build(self):

        return screen_manager

if __name__ == '__main__':
    MyApp().run()
