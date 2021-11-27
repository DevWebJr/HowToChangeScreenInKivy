from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Controller.HomePageController import HomePageController
from Controller.FirstPageController import FirstPageController
from Controller.SecondPageController import SecondPageController
from Controller.ThirdPageController import ThirdPageController


class Window(BoxLayout):
    """this class implement a method for clear all widgets before displaying a view"""
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, orientation='vertical', **kwargs)


    def display_screen(self, screen):
        """This function displays screen you have passed in argument"""
        self.clear_widgets()
        self.add_widget(screen)


class Screens():
    """this class is a manager for all views"""
    def __init__(self):
        
        self.window = Window()
        
        self.home_page = HomePageController(self)

        self.first_page = FirstPageController(self)

        self.second_page = SecondPageController(self)

        self.third_page = ThirdPageController(self)

        self.window.display_screen(self.home_page.view)
        

    def show(self, screen):
        """This shortcut function calls the function of Class Window, which one can display screen you have passed in argument"""
        self.window.display_screen(screen.view)


class Game(App):
    def build(self):
        self.title = "Display Screeens in Kivy"
        screen = Screens()
        return screen.window


if __name__ == '__main__':
    Game().run()
