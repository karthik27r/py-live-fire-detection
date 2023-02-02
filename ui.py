import customtkinter
import tkinter
import account


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("theme.json")


uiApp = customtkinter.CTk()
uiApp.geometry(f"{600}x{500}")

def loginNext():
    uiApp.destroy()
    account.loginScreen()
    
def createAcc():
    uiApp.destroy()
    account.signupScreen()
    

uiApp.title("LiveFire Detection")

title = "LiveFire Detection"
label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

def loginClick():
    textLogin_c = "Processing....."
    loginButton.configure(text=textLogin_c)
    loginNext()
    
def signupClick(self):
    textLogin_c = "Processing....."
    loginButton.configure(text=textLogin_c)
    createAcc()

textLogin = "Log in"
loginButton = customtkinter.CTkButton(master="",text = textLogin, command=loginClick)
loginButton.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

title = "Create Your Account"
label = tkinter.Label(uiApp,text=title, bg="#1E1E1E", foreground="#FFFFFF", font=("montserrat",10), cursor="hand2")
label.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)
label.bind("<Button-1>",signupClick)
# loginButton.pack(padx=20, pady=10)








uiApp.mainloop()

