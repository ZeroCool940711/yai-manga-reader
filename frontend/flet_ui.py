import flet as ft

def main(page: ft.Page):
    page.title = "Yai"
    page.theme_mode = ft.ThemeMode.DARK
    #page.window_maximized = True


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
        expand=1,
        content=ft.Text("Library is empty. Go to Browse to add something from some of the supported sites or to add your own content."),
    )
    
    page.add(
        body,
    )

ft.app(target=main)