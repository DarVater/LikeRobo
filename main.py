from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.animation import Animation
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import Rotate
from language_screen import LanguageScreen


Window.size = (400, 800)

class FlashCardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flash_card = FlashCard()
        self.add_widget(self.flash_card)
        self.add_back_btn()
        self.x = 0
        self.y = 0

    def add_back_btn(self):
        self.button = Button(text=lang_core.get_text_from_map('mein_menu_title'),
                             size_hint=[1, .1],
                             pos_hint={'right': 1, 'top': 1})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def next_card(self, animation, rotate):
        self.x = 0
        self.y = self.width * 2
        self.clear_widgets()
        self.flash_card = FlashCard()
        self.add_widget(self.flash_card)
        self.add_back_btn()
        animation = Animation(y=0, duration=0.1)
        animation.start(self)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        screen_manager.current = 'screen1'

class FlashCard(FloatLayout, DragBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        card_pos = (200, 400)
        self.front = Image(source='fleshcard.png', allow_stretch=True, keep_ratio=False, size_hint=(0.8, 0.8),
                           pos_hint={'center_x': 0.9, 'center_y': 0.9})
        self.back = Image(source='fleshcard.png', allow_stretch=True, keep_ratio=False, size_hint=(0.8, 0.8),
                           pos_hint={'center_x': 0.9, 'center_y': 0.9})
        self.front.add_widget(Label(text='Front of card', font_size='20sp', size_hint=(1, 1),
                                    pos=[Window.size[0]/3, Window.size[1]/3.2]))
        self.back.add_widget(Label(text='Back of card', font_size='20sp', size_hint=(1, 1),
                                    pos=[Window.size[0]/3, Window.size[1]/3.2]))
        self.add_widget(self.front)
        self.is_back_card = False

        with self.front.canvas.before:
            PushMatrix()
            print(self.front.pos)
            self.front.rot = Rotate()
            self.front.rot.angle = 0
            self.front.rot.origin = [Window.size[0]/2, Window.size[1]/2]
            self.front.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.front.rot.axis = (0, 0, 1)
        with self.front.canvas.after:
            PopMatrix()


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
                    with self.back.canvas.before:
                        PushMatrix()
                        self.back.rot = Rotate()
                        self.back.rot.angle = 0
                        self.back.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                        self.back.rot.axis = (0, 0, 1)
                    with self.back.canvas.after:
                        PopMatrix()
                    self.is_back_card = True

            elif touch.x < touch.touch_down_x:
                # self.rot.angle -= 20
                # Shift to the right
                animation = Animation(x=-1*(self.parent.width + self.width), duration=0.1)
                animation.bind(on_complete=self.parent.next_card)
                animation.start(self.parent)
            touch.ungrab(self)

            return 1
        return super().on_touch_up(touch)

    def change_card_side(self, animation, rotate):
        self.clear_widgets()
        self.add_widget(self.back)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source='background.png', allow_stretch=True, keep_ratio=False))
        button_grid = GridLayout(cols=1, size_hint=(0.2, 0.8), pos_hint={'right': 1, 'center_y': 0.5}, orientation='rl-bt')
        button1 = Button(text="Button 1")
        button1.bind(on_press=self.goto_screen2)
        button_grid.add_widget(button1)
        button_grid.add_widget(Button(text="Button 2"))
        button_grid.add_widget(Button(text="Button 3"))
        button_grid.add_widget(Button(text="Button 4"))
        button_grid.add_widget(Button(text="Exit", on_press=self.exit_app))
        self.add_widget(button_grid)

    def goto_screen2(self, instance):
        screen_manager.current = 'screen2'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        global lang_core
        super().__init__(**kwargs)
        self.add_widget(Image(source='background.png', allow_stretch=True, keep_ratio=False))
        button_grid = GridLayout(cols=1, size_hint=(0.3, 0.5), pos_hint={'right': 1, 'center_y': 0.5}, orientation='rl-bt')
        button1 = Button(text="Road Map")
        button1.bind(on_press=self.goto_screen2)
        print(lang_core.selected_language)
        button2 = Button(text=lang_core.get_text_from_map(title='bind_title'))
        button2.bind(on_press=self.goto_screen3)
        button3 = Button(text=lang_core.get_text_from_map('settings_title'))
        button3.bind(on_press=self.goto_screen4)
        button_grid.add_widget(Button(text=lang_core.get_text_from_map('exit_title')
                                      , on_press=self.exit_app))
        button_grid.add_widget(button3)
        button_grid.add_widget(button2)
        button_grid.add_widget(button1)
        self.add_widget(button_grid)

    def goto_screen2(self, instance):
        screen_manager.current = 'screen2'

    def goto_screen3(self, instance):
        screen_manager.current = 'screen3'

    def goto_screen4(self, instance):
        screen_manager.current = 'screen4'

    def exit_app(self, instance):
        App.get_running_app().stop()

class RoadmapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source='roadmap_background.png', allow_stretch=True, keep_ratio=False))
        self.indicator_grid = GridLayout(rows=25, row_default_height=20, row_force_default=True,
                                                size_hint=[0.2, .2],
                                                pos_hint={'center_x':  0.9, 'center_y': 0.65})
        for i in range(20):
            self.indicator_grid.add_widget(Button(text='Indicator %d' % (i + 1),
                                         size_hint=[0.1, .2], width = 30))
            if (i+1) % 4 == 0:
                self.indicator_grid.add_widget(Label(text=''))

        self.add_widget(self.indicator_grid)
        self.add_back_btn()
        self.add_widget(Label(text='Roadmap', font_size='30sp',
                             pos_hint={'center_x':  0.2, 'center_y': 0.87}))

    def add_back_btn(self):
        self.button = Button(text=lang_core.get_text_from_map('mein_menu_title'),
                             size_hint=[1, .1],
                             pos_hint={'right': 1, 'top': 1})
        self.button.bind(on_press=self.goto_main)
        self.add_widget(self.button)

    def goto_main(self, instance):
        animation = Animation(y=-180, duration=0.5)
        animation.start(self)
        screen_manager.current = 'screen1'

screen_manager = ScreenManager()

def screen_manager_rebuild():
    global lang_core
    screen_manager.clear_widgets()
    screen_manager.add_widget(lang_core)
    screen_manager.add_widget(MainScreen(name='screen1'))
    screen_manager.add_widget(RoadmapScreen(name='screen2'))
    screen_manager.add_widget(FlashCardScreen(name='screen3'))


lang_core = LanguageScreen(screen_manager, name='screen4')
screen_manager.add_widget(lang_core)
screen_manager.add_widget(MainScreen(name='screen1'))
screen_manager.add_widget(RoadmapScreen(name='screen2'))
screen_manager.add_widget(FlashCardScreen(name='screen3'))
screen_manager.current = 'screen1'

screen_manager.rebuild = screen_manager_rebuild

class MyApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    MyApp().run()
