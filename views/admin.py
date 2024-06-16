import flet as ft
import flet_easy as fs
from components import SwoDrawer

counter = fs.AddPagesy(
    route_prefix="/admin",
)


# We add a second page
@counter.page(route="/", title="Admin")
def counter_page(data: fs.Datasy):
    page = data.page
    view = data.view

    return ft.View(
        controls=[
            ft.Text("Admin menu"),
            SwoDrawer("Show_drawer", view.drawer)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.drawer,
    )
