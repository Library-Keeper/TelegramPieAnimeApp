import flet as ft
import flet_easy as fs
from components import SwoDrawer

index = fs.AddPagesy()


# We add a page
@index.page(route="/", title="Flet-Easy")
def index_page(data: fs.Datasy):
    view = data.view

    return ft.View(
        controls=[
            ft.Text("Home page", size=30),
            SwoDrawer("Show_drawer", view.drawer),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.drawer,
    )

@index.page(route="/{id}", title="Flet-Easy")
def index_page(data: fs.Datasy):
    view = data.view

    return ft.View(
        controls=[
            ft.Text("Home page", size=30),
            SwoDrawer("Show_drawer", view.drawer),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.drawer,
    )