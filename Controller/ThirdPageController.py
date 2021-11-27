from View.ThirdPageView import ThirdPageView


class ThirdPageController():
    def __init__(self, screen, **kwargs):
        self.view = ThirdPageView(self)
        self.screen = screen

    def switch_to_home_page_view(self):
        self.screen.show(self.screen.home_page)

    def switch_to_first_page_view(self):
        self.screen.show(self.screen.first_page)

    def switch_to_second_page_view(self):
        self.screen.show(self.screen.second_page)
