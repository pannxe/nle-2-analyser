__version__ = "0.1.1"

import datetime

import flet as ft

import criteria
import widgets

TARGERS = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80]


def report(scores: dict[str, int]) -> ft.View:
    md_text = (
        "# Analysis Report\n\n"
        f"สร้างเมื่อวันที่ {datetime.datetime.now(tz=datetime.UTC):%d/%m/%y เวลา %H:%M}"
        f" น. ด้วย **NL-2 Analyser** v.{__version__} โดย **Mr.Tofu (2025)**\n\n"
        "## Disclaimer\n\n"
        "รายงานต่อไปนี้ไม่ยืนยันความถูกต้อง หากพบโปรแกรมทำงานผิดพลาด สามารถเปิด issue บน "
        "Github ได้ที่ [https://github.com/pannxe/nle-2-analyser/issues](https://github.com/pannxe/nle-2-analyser/issues)\n\n"
        "## วิเคราะห์คะแนน\n\n"
    )
    score_criteria = criteria.NL2_TOPICS

    for k, (name, full), got in zip(
        scores.keys(), score_criteria.values(), scores.values(), strict=False
    ):
        md_text += (
            f"### {k} — {name.capitalize()}\n"
            "| เต็ม | ได้ | % |\n"
            "| :-: | :-: | :-: |\n"
            f"| {full} | **{got}** | {got / full * 100:.2f} |\n\n"
        )
    sum_score = sum(scores.values())
    md_text += (
        f"### สรุปรวมคะแนนทั้งหมด\n\n"
        "| เต็ม | ได้ | % |\n"
        "| :-: | :-: | :-: |\n"
        f"| 300 | **{sum_score}** | {sum_score / 3:.2f} |\n\n"
        "## การวิเคราะห์ Impact\n\n"
        "การดูค่า impact ช่วยวางลำดับความสำคัญของหัวข้อต่าง ๆ ได้ "
        "โดยหัวข้อที่ค่า impact สำหรับคะแนนคาดหวัง (target) นั้น ๆ สูง หมายความว่า "
        "หากคิดว่าน่าจะทำคะแนนได้เท่าค่าคาดหวังในการสอบครั้งหน้า (อาจอ้างอิงจากเกรด) "
        "หัวข้อนั้น ๆ จะมีผลให้คะแนนโดยรวมสูงมากขี้นมากที่สุด คำนวนจากสูตร :\n\n"
        "```text\n"
        "(target - (got / full)) * (full / 3)\n"
        "```\n\n"
        "คะแนนติดลบหมายถึงทำได้ถึงเป้าอยู่แล้ว และค่า impact บวกจะเท่ากับ % คะแนนที่จะเพิ่ม"
        "ขึ้นหากทำหัวข้อนั้น ๆ ได้ถึงเป้า\n\n"
    )

    for target in TARGERS:
        md_text += (
            f"### ค่าคาดหวังที่ {int(target * 100)}%\n\n"
            "| หัวข้อ | impact |\n"
            "| -: | :- |\n"
        )
        for k, (_, full), got in zip(
            scores.keys(),
            score_criteria.values(),
            scores.values(),
            strict=False,
        ):
            md_text += (
                f"| {k} | {(target - (got / full)) * (full / 3):.2f} % |\n"
            )

    def copy_md(e: ft.ControlEvent) -> None:
        e.page.set_clipboard(md_text)

        success_sb = ft.SnackBar(
            content=ft.Text(
                "ระวัง! หากใช้ iOS หรือ iPadOS อาจ copy ไม่สำเร็จ!")
        )
        e.page.open(success_sb)
        e.page.update()

    copy_to_clipboard_fab = ft.FloatingActionButton(
        icon=ft.Icons.COPY, on_click=copy_md
    )

    return ft.View(
        route="/report",
        controls=[
            ft.Markdown(
                md_text,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link=lambda e: e.page.launch_url(e.data),
                md_style_sheet=ft.MarkdownStyleSheet(
                    h1_text_style=ft.TextStyle(24, font_family="nstl-bold"),
                    h2_text_style=ft.TextStyle(18, font_family="nstl-bold"),
                    h3_text_style=ft.TextStyle(16, font_family="nstl-bold"),
                    block_spacing=16,
                ),
                expand=True,
                selectable=True,
            ),
        ],
        floating_action_button=copy_to_clipboard_fab,
        scroll=ft.ScrollMode.AUTO,
        appbar=widgets.appbar(),
    )
