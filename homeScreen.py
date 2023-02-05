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
    uiApp.title("LIveFire Dashboard")
    
    id = str(uid)
    
    uiApp.columnconfigure(1, weight=0)
    uiApp.rowconfigure(0, weight=1)

    optionsFrame = customtkinter.CTkFrame(master="", fg_color="transparent", border_color="#DC5F00" ,border_width= 2)
    optionsFrame.configure(width=150)
    optionsFrame.grid(row =0, column=0, sticky='ns')
    optionsFrame.columnconfigure(0, weight=1)
    optionsFrame.rowconfigure(0, weight=1)
    
    homeFrame = customtkinter.CTkFrame(master="",border_color="#Defd00", fg_color="transparent")
    uiApp.grid_columnconfigure(1, weight=1)
    homeFrame.grid(row=0, column=1, sticky = 'nsew')
    homeFrame.columnconfigure(1, weight=1)
    
    
    title = "Welcome "+username+" to LiveFire Detection "
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",20), padx=15, pady=30)
    label.grid(row=0, column=1, sticky = 'nw')
    # label.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)
    
    uiApp.mainloop()