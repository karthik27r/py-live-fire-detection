import customtkinter
import tkinter
import re
import db
import homeScreen

res=""

def essentials():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("theme.json")
        
        
def loginScreen():
    
    essentials()
   
        
    uiApp = customtkinter.CTk()
    uiApp.geometry(f"{600}x{500}")
    uiApp.title("LiveFire Login")

    title = "Log In To Your Account"
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
    label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    
    regBox = customtkinter.CTkFrame(master="", width=300, height=200, corner_radius=15, fg_color="#1E1E1E")
    regBox.place(relx=0.5, rely=0.5, anchor =tkinter.CENTER)
    
    usernameLabel = customtkinter.CTkLabel(master=regBox, text="Username")
    usernameLabel.place(x=20, y=20)
    usernameEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Enter Your Username" )
    usernameEntry.place(x=20, y=45)
    
    passwordLabel = customtkinter.CTkLabel(master=regBox, text="Password")
    passwordLabel.place(x=20, y=85)
    passwordEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Enter Your Password" )
    passwordEntry.place(x=20, y=110)
    
    
            
    def userCheck():
        username = usernameEntry.get()
        password = passwordEntry.get()
        
        res = db.userVerification(username,password)
        
        def gotohome():
            uiApp.destroy()
            homeScreen.homeScreen(res,username)
        
        if res:
            print("login successful")
            usernameEntry.configure(border_color="green")
            passwordEntry.configure(border_color="green")
            loginAccButton.configure(fg_color="green",hover_color="green", text="Login Successful | Processing...")
            uiApp.after(4000, gotohome)
            
        else:
            usernameEntry.configure(border_color="red")
            passwordEntry.configure(border_color="red")
            print("login failed")
            
        
    loginAccButton = customtkinter.CTkButton(master=uiApp, text="Login to Your Account", command= lambda:userCheck())
    loginAccButton.place(relx=0.5, rely=0.65,width=380, anchor=tkinter.CENTER)
    
    uiApp.mainloop()
    
def signupScreen():

    essentials()

    uiApp = customtkinter.CTk()
    uiApp.geometry(f"{600}x{500}")


    uiApp.title("LiveFire Signup")

    title = "Create an account"
    label = customtkinter.CTkLabel( master="", text=title, text_color="#FFFFFF",font=("montserrat",30))
    label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    
    regBox = customtkinter.CTkFrame(master="", width=300, height=300, corner_radius=15, fg_color="#1E1E1E")
    regBox.place(relx=0.5, rely=0.5, anchor =tkinter.CENTER)
    
    usernameLabel = customtkinter.CTkLabel(master=regBox, text="Username")
    usernameLabel.place(x=20, y=20)
    usernameEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Enter Your Username" )
    usernameEntry.place(x=20, y=45)
    
    emailLabel = customtkinter.CTkLabel(master=regBox, text="Email")
    emailLabel.place(x=20, y=85)
    emailEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Enter Your Email" )
    emailEntry.place(x=20, y=110)
    
    passwordLabel = customtkinter.CTkLabel(master=regBox, text="Password")
    passwordLabel.place(x=20, y=150)
    passwordEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Enter Your Password" )
    passwordEntry.place(x=20, y=175)
    
    repasswordLabel = customtkinter.CTkLabel(master=regBox, text="Re-Enter Password")
    repasswordLabel.place(x=20, y=215)
    repasswordEntry = customtkinter.CTkEntry(master=regBox, width=250, placeholder_text="Re-Enter Your Password" )
    repasswordEntry.place(x=20, y=240)
    
    def resDis(res):
        
        if res == "Email-Fail":
            emailEntry.configure(border_color="red",placeholder_text="Error")
            print("Error")
        elif res == "Email-Success":
            emailEntry.configure(border_color="green")
            print("Success")
            
        if res == "Pass-Fail":
            passwordEntry.configure(border_color="red",placeholder_text="Error")
            repasswordEntry.configure(border_color="red",placeholder_text="Error")
            print("Error")
        elif res == "Re-Pass-Fail":
            passwordEntry.configure(border_color="red",placeholder_text="Error")
            repasswordEntry.configure(border_color="red",placeholder_text="Error")
            print("Pattern Error")
        elif res == "Pass-Valid":
            passwordEntry.configure(border_color="green")
            repasswordEntry.configure(border_color="green")
            print("Sucess")

            
    
        
        
    def dbcon(username, password,email):
        
        def gotologin():
            uiApp.destroy()
            loginScreen()
            
            
        res = db.createAcoount(username, password, email)
        if res == "uPresent":
            usernameEntry.configure(border_color="yellow",placeholder_text="username already exists")
            # usernameELabel = customtkinter.CTkLabel(master=regBox, text="Email Already Exists")
            # usernameELabel.place(x=50, y=25)
            
        elif res == "ePresent":
            emailEntry.configure(border_color="yellow",placeholder_text="Email already exists")
            # emailELabel = customtkinter.CTkLabel(master=regBox, text="Email Already Exists")
            # emailELabel.place(x=50, y=90)
        elif res == "success":
            usernameEntry.configure(border_color="green")
            emailEntry.configure(border_color="green")
            createAccButton.configure(fg_color="green",hover_color="green", text="Account Created | Processing...")
            uiApp.after(4000, gotologin)
        
            
        # print("dbpass")
        # print(username)
        # print(email)
        # print(password)        
            
    def validCheck():
        
        usernameEntry.configure(border_color="#DC5F00",placeholder_text="Enter Your username")
        passwordEntry.configure(border_color="#DC5F00",placeholder_text="Enter Your Password")
        repasswordEntry.configure(border_color="#DC5F00",placeholder_text="Re-Enter Your Password")
        emailEntry.configure(border_color="#DC5F00",placeholder_text="Enter Your Email")
        
        username=usernameEntry.get()
        email = emailEntry.get()
        password = passwordEntry.get()
        repassword = repasswordEntry.get()
    
        print(email)
        print(password)
        print(repassword)
        
        count = 0
        
        emailPattern=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        ematch = emailPattern.match(email)
        if ematch:
            res = "Email-Success"
            resDis(res)
            count=count+1
        else:
            res ="Email-Fail"
            resDis(res)
 
    
        passPattern = "^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,}$"
        match = re.match(passPattern, password)
        reMatch = re.match(passPattern, repassword)
    
        if match and reMatch:
            if password == repassword:
                res = "Pass-Valid"
                resDis(res)
                count=count+1
                
            else:
                res="Pass-Fail"
                resDis(res)
        else:
            res="Re-Pass-Fail"
            resDis(res)
            
        if count == 2:
            count = 0
            dbcon(username,password,email)
        else:
            count=0
            print("")
        
    
    createAccButton = customtkinter.CTkButton(master=uiApp, text="Create Your Account", command= lambda:validCheck())
    createAccButton.place(relx=0.5, rely=0.85,width=380, anchor=tkinter.CENTER)
    

    
    
    
    uiApp.mainloop()