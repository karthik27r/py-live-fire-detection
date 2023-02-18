import customtkinter
from tkinter import filedialog
import detection

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

    def openAfile():
        uiApp.filename = filedialog.askopenfilename(initialdir="", title="Open a Video File")
        fname = uiApp.filename
        print(fname)
        detection.vidDetection(fname)
        
    def homePage():
        homeFrame = customtkinter.CTkFrame(master="",border_color="#Defd00", fg_color="transparent")
        uiApp.grid_columnconfigure(1, weight=1)
        homeFrame.grid(row=0, column=1, sticky = 'nsew')
        homeFrame.columnconfigure(1, weight=1)
    
    
        title = "Welcome "+username+" to LiveFire Detection "
        label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",20), padx=15, pady=30)
        label.grid(row=0, column=1, sticky = 'nw')
        # label.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)
      
    def livePage():
        liveFrame = customtkinter.CTkFrame(master="",border_color="#Defd00", fg_color="transparent")
        uiApp.grid_columnconfigure(1, weight=1)
        liveFrame.grid(row=0, column=1, sticky = 'nsew')
        liveFrame.columnconfigure(1, weight=1)
    
    
        title = "Detect Live Fire"
        label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",20), padx=15, pady=30)
        label.grid(row=0, column=1, sticky = 'nw')
        # label.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)
        
    def picPage():
        picFrame = customtkinter.CTkFrame(master="",border_color="#Defd00", fg_color="transparent")
        uiApp.grid_columnconfigure(1, weight=1)
        picFrame.grid(row=0, column=1, sticky = 'nsew')
        picFrame.columnconfigure(1, weight=1)
    
    
        title = "Detect Fire in a Picture"
        label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",20), padx=15, pady=30)
        label.grid(row=0, column=1, sticky = 'nw')
        # label.place(relx=0.6, rely=0.1, anchor=tkinter.CENTER)
        
    def vidPage():
        vidFrame = customtkinter.CTkFrame(master="",border_color="#Defd00", fg_color="transparent")
        uiApp.grid_columnconfigure(1, weight=1)
        vidFrame.grid(row=0, column=1, sticky = 'nsew')
        vidFrame.columnconfigure(1, weight=1)
    
    
        title = "Detect Fire in a Video"
        label = customtkinter.CTkLabel( master=vidFrame, text=title, text_color="#FFFFFF",font=("montserrat",25), padx=15, pady=30)
        label.grid(row=1, column=1, sticky = 'nw')
        
        userChoice = "Please Insert a Video"
        userChoiceLabel = customtkinter.CTkLabel( master=vidFrame, text=userChoice, text_color="#FFFFFF",font=("montserrat",18), padx=15, pady=20)
        userChoiceLabel.grid(row =2, column =1,sticky ="nsew")
        
        userChoiceButton = customtkinter.CTkButton( master=vidFrame, text = "Insert Video File", font=("montserrat",15), command= lambda:openAfile())
        userChoiceButton.grid(row=3, column=1, columnspan=2, sticky='n')

        
    optionsFrame = customtkinter.CTkFrame(master="", border_color="#DC5F00" ,border_width= 2)
    optionsFrame.configure(width=150)
    optionsFrame.grid(row =0, column=0, sticky='ns')
    optionsFrame.columnconfigure(0, weight=1)
    optionsFrame.rowconfigure(0, weight=1)
    
    def hideIndicate():
        homeBtn.configure(fg_color="transparent")
        liveBtn.configure(fg_color="transparent")
        picBtn.configure(fg_color="transparent")
        vidBtn.configure(fg_color="transparent")
        
    def indicate(inp,page):
        hideIndicate()
        inp.configure(fg_color='#DC5F00', hover_color='#DC5F00')
        page()
    
    homeBtn = customtkinter.CTkButton(master=optionsFrame, text="Home", fg_color="#DC5F00", command= lambda:indicate(homeBtn, homePage), hover_color="#383838")
    homeBtn.place(relx=0.025, rely=0.1)
    liveBtn = customtkinter.CTkButton(master=optionsFrame, text="Live Detection", fg_color="transparent", command= lambda:indicate(liveBtn, livePage), hover_color="#383838")
    liveBtn.place(relx=0.025, rely=0.25)
    picBtn = customtkinter.CTkButton(master=optionsFrame, text="Photo Detection", fg_color="transparent", command= lambda:indicate(picBtn, picPage), hover_color="#383838")
    picBtn.place(relx=0.025, rely=0.325)
    vidBtn = customtkinter.CTkButton(master=optionsFrame, text="Video Detection", fg_color="transparent", command= lambda:indicate(vidBtn, vidPage), hover_color="#383838")
    vidBtn.place(relx=0.025, rely=0.4)
    
    homePage()
    
    uiApp.mainloop()