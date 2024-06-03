from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame4")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuPage31(Frame):
    def __init__(self, master, show_main_menu_func, switch_to_menu_page3, switch_to_tme_page, switch_to_ee_page, switch_to_ene_page, switch_to_te_page, switch_to_coe_page):
        super().__init__(master)
        self.show_main_menu_func = show_main_menu_func
        self.switch_to_menu_page3 = switch_to_menu_page3
        self.switch_to_tme_page = switch_to_tme_page
        self.switch_to_ee_page = switch_to_ee_page
        self.switch_to_ene_page = switch_to_ene_page
        self.switch_to_te_page = switch_to_te_page
        self.switch_to_coe_page = switch_to_coe_page

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
            command=switch_to_menu_page3,
            relief="flat"
        )
        button_2.place(x=490.0, y=710.0, width=70.0, height=70.0)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=switch_to_coe_page,
            relief="flat"
        )
        button_3.place(
            x=150.0,
            y=390.0,
            width=450.0,
            height=100.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=switch_to_te_page,
            relief="flat"
        )
        button_4.place(
            x=680.0,
            y=250.0,
            width=450.0,
            height=100.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=switch_to_ene_page,
            relief="flat"
        )
        button_5.place(
            x=150.0,
            y=250.0,
            width=450.0,
            height=100.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=switch_to_ee_page,
            relief="flat"
        )
        button_6.place(
            x=680.0,
            y=110.0,
            width=450.0,
            height=100.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=switch_to_tme_page,
            relief="flat"
        )
        button_7.place(
            x=150.0,
            y=110.0,
            width=450.0,
            height=100.0
        )


        print("MenuPage1 initialized")

