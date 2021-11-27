from View.FirstPageView import FirstPageView


class FirstPageController():
    def __init__(self, screen, **kwargs):
        self.view = FirstPageView(self)
        self.screen = screen

    def switch_to_home_page_view(self):
        self.screen.show(self.screen.home_page)

    def switch_to_second_page_view(self):
        self.screen.show(self.screen.second_page)

    def switch_to_third_page_view(self):
        self.screen.show(self.screen.third_page)
