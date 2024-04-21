import flet as ft

def main(page: ft.Page):
    page.title = "Zo World"

    chats=[]
    
    logo=ft.Container(
        content=ft.Text(
            value="\z/",
            size=25,
            color="#36d189"
        ),
        padding=ft.padding.Padding(left=20,right=10,top=10,bottom=0)
    )

    chatcont=ft.Container(
        content=ft.Column([ft.Text("\z/", size=35, color="#36d189"),
                           ft.ListView(controls=[])]),
        bgcolor="black",
        margin=ft.margin.Margin(left=310, right=200, top=50, bottom=0),
        width=800,
        height=600,
        border_radius=30,
        padding=ft.padding.Padding(left=375, right=100, top=10, bottom=0)
    )

    field=ft.CupertinoTextField(
                placeholder_text="How may i help you?",
                bgcolor=ft.colors.GREY_900,
                width=800,
                height=50,
                border_radius=10,
                )

    submit=ft.IconButton(
                bgcolor="#36d189",
                icon=ft.icons.SEND_ROUNDED,
                icon_color="white",
                height=50,
                width=50,
                hover_color=ft.colors.TRANSPARENT,
                padding=ft.padding.Padding(left=5, top=0, right=0, bottom=0)
            )
    
    form=ft.Container(
        content=ft.Row(
                    controls=[field, submit],
                    ),
        padding=ft.padding.Padding(left=300, right=250, top=130, bottom=20),
        
        )

    page.add(
        logo,
        chatcont,
        form
    
    )

ft.app(main)