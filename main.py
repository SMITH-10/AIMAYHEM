import flet as ft

def main(page: ft.Page):
    page.title = "Zo World"

    logo=ft.Text(
        value="\z/",
        size=30
    )
    
    logocont=ft.Container(
        content=logo,
        padding=ft.padding.Padding(left=10,right=10,top=10,bottom=0)
    )
   
    field=ft.CupertinoTextField(
        placeholder_text="search",
        bgcolor=ft.colors.GREY_900,
    )


    fieldcont=ft.Container(
        content=field,
        margin=100
    )

    submit=ft.CupertinoButton(
            content=ft.Text("SUBMIT", color=ft.cupertino_colors.WHITE),
            opacity_on_click=0.1,
            bgcolor=ft.colors.BLACK,
            
        )
    submitcon=ft.Container(
        content=submit,
        padding=ft.padding.Padding(left=300,right=10,top=0,bottom=90)

    )
    page.add(
        logocont,
        fieldcont,
        submitcon
        
    )

ft.app(main)