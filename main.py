import flet as ft

from utils import first_run, get_options, set_default_config

if_first_run = first_run()

options = get_options()

def main(page: ft.Page):
    page.title = options["app_title"]
    page.theme_mode = ft.ThemeMode.DARK if options["theme_mode"] == "dark" else ft.ThemeMode.LIGHT if options["theme_mode"] == "light" else ft.ThemeMode.SYSTEM
    #page.window_maximized = True
    
    page.window_maximized = True
    
    theme = ft.Theme()
    theme.page_transitions.android = ft.PageTransitionTheme.OPEN_UPWARDS
    theme.page_transitions.ios = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.macos = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.ZOOM
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    page.theme = theme

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Library"),
        center_title=False,
        bgcolor=ft.colors.GREY_900,
        actions=[
            ft.IconButton(ft.icons.SEARCH),
            ft.IconButton(ft.icons.SORT),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Update Library"
                        ),
                    ft.PopupMenuItem(
                        text="Update category"
                        ),
                    ft.PopupMenuItem(
                        text="Open Random Entry"
                        ),
                ]
            ),
        ],
    )
    
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        adaptive=True,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.LIBRARY_BOOKS,
                label="Library"
                ),
            ft.NavigationDestination(
                icon=ft.icons.UPDATE, 
                label="Updates"
                ),
            ft.NavigationDestination(
                icon=ft.icons.HISTORY,
                label="History",
            ),
            ft.NavigationDestination(
                icon=ft.icons.EXPLORE,
                label="Browse",
            ),
            ft.NavigationDestination(
                icon=ft.icons.MORE,
                label="More",
            ),
        ]
    )
    
    body = ft.Container(
        expand=80,
        content=ft.Text("Library is empty. Go to Browse to add something from some of the supported sites or to add your own content."),
    )
    
    page.add(
        body,
    )

ft.app(target=main)