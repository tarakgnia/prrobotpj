from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage
from tkinterweb import HtmlFrame #import the HTML browser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame6")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RcePage(Frame):
    def __init__(self, master, show_main_menu_func, switch_to_menu_next, switch_to_menu_back):
        super().__init__(master)
        self.show_main_menu_func = show_main_menu_func
        self.switch_to_menu_next = switch_to_menu_next
        self.switch_to_menu_back = switch_to_menu_back
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

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_menu_next,
            relief="flat"
        )
        button_2.place(x=720.0, y=710.0, width=70.0, height=70.0)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_menu_back,
            relief="flat"
        )
        button_3.place(
            x=490.0,
            y=710.0,
            width=70.0,
            height=70.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            640.0,
            370.0,
            image=self.image_image_1
        )

        # Add HtmlFrame to display a webpage
        self.html_frame = HtmlFrame(self, horizontal_scrollbar="auto")
        self.html_frame.place(x=41.0, y=47.0, width=1198.0, height=638.0)
        self.html_frame.load_website("http://eng.rmutsv.ac.th/engineeri/th/railway-civil")

        print("RCE")

