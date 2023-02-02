import customtkinter
import tkinter

def loginScreen():
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("theme.json")

    uiApp = customtkinter.CTk()
    uiApp.geometry(f"{600}x{500}")


    uiApp.title("LiveFire Login")

    title = "Log In To Your Account"
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
    label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    
    uiApp.mainloop()
    
def signupScreen():
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("theme.json")

    uiApp = customtkinter.CTk()
    uiApp.geometry(f"{600}x{500}")


    uiApp.title("LiveFire Signup")

    title = "Create an account"
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
    label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    
    uiApp.mainloop()