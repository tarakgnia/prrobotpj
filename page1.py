from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



class MenuPage1:
    def __init__(self, master, show_main_menu_func):
        self.master = master
        self.show_main_menu_func = show_main_menu_func
        self.frame = Canvas(
            self.master,
            bg="#FFFFFF",
            height=800,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.frame.place(x=0, y=0)
        self.frame.create_rectangle(
            0.0,
            0.0,
            1280.0,
            800.0,
            fill="#F4EE76",
            outline=""
        )
        self.frame.create_rectangle(
            40.0,
            50.0,
            1240.0,
            690.0,
            fill="#FFFFFF",
            outline=""
        )
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.master,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_main_menu_func,
            relief="flat"
        )
        self.button_1.place(x=600.0, y=705.0, width=80.0, height=80.0)
