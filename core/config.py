import flet as ft
import flet_easy as fs


class ConfigApp:
    def __init__(self, app: fs.FletEasy):
        self.app = app
        self.start()

    def start(self):
        @self.app.view
        def view_config(data: fs.Datasy):
            return fs.Viewsy(
                drawer=ft.NavigationDrawer(
                    controls=[
                        ft.Container(height=12),
                        ft.Column(
                            controls=[
                                ft.Text("PieAnime", size=25, text_align=ft.TextAlign.CENTER),
                                ft.Divider(thickness=2),
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text("Anime", size=25),
                                            ft.Icon(name=ft.icons.MOVIE_FILTER_OUTLINED)
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    on_click=data.go(data.route_init),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=0)
                                    ),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                )
            )

        @self.app.config
        def page_config(page: ft.Page):
            theme = ft.Theme()
            platforms = ["android", "ios", "macos", "linux", "windows"]
            for platform in platforms:  # Removing animation on route change.
                setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)
            page.theme = theme
