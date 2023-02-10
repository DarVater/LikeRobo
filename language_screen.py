from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.spinner import Spinner


# Example mapping of interface text to different languages



class LanguageScreen(Screen):
    text_map = {
        'Русский': {
            'mein_menu_title': 'Главное меню',
            'settings_title': 'Настройки',
            'bind_title': 'Загружать\n   навык',
            'exit_title': 'Выход',
        },
        'Украинский': {
            'mein_menu_title': 'Главне меню',
            'bind_title': 'Загружать\n навичку',
            'settings_title': 'Настройки',
            'exit_title': 'Вихід',
        }
    }

    languages = ['Украинский', 'Русский']
    selected_language = 'Русский'
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.spinner = Spinner(
            text=self.selected_language,
            values=self.languages,
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        self.screen_manager = screen_manager
        self.add_back_btn()
        self.add_widget(self.spinner)

    def update_language(self):
        self.selected_language = self.spinner.text
        self.screen_manager.rebuild()

    def add_back_btn(self):
        self.button = Button(text=self.get_text_from_map('mein_menu_title'),
                             size_hint=[1, .1],
                             pos_hint={'right': 1, 'top': 1})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def get_text_from_map(self, title):
        return self.text_map[self.selected_language][title]

    def goto_main(self, instance):
        self.update_language()
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        self.screen_manager.current = 'screen1'
