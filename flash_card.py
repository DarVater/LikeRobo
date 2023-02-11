from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.animation import Animation
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import Rotate
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class FlashCardScreen(Screen):
    def __init__(self, lang_data, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.flash_card = FlashCard()
        self.add_widget(self.flash_card)
        self.screen_manager = screen_manager
        self.lang_data = lang_data
        print(lang_data)
        self.x = 0
        self.y = 0
        self.add_back_btn()

    def add_back_btn(self):
        self.button = Button(text=self.lang_data.get_text_from_map('mein_menu_title'),
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
        self.screen_manager.current = 'screen1'


class FlashCard(FloatLayout, DragBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        card_pos = (200, 400)
        self.front = self.create_new_card('fleshcard_new.png')
        self.back = self.create_new_card('fleshcard_know.png')
        self.fail = self.create_new_card('fleshcard_fail.png')
        self.add_widget(self.front)
        self.is_back_card = False


    def create_new_card(self, src):
        result_widget = Image(source='imgs/'+src, allow_stretch=True, keep_ratio=False, size_hint=(0.8, 0.8),
                           pos_hint={'center_x': 0.9, 'center_y': 0.9})

        result_widget.add_widget(Label(text='Я буду работающим? \n\n(продолжительное \nбудет длиться)', font_size='20sp', size_hint=(1, 1),
                                    pos=[Window.size[0]/3, Window.size[1]/3.2]))
        with result_widget.canvas.before:
            PushMatrix()
            result_widget.rot = Rotate()
            result_widget.rot.angle = 0
            result_widget.rot.origin = [Window.size[0]/2, Window.size[1]/2]
            result_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            result_widget.rot.axis = (0, 0, 1)
        with result_widget.canvas.after:
            PopMatrix()
        return result_widget

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
                    self.is_back_card = True

            elif touch.x < touch.touch_down_x:

                self.clear_widgets()
                self.add_widget(self.fail)
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

