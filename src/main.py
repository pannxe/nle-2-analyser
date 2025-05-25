__version__ = "0.1.1"


import flet as ft

import views


def main(page: ft.Page) -> None:
    page.fonts = {
        "nstl": "/fonts/NotoSansThaiLooped-Regular.ttf",
        "nstl-bold": "/fonts/NotoSansThaiLooped-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="nstl")

    def route_change(_: ft.ControlEvent) -> None:
        if page.route == "/":
            page.views.clear()
            page.views.append(views.data_input())
        elif page.route != "/report":
            page.go("/")

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(main, assets_dir="assets",
       view=ft.AppView.WEB_BROWSER, route_url_strategy="hash")
