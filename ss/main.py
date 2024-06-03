from tkinter import Tk
from mainmenu import MainMenu
from menupage1 import MenuPage1
from menupage2 import MenuPage2
from menupage3 import MenuPage3
from menupage31 import MenuPage31
from ce_page import CePage
from rce_page import RcePage
from se_page import SePage
from ie_page import IePage
from pe_page import PePage
from tie_page import TiePage
from me_page import MePage
from mre_page import MrePage
from tme_page import TmePage
from ee_page import EePage
from ene_page import EnePage
from te_page import TePage
from coe_page import CoePage
from tkinterweb import HtmlFrame #import the HTML browser
import speech_recognition as sr
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x800")
        self.root.configure(bg="#FFFFFF")
        self.current_page = None

        self.main_menu = MainMenu(self.root, self.show_menu_page1, self.show_menu_page2, self.show_menu_page3, self.show_menu_page31)
        self.menu_page1 = MenuPage1(self.root, self.show_main_menu)
        self.menu_page2 = MenuPage2(self.root, self.show_main_menu, self.listen_and_open_video)
        self.menu_page3 = MenuPage3(self.root, self.show_main_menu, self.show_menu_page31, self.show_ce_page, self.show_rce_page, self.show_se_page, self.show_pe_page, self.show_ie_page, self.show_tie_page, self.show_me_page, self.show_mre_page)
        self.menu_page31 = MenuPage31(self.root, self.show_main_menu, self.show_menu_page3, self.show_tme_page, self.show_ee_page, self.show_ene_page, self.show_te_page, self.show_coe_page)
        self.ce_page = CePage(self.root, self.show_main_menu, self.show_rce_page)
        self.rce_page = RcePage(self.root, self.show_main_menu, self.show_se_page, self.show_ce_page)
        self.se_page = SePage(self.root, self.show_main_menu, self.show_pe_page, self.show_rce_page)
        self.pe_page = PePage(self.root, self.show_main_menu, self.show_ie_page, self.show_se_page)
        self.ie_page = IePage(self.root, self.show_main_menu, self.show_tie_page, self.show_pe_page)
        self.tie_page = TiePage(self.root, self.show_main_menu, self.show_me_page, self.show_ie_page)
        self.me_page = MePage(self.root, self.show_main_menu, self.show_mre_page, self.show_tie_page)
        self.mre_page = MrePage(self.root, self.show_main_menu, self.show_tme_page, self.show_me_page)
        self.tme_page = TmePage(self.root, self.show_main_menu, self.show_ee_page, self.show_mre_page)
        self.ee_page = EePage(self.root, self.show_main_menu, self.show_ene_page, self.show_tme_page)
        self.ene_page = EnePage(self.root, self.show_main_menu, self.show_te_page, self.show_ee_page)
        self.te_page = TePage(self.root, self.show_main_menu, self.show_coe_page, self.show_ene_page)
        self.coe_page = CoePage(self.root, self.show_main_menu, self.show_te_page)        
        

        self.show_main_menu()

    def show_main_menu(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.main_menu
        self.current_page.pack(fill='both', expand=True)
        print("Main menu displayed")

    def show_menu_page1(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.menu_page1
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_menu_page2(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.menu_page2
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_menu_page3(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.menu_page3
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_menu_page31(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.menu_page31
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_ce_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.ce_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_rce_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.rce_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_se_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.se_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_ie_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.ie_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_pe_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pe_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_tie_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.tie_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_me_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.me_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_mre_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.mre_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_tme_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.tme_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_ee_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.ee_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_ene_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.ene_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_te_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.te_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def show_coe_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.coe_page
        self.current_page.pack(fill='both', expand=True)
        print("MenuPage1 displayed")

    def listen_and_open_video(self):
        self.r = sr.Recognizer()

        with sr.Microphone() as source:
            print("กรุณาพูดคำสั่งเพื่อเปิดวิดีโอ...")
            audio = self.r.listen(source) 
            self.r.adjust_for_ambient_noise(source)

        try:
            # แปลงเสียงเป็นข้อความด้วย Google Web Speech API
            command = self.r.recognize_google(audio, language="th-TH")
            print("คำสั่งที่คุณพูดคือ: " + command)

            # เปิดวิดีโอบนเครื่องคอมพิวเตอร์
            if "เปิดวิดีโอ" in command:
                video_name = command.split("เปิดวิดีโอ")[1].strip()
                video_path = f"E:\FinalProject\ทดสอบ.mp4"  # เปลี่ยนเป็น path ของวิดีโอ
                if os.path.exists(video_path):
                    os.startfile(video_path)
                    print(f"กำลังเปิดวิดีโอ {video_name}...")
                else:
                    print(f"ไม่พบวิดีโอชื่อ {video_name} ในเครื่องคอมพิวเตอร์ของคุณ")
            else:
                print("ไม่พบคำสั่งที่ถูกต้อง")

        except sr.UnknownValueError:
            print("ไม่สามารถรับเสียงคำสั่งได้")
        except sr.RequestError:
            print("ไม่สามารถเชื่อมต่อกับ Google Web Speech API ได้")

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    # root.attributes('-fullscreen', True)
    root.resizable(False, False)
    root.mainloop()
