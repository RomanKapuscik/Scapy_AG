from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.geometry('500x500')
button = ctk.CTkButton(root, text="Click me!", command=root.destroy)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


root.mainloop()
