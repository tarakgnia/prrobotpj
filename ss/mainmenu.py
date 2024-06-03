from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainMenu(Frame):
    def __init__(self, master, switch_to_menu_page1, switch_to_menu_page2, switch_to_menu_page3, switch_to_menu_page31):
        super().__init__(master)
        self.switch_to_menu_page1 = switch_to_menu_page1
        self.switch_to_menu_page2 = switch_to_menu_page2
        self.switch_to_menu_page3 = switch_to_menu_page3
        self.switch_to_menu_page31 = switch_to_menu_page31
        self.configure(bg="#FFFFFF")

        frame = Canvas(
            self,
            bg="#FFFFFF",
            height=800,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        frame.place(x=0, y=0)
        frame.create_rectangle(
            0.0,
            0.0,
            1280.0,
            800.0,
            fill="#F4EE76",
            outline=""
        )
        frame.create_rectangle(
            40.0,
            50.0,
            1240.0,
            690.0,
            fill="#FFFFFF",
            outline=""
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_menu_page2,
            relief="flat"
        )
        button_1.place(x=890.0, y=260.0, width=220.0, height=220.0)
        print("Button 1 initialized")
        
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_menu_page1,
            relief="flat"
        )
        button_2.place(x=530.0, y=260.0, width=220.0, height=220.0)
        print("Button 2 initialized")


        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_menu_page3,
            relief="flat"
        )
        button_3.place(x=170.0, y=260.0, width=220.0, height=220.0)
        print("Button 3 initialized")
       
        print("MainMenu initialized")
