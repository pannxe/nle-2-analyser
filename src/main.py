__version__ = "0.1.1"


import flet as ft

import views


def main(page: ft.Page) -> None:
    page.fonts = {
        "nstl": "/fonts/NotoSansThaiLooped-Regular.ttf",
        "nstl-bold": "/fonts/NotoSansThaiLooped-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="nstl")
    page.adaptive = False

    def route_change(_: ft.RouteChangeEvent) -> None:
        if page.route != "/report":
            page.views.clear()
            page.views.append(views.data_input())
        page.update()

    def view_pop(_: ft.ViewPopEvent) -> None:
        page.views.pop()
        page.go(page.views[-1].route)  # type: ignore noqa

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(
    main,
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER,
    route_url_strategy="hash",
    web_renderer=ft.WebRenderer.HTML,
)
