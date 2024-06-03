from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuPage1(Frame):
    def __init__(self, master, show_main_menu_func):
        super().__init__(master)
        self.show_main_menu_func = show_main_menu_func
        self.configure(bg="#FFFFFF")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=800,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            800.0,
            fill="#F4EE76",
            outline=""
        )
        canvas.create_rectangle(
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
            command=self.show_main_menu_func,
            relief="flat"
        )
        button_1.place(x=600.0, y=705.0, width=80.0, height=80.0)

        print("MenuPage1 initialized")

