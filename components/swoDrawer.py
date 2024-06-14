from flet import AppBar, NavigationDrawer, IconButton
import flet as ft


class SwoDrawer(AppBar):
    def __init__(
        self, text: str, drawer: NavigationDrawer, close: bool = False, **kwargs
    ) -> AppBar:
        super().__init__(**kwargs)
        self.leading = IconButton(
            icon=ft.icons.MENU,
            on_click=self.go_url
        )
        self.drawer = drawer
        self.close = close
        self.title = ft.Text(text)
        self.bgcolor = ft.colors.RED_400

    def go_url(self, e):
        if not self.close:
            self.drawer.open = True
        else:
            self.drawer.open = False

        self.page.update()
