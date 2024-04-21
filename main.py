import flet as ft
from neurum import Neurum
import json

n=Neurum('vansh')
sys_prompt="SYSTEM PROMPT: Your name is Zo. You are an AI concierge of Zo World which provides a house studio style event space for indie hackers, creators to conduct events like hackathons and workshops, etc and also operates Zostels which are affordable hostel accomodation for travellers providing an engaging community. You only respond in JSON format with only 2 keys namely Answer, which is the message you give to the user, and Booking which is a boolean. Customers can ask to book appointments for conducting events, and when they ask to book appointments or anything, you will set Booking boolean to true and answer that you're happy to book an appointment and will ask for nothing, otherwise respond with false in the JSON. You will answer user's queries regarding Zo House and help them navigate the process of the event. You can only talk about this topic of Zo World and its events and not about anything else. You can also give suggestions if asked about the event but nothing else."

def main(page: ft.Page):
    page.title = "Zo World"

    chats=[]

    def submitinfo(event):

        info={"Name": name.value, 
              "Contact": contact.value, 
              "Event Name": eventname.value, 
              "Date": date.value
             }

        # Try to read the existing data from the file
        json_data=json.dumps(info, indent=4)

        with open('data.json', "w") as json_file:
            json_file.write(json_data)

        name.value=""
        contact.value=""
        eventname.value=""
        date.value=""

    name=ft.CupertinoTextField(
                        placeholder_text="Name",
                    )
    contact=ft.CupertinoTextField(
                        placeholder_text="Contact",
                    )
    eventname=ft.CupertinoTextField(
                        placeholder_text="Event Name",
                    )
    date=ft.CupertinoTextField(
                        placeholder_text="Event Date",
                    )
    subinfo=ft.CupertinoButton(
                        text="submit",
                        bgcolor="#24915e",
                        color="white",
                        on_click=submitinfo
                    )

    def submit(event):
        chats.append(ft.Container(content=ft.Text(field.value, color="white"),
                                  bgcolor=ft.colors.GREY_900,
                                  padding=10,
                                  border_radius=10,
                                  ))
        page.update()


        res=n.generate(f"{sys_prompt}. USER PROMPT: {field.value}")
        response_json=json.loads(res)
        answer=response_json['Answer']
        
        chats.append(ft.Container(content=ft.Text(answer, color="white"),
                                  bgcolor="#24915e",
                                  padding=10,
                                  border_radius=10,
                                  ))
        field.value=""
        if response_json['Booking']==True:
            chats.append(ft.Container(
                content=ft.Column(
                    [name, 
                     contact, 
                     eventname, 
                     date, 
                     subinfo],
                )
            ))

        page.update()
    
    logo=ft.Container(
        content=ft.Text(
            value="\z/",
            size=25,
            color="#36d189",
        ),
        padding=ft.padding.Padding(left=20,right=10,top=10,bottom=0)
    )

    chatcont=ft.Container(
        content=ft.Column([ft.Container(ft.Text("\z/", size=35, color="#36d189"), padding=ft.padding.Padding(left=300, right=0, top=0, bottom=0)),
                           ft.ListView(controls=chats, 
                                       spacing=10,
                                       )],
                                       width=800,
                                       scroll=ft.ScrollMode.HIDDEN,
                                       expand=True),
        bgcolor="black",
        margin=ft.margin.Margin(left=310, right=200, top=50, bottom=0),
        width=800,
        height=600,
        border_radius=30,
        padding=ft.padding.Padding(left=75, right=100, top=10, bottom=0)
    )

    field=ft.CupertinoTextField(
                placeholder_text="How may i help you?",
                bgcolor=ft.colors.GREY_900,
                width=800,
                height=50,
                border_radius=10,
                selection_color="#36d189",
                focused_border_color="#36d189",
                on_submit=submit
                )
    
    form=ft.Container(
        content=ft.Row(
                    controls=[field],
                    ),
        padding=ft.padding.Padding(left=310, right=250, top=130, bottom=20),
        
        )

    page.add(
        logo,
        chatcont,
        form
    
    )

ft.app(main)