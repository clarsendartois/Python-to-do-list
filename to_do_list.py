import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_text = ("Bookman Old Style", 40, "bold")
font_style_entry = ("Bookman Old Style", 40)

topbar_bg_color = "#32405b"

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
        frame = ctk.CTkFrame(self.window, width=400,
                             height=52, border_width=0)
        frame.place(x=0, y=180)

        task_entry = ctk.CTkEntry(
            frame, width=300, font=font_style_entry, fg_color="white")
        task_entry.place(x=0, y=0)
        task_entry.focus


if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.run()
