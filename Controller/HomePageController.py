from View.HomePageView import HomePageView

class HomePageController():
    def __init__(self, screen, **kwargs):
        self.view = HomePageView(self)
        self.screen = screen

    def switch_to_first_page_view(self):
        self.screen.show(self.screen.first_page)

    def switch_to_second_page_view(self):
        self.screen.show(self.screen.second_page)

    def switch_to_third_page_view(self):
        self.screen.show(self.screen.third_page)
        