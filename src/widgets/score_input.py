import flet as ft

SIZE_CUTOFF = 6


class ScoreInput(ft.Row):
    def __init__(self, name: str, full_score: int) -> None:
        super().__init__()
        self.name: str = name
        self.full_score: int = full_score
        self.score: int = 0

    def build(self) -> None:
        def dd_change(e: ft.ControlEvent) -> None:
            self.score = int(e.control.value)

        dd_options = [
            ft.DropdownOption(
                key=str(k),
                text=f"{100 * k / self.full_score:.2f}%",
            )
            for k in range(self.full_score + 1)
        ]

        input_dd = ft.Dropdown(
            options=dd_options,  # type: ignore noqa
            label=self.name,
            on_change=dd_change,
            editable=True,
            menu_height=250 if len(dd_options) > SIZE_CUTOFF else None,
            expand=True,
            enable_filter=True,
            enable_search=True,
            border_color=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        )

        self.score = int(input_dd.value or 0)

        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            input_dd,
        ]
