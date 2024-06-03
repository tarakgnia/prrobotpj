import tkinter as tk
from tkinterweb import HtmlFrame

def main():
    root = tk.Tk()
    root.title("Web Page in Tkinter")

    # Set the size of the window
    root.geometry("800x600")

    # Create an HtmlFrame widget
    html_frame = HtmlFrame(root)

    # Pack the HtmlFrame widget into the window
    html_frame.pack(fill="both", expand=True)

    # Load a webpage
    html_frame.load_website("https://www.example.com")

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
