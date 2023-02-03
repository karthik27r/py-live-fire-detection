import customtkinter
import tkinter

def ess():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("theme.json")

def homeScreen(uid,username):
    
    print("Welcome to HomeScreen")
    ess()
    uiApp = customtkinter.CTk()
    uiApp.geometry(f"{600}x{500}")
    
    id = str(uid)
    
    title = "Welcome "+username+" to LiveFire Detection "+id
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
    label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    
    uiApp.mainloop()