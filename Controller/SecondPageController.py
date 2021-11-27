from View.SecondPageView import SecondPageView


class SecondPageController():
    def __init__(self, screen, **kwargs):
        self.view = SecondPageView(self)
        self.screen = screen

    def switch_to_home_page_view(self):
        self.screen.show(self.screen.home_page)

    def switch_to_first_page_view(self):
        self.screen.show(self.screen.first_page)

    def switch_to_third_page_view(self):
        self.screen.show(self.screen.third_page)
