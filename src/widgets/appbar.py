import flet as ft


def appbar() -> ft.AppBar:
    return ft.AppBar(
        title=ft.Text("NL2 Analyser"),
        center_title=True,
        force_material_transparency=True,
    )
