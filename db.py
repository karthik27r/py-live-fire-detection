import sqlite3
import account

conn = sqlite3.connect("fireuser.db")
print("Databse created successfully")

try:
    conn.execute("""CREATE TABLE fireuser (user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL, 
    user_email TEXT NOT NULL, 
    user_password TEXT NOT NULL)""")
    
except Exception as e:
    print("Error:", e)
    
print("FireUser Table Loaded")

def  createAcoount(username, password, email):
    
    print("username from dbcon")
    print(username)

    cursor = conn.execute("SELECT user_id FROM fireuser WHERE user_name=?",(username,))
    usernameResult = cursor.fetchall()
    cursor = conn.execute("SELECT user_id FROM fireuser WHERE user_email=?",(email,))
    emailResult = cursor.fetchall()
    if len(usernameResult)>0:
        print("Username already present")
        return "uPresent"
    elif len(emailResult)>0:
        print("Email already present")
        return "ePresent"
    else:
        print("Account Created Successfully")
        conn.execute("INSERT INTO fireuser (user_name, user_email, user_password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        print("User Created Successfully")
        return "success"

def userVerification(username, password):
    print("User Verification Process Start")
    cursor = conn.execute("SELECT user_id FROM fireuser WHERE user_name=? AND user_password=?", (username, password))
    res = cursor.fetchone()
    if res:
        return res[0]
    else:
        return None
    