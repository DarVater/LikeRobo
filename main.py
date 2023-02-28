from kivmob import KivMob, RewardedListenerInterface, TestIds
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform

from language_screen import LanguageScreen, LanguageData
from roadmap_screen import RoadmapScreen
from flash_card import FlashWrapperScreen
from mode_screen import ModeScreen
from kivy.config import Config

test_ads = True

Config.set('kivy','window_icon','imgs/icon.png')

if platform != "android":
    Window.size = (500, 1000)
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
                            background_down='imgs/main_button_down.png', on_release=foo,
                            on_press=screen_manager.play_button)

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

sound = None
def start_play_start(df=''):
    return start_play('start')
def start_play_wrong(df=''):
    return start_play('wrong')
def start_play_rotate(df=''):
    return start_play('rotate')
def start_play_right(df=''):
    return start_play('right')

def start_play_button(df=''):
    return start_play('button')

def start_play_lose(df=''):
    return start_play('lose')
def start_play_won(df=''):
    return start_play('won')

def start_play_toggle(df=''):
    return start_play('toggle')

def start_play(file):
    global sound
    source = 'songs/' + file + '.mp3'
    if sound:
        sound.stop()
    sound = SoundLoader.load(source)
    if sound:
        return sound.play()
    else:
        print('Dont find' + source)

screen_manager.play_button = start_play_button
screen_manager.play_toggle = start_play_toggle
screen_manager.play_start = start_play_start
screen_manager.play_wrong = start_play_wrong
screen_manager.play_rotate = start_play_rotate
screen_manager.play_right = start_play_right
screen_manager.play_won = start_play_won
screen_manager.play_lose = start_play_lose


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
    store.put('app_data', selected_language='Русский', road_map={})
    app_data = store.get('app_data')
    selected_language = 'Русский'

lang_data = LanguageData()
lang_data.update_language(selected_language)
create_widget_screens()
screen_manager.current = 'screen1'


if test_ads != True:
    screen_manager.ads_ids = {
        'APP': 'ca-app-pub-9906169229834445~1570037277',
        'BANNER': 'ca-app-pub-9906169229834445/6439220570',
        'REWARDED_VIDEO': 'ca-app-pub-9906169229834445/9364437240'
    }
else:
    screen_manager.ads_ids = {
        'APP': TestIds.APP,
        'BANNER': TestIds.BANNER,
        'REWARDED_VIDEO': TestIds.REWARDED_VIDEO
    }

screen_manager.rebuild = screen_manager_rebuild
if platform == "android":
    screen_manager.ads = None

class MyApp(App):
    def build(self):
        if platform == "android":
            screen_manager.ads = KivMob(screen_manager.ads_ids['APP'])
            # self.ads.new_banner(TestIds.BANNER)
            # self.ads.request_banner()
            # self.ads.show_banner()
            screen_manager.ads.load_rewarded_ad(screen_manager.ads_ids['REWARDED_VIDEO'])
            screen_manager.ads.set_rewarded_ad_listener(RewardedListenerInterface())
        self.icon = 'imgs/icon.png'
        self.loaded = 'imgs/background_main.png'
        return screen_manager

    def on_resume(self):
        if platform == "android":
            self.ads.load_rewarded_ad(screen_manager.ads_ids['REWARDED_VIDEO'])

if __name__ == '__main__':
    MyApp().run()
# from kivmob import KivMob, TestIds, RewardedListenerInterface
#
# from kivy.app import App
# from kivy.uix.button import Button
#
# class RewardedVideoTest(App):
#     """ Display a rewarded video ad on button release.
#     """
#
#     def build(self):
#         self.ads = KivMob(TestIds.APP)
#         self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)
#         # Add any callback functionality to this class.
#         self.ads.set_rewarded_ad_listener(RewardedListenerInterface())
#         return Button(text='Show Rewarded Ad',
#                       on_release=lambda a:self.ads.show_rewarded_ad())
#
#     def on_resume(self):
#         self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)
#
# if __name__ == "__main__":
#     RewardedVideoTest().run()
