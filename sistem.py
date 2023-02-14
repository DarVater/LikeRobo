from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window

kv = """
<BackButton@Button>:
    background_color: 0,0,0,0  
    background_normal: ''
    canvas.before:
        Color: 
            rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            source: 'imgs/home_btn_normal.png' if self.state=='normal' else 'imgs/home_btn_down.png'
            pos: self.pos
            size: self.size
            radius: [50,]
<StartButton@Button>:
    background_down: 0,0,0,0
    background_normal: ''
    canvas.before:
        Color: 
            rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            source: 'imgs/start_road_btn_normal.png' if self.state=='normal' else 'imgs/_down.png'
            pos: self.pos
            size: self.size
"""

class BackButton(Button):
    pass

class StartButton(Button):
    pass

Builder.load_string(kv)


def get_media_lvl():
    media_lvl = 'M1'
    if Window.size[1] > 1500:
        if Window.size[0] < 1500:
            media_lvl = 'M2'
    print('media_lvl', media_lvl)
    return media_lvl
