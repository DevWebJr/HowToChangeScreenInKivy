from kivy.core.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class HomePageView(FloatLayout):
    def __init__(self, controller, **kwargs):
        FloatLayout.__init__(self, **kwargs)
        self.controller = controller
        self.label = Label()
        self.label.text = "Vous êtes sur la page d'accueil"
        self.label.color = "#fdcb6e"
        self.label.font_size = 33
        self.label.bold = True
        self.label.italic = True
        self.add_widget(self.label)
        self.add_buttons()
        
    def add_buttons(self):
        self.box = BoxLayout()
        self.add_widget(self.box)
        self.switch_to_first_page_button = Button(
            text='Page 1', background_normal="", background_color="#2d3436", color="#fab1a0", size_hint=(.20, .20))
        self.switch_to_first_page_button.bind(on_press=self.switch_to_first_page)
        self.box.add_widget(self.switch_to_first_page_button)
        
        self.switch_to_second_page_button = Button(
            text='Page 2', background_normal="", background_color="#2d3436", color="#0984e3", size_hint=(.20, .20))
        self.switch_to_second_page_button.bind(on_press=self.switch_to_second_page)
        self.box.add_widget(self.switch_to_second_page_button)

        self.switch_to_third_page_button = Button(
            text='Page 3', background_normal="", background_color="#2d3436", color="#a29bfe", size_hint=(.20, .20))
        self.switch_to_third_page_button.bind(on_press=self.switch_to_third_page)
        self.box.add_widget(self.switch_to_third_page_button)
        
    def switch_to_first_page(self, widget):
        self.controller.switch_to_first_page_view()

    def switch_to_second_page(self, widget):
        self.controller.switch_to_second_page_view()

    def switch_to_third_page(self, widget):
        self.controller.switch_to_third_page_view()
