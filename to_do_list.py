import tkinter as tk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_text = ("Bookman Old Style", 40, "bold")
font_style_entry = ("Bookman Old Style", 40)
font_style_add_button = ("Bookman Old Style", 35, "bold")
font_style_listbox = ("Bookman Old Style", 35)

standard_bg_color = "#242424"
topbar_bg_color = "#32405b"
listbox_fg_color = "#32405b"
selectbackground_color = "#5a95ff"

text_heading = "ALL TASK"

task_list = []


class ToDoList:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x650+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/clarsen_icon.ico")
        self.window.title("CLARSEN: To-Do List")

        self.heading = self.create_heading()
        self.entry_task = self.create_entry_task()
        self.buttons = self.create_buttons()
        self.listbox = self.create_listbox()
        self.open_taks = self.open_taks_file()

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
        global frame_entry, task_entry
        frame_entry = ctk.CTkFrame(self.window, width=400,
                                   height=52, border_width=0)
        frame_entry.place(x=0, y=180)

        task_entry = ctk.CTkEntry(
            frame_entry, width=300, font=font_style_entry, text_color="black", fg_color="white")
        task_entry.place(x=0, y=0)
        task_entry.focus

    def create_buttons(self):
        add_btn = ctk.CTkButton(
            frame_entry, text="ADD", font=font_style_add_button, width=100, height=50, border_width=2, command=self.add_task)
        add_btn.place(x=300, y=0)

        del_img = ctk.CTkImage(light_image=Image.open(
            "./img/delete.png"), size=(50, 50))
        del_btn = ctk.CTkButton(self.window, text="", image=del_img,
                                border_width=0, width=1, bg_color=standard_bg_color, fg_color=standard_bg_color, command=self.delete_task)
        del_btn.place(relx=0.5, rely=0.5, x=-30, y=250)

    def create_listbox(self):
        global listbox
        frame_listbox = tk.Frame(
            self.window, bd=3, width=700, height=320, bg=listbox_fg_color)
        frame_listbox.place(x=0, y=480)

        listbox = tk.Listbox(frame_listbox, font=font_style_listbox, width=26, height=11,
                             bg=listbox_fg_color, fg="white", cursor="hand2", selectbackground=selectbackground_color)
        listbox.pack(side="left", fill="both", padx=2)

        scrollbar = tk.Scrollbar(frame_listbox)
        scrollbar.pack(side="right", fill="both")

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

    def open_taks_file(self):
        try:
            with open("tasklist.txt", "r") as taskfile:
                tasks = taskfile.readlines()

            for task in tasks:
                if task != "":
                    task_list.append(task)
                    listbox.insert("end", task)
        except:
            file = open("tasklist.txt", "w")
            file.close()

    def add_task(self):
        task = task_entry.get()
        task_entry.delete(0, "end")

        if task:
            with open("tasklist.txt", "a") as taskfile:
                taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert("end", task)

    def delete_task(self):
        listbox.delete("active")
        with open("tasklist.txt", "rt") as taskfile:
            lines = taskfile.readlines()
            for line in lines:
                if listbox.get("active") == line[:-2]:
                    lines.remove(line)
                    taskfile.write(line)

                taskfile.close()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.run()
