import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ToDoList:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x650+0+0")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: To-Do List")

        self.image_icon = self.create_image_icon()

    def run(self):
        self.window.mainloop()

    def create_image_icon(self):
        image_icon = tk.PhotoImage(file="./img/task.png")
        self.window.iconphoto(False, image_icon)


if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.run()
