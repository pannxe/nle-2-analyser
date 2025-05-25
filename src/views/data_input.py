import flet as ft

import criteria
import widgets

from .report import report


def data_input() -> ft.View:
    score_inputs_content = [
        widgets.ScoreInput(k, v[1]) for k, v in criteria.NL2_TOPICS.items()
    ]

    score_inputs_col = ft.Column(
        controls=score_inputs_content,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    footer_txt = ft.Text(
        "Made by Mr.Tofu (2025)\nFor educational purpose only.",
    )

    def gen_report(e: ft.ControlEvent) -> None:
        scores = {c.name: int(c.score) for c in score_inputs_content}
        e.page.views.clear()
        e.page.views.append(report(scores))
        e.page.go("/report")

    gen_report_btn = ft.FilledButton(
        "Analyse",
        icon=ft.Icons.ANALYTICS,
        on_click=gen_report,
    )
    footer_row = ft.Row(
        controls=[
            footer_txt,
            gen_report_btn,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    main_col = ft.Column(
        controls=[
            score_inputs_col,
            footer_row,
        ],
        expand=True,
        spacing=8,
    )

    return ft.View(
        route="/",
        controls=[main_col],
        appbar=widgets.appbar(),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
