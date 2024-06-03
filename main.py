from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from page1 import MenuPage1
from page2 import MenuPage2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\FinalProject\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1280x800")
window.configure(bg="#FFFFFF")


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x800")
        self.root.configure(bg="#FFFFFF")
        self.current_page = None

        self.show_main_menu()  # Show the main menu initially

    def show_main_menu(self):
        if self.current_page:
            self.current_page.frame.place_forget()  # Hide the current page
        self.current_page = MenuPage1(self.root, self.show_main_menu)

# canvas = Canvas(
#     window,
#     bg="#FFFFFF",
#     height=800,
#     width=1280,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge"
# )
# canvas.place(x=0, y=0)
# canvas.create_rectangle(
#     0.0,
#     0.0,
#     1280.0,
#     800.0,
#     fill="#F4EE76",
#     outline=""
# )
# canvas.create_rectangle(
#     40.0,
#     50.0,
#     1240.0,
#     690.0,
#     fill="#FFFFFF",
#     outline=""
# )

def switch_to_menupage1():
    global menupage1_frame
    menupage1_frame = MenuPage1(window)
    # menupage1_frame.place(x=40, y=50, width=1240, height=640)

def switch_to_menupage2():
    global menupage2_frame
    menupage2_frame = MenuPage2(window)
    # menupage1_frame.place(x=40, y=50, width=1240, height=640)

# button_image_1 = PhotoImage(
#     file=relative_to_assets("button_1.png"))
# button_1 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=switch_to_menupage2,
#     relief="flat"
# )
# button_1.place(
#     x=890.0,
#     y=260.0,
#     width=220.0,
#     height=220.0
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
#     x=530.0,
#     y=260.0,
#     width=220.0,
#     height=220.0
# )

# button_image_3 = PhotoImage(
#     file=relative_to_assets("button_3.png"))
# button_3 = Button(
#     image=button_image_3,
#     borderwidth=0,
#     highlightthickness=0,
#     command=switch_to_menupage1,
#     relief="flat"
# )
# button_3.place(
#     x=170.0,
#     y=260.0,
#     width=220.0,
#     height=220.0
# )

window.resizable(False, False)
window.mainloop()
