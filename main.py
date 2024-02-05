import flet as ft
import flet_easy as fs

from utils import first_run, get_options, set_default_config

if_first_run = first_run()

options = get_options()

app = fs.FletEasy(route_init="/home")


@app.page_404("/404", page_clear=True)
def page404(data: fs.Datasy):
    page = data.page
    page.title = "Error 404"

    view = data.view

    return ft.View(
        appbar=view.appbar,
        route="/error404",
        controls=[
            ft.Container(
                expand=1,
                alignment=ft.alignment.center,
                content=ft.Text(
                    "Error 404. Page not found.",
                    size=30,
                    expand=1,
                    text_align=ft.MainAxisAlignment.CENTER,
                ),
            ),
            NavBar(),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


@app.view
def app_bar(data: fs.Datasy):
    page = data.page

    appbar = ft.AppBar(
        leading_width=40,
        title=ft.TextButton(
            "Library",
            on_click=lambda e: e.page.go("/home"),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(),
                color=ft.colors.WHITE,
            ),
        ),
        center_title=False,
        bgcolor=ft.colors.GREY_900,
        actions=[
            ft.IconButton(ft.icons.SEARCH),
            ft.IconButton(ft.icons.SORT),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Update Library"),
                    ft.PopupMenuItem(text="Update category"),
                    ft.PopupMenuItem(text="Open Random Entry"),
                ]
            ),
        ],
    )

    return fs.Viewsy(
        appbar=appbar,
    )


class NavBar(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        nav_bar = ft.Container(
            padding=0,
            bgcolor=ft.colors.GREY_900,
            height=80,
            content=ft.Row(
                spacing=20,
                expand=1,
                height=80,
                alignment=ft.alignment.center,
                controls=[
                    fs.ResponsiveControlsy(
                        ft.TextButton(
                            text="Library",
                            height=80,
                            icon=ft.icons.LIBRARY_BOOKS,
                            on_click=lambda e: e.page.go("/home"),
                        ),
                        expand=1,
                    ),
                    fs.ResponsiveControlsy(
                        ft.TextButton(
                            text="Updates",
                            height=80,
                            icon=ft.icons.UPDATE,
                            on_click=lambda e: e.page.go(route="/updates"),
                        ),
                        expand=1,
                    ),
                    fs.ResponsiveControlsy(
                        ft.TextButton(
                            text="History",
                            height=80,
                            icon=ft.icons.HISTORY,
                            on_click=lambda e: e.page.go("/history"),
                        ),
                        expand=1,
                    ),
                    fs.ResponsiveControlsy(
                        ft.TextButton(
                            text="Browse",
                            height=80,
                            icon=ft.icons.EXPLORE,
                        ),
                        expand=1,
                    ),
                    fs.ResponsiveControlsy(
                        ft.TextButton(
                            text="More",
                            height=80,
                            icon=ft.icons.MORE,
                            on_click=lambda e: e.page.go("/settings"),
                        ),
                        expand=1,
                    ),
                ],
            ),
        )

        return nav_bar


@app.page(route="/updates")
def updates_page(data: fs.Datasy):
    page = data.page

    view = data.view

    app_bar = view.appbar
    app_bar.title = ft.TextButton(
        "Updates",
        on_click=lambda e: e.page.go("/home"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(),
            color=ft.colors.WHITE,
        ),
    )

    body = ft.Container(
        expand=80,
        alignment=ft.alignment.center,
        content=ft.Text(
            "No Updates available. Go to Browse to add something from some of the supported sites or to add your own content."
        ),
    )

    return ft.View(
        route="/updates",
        controls=[
            app_bar,
            body,
            NavBar(),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


@app.page(route="/home")
def main(data: fs.Datasy):
    page = data.page

    page.title = options["app_title"]
    page.theme_mode = (
        ft.ThemeMode.DARK
        if options["theme_mode"] == "dark"
        else ft.ThemeMode.LIGHT
        if options["theme_mode"] == "light"
        else ft.ThemeMode.SYSTEM
    )
    # page.window_maximized = True
    page.padding = 0

    theme = ft.Theme()
    theme.page_transitions.android = ft.PageTransitionTheme.OPEN_UPWARDS
    theme.page_transitions.ios = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.macos = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.ZOOM
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    page.theme = theme

    view = data.view

    # page.navigation_bar = NavBar()

    body = ft.Container(
        expand=1,
        alignment=ft.alignment.center,
        content=ft.Text(
            "Library is empty. Go to Browse to add something from some of the supported sites or to add your own content."
        ),
    )

    return ft.View(
        route="/home",
        controls=[
            view.appbar,
            body,
            NavBar(),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


app.run(
    port=8000,
)
