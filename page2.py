from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuPage2:
    def __init__(self, master):
        self.master = master
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
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=660.0, y=705.0, width=80.0, height=80.0)
       
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=540.0, y=705.0, width=80.0, height=80.0)



# canvas = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 800,
#     width = 1280,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )

# canvas.place(x = 0, y = 0)
# canvas.create_rectangle(
#     0.0,
#     0.0,
#     1280.0,
#     800.0,
#     fill="#F4EE76",
#     outline="")

# canvas.create_rectangle(
#     40.0,
#     50.0,
#     1240.0,
#     690.0,
#     fill="#FFFFFF",
#     outline="")

# button_image_1 = PhotoImage(
#     file=relative_to_assets("button_1.png"))
# button_1 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_1 clicked"),
#     relief="flat"
# )
# button_1.place(
#     x=660.0,
#     y=705.0,
#     width=80.0,
#     height=80.0
# )

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_2 clicked"),
#     relief="flat"
# )
# button_2.place(
#     x=540.0,
#     y=705.0,
#     width=80.0,
#     height=80.0
# )

