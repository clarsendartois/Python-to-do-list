# import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_text = ("Bookman Old Style", 40, "bold")
font_style_entry = ("Bookman Old Style", 40)
font_style_add_button = ("Bookman Old Style", 35, "bold")

topbar_bg_color = "#32405b"
listbox_fg_color = "#32405b"

text_heading = "ALL TASK"


class ToDoList:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x650+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/task.ico")
        self.window.title("CLARSEN: To-Do List")

        self.heading = self.create_heading()
        self.entry_task = self.create_entry_task()
        self.buttons = self.create_buttons()
        self.listbox = self.create_listbox()

    def run(self):
        self.window.mainloop()

    def create_heading(self):
        topbar_img = ctk.CTkImage(light_image=Image.open(
            "./img/topbar.png"), size=(400, 80))
        topbar = ctk.CTkLabel(self.window, text=None, image=topbar_img)
        topbar.pack()

        taskboard_img = ctk.CTkImage(light_image=Image.open(
            "./img/taskboard.png"), size=(50, 50))
        taskboard_img = ctk.CTkLabel(
            self.window, text=None, image=taskboard_img, bg_color=topbar_bg_color)
        taskboard_img.place(x=10, y=10)

        task_img = ctk.CTkImage(light_image=Image.open(
            "./img/task.png"), size=(50, 50))
        task_img = ctk.CTkLabel(
            self.window, text=None, image=task_img, bg_color=topbar_bg_color)
        task_img.place(x=345, y=10)

        heading_text = ctk.CTkLabel(
            self.window, text=text_heading, bg_color=topbar_bg_color, font=font_style_text)
        heading_text.place(x=100, y=15)

    def create_entry_task(self):
        global frame_entry
        frame_entry = ctk.CTkFrame(self.window, width=400,
                                   height=52, border_width=0)
        frame_entry.place(x=0, y=180)

        task_entry = ctk.CTkEntry(
            frame_entry, width=300, font=font_style_entry, text_color="black", fg_color="white")
        task_entry.place(x=0, y=0)
        task_entry.focus

    def create_buttons(self):
        add_btn = ctk.CTkButton(
            frame_entry, text="ADD", font=font_style_add_button, width=100, height=50, border_width=2)
        add_btn.place(x=300, y=0)

    def create_listbox(self):
        frame_listbox = ctk.CTkFrame(
            self.window, border_width=3, width=700, height=320, fg_color=listbox_fg_color)
        frame_listbox.pack(pady=(160, 0))

        # listbox = tk.Listbox(frame_listbox, width=40, height=16, bg="#32405b")
        # listbox.pack(side="left", fill="both", padx=2)
        # # listbox.pack() #(side=LEFT, fill=BOTH, padx=2)

        # textbox = ctk.CTkTextbox(frame_listbox, width=400, corner_radius=0)
        # textbox.pack(side="left", fill="both", padx=2)
        # textbox.insert("0.0", "Some example text!\n" * 50)

        # # insert at line 0 character 0
        # textbox.insert("0.0", "new text to insert")
        # # get text from line 0 character 0 till the end
        # text = textbox.get("0.0", "end")
        # textbox.delete("0.0", "end")  # delete all text
        # # configure textbox to be read-only
        # textbox.configure(state="disabled")


if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.run()
