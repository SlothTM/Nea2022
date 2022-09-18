from tkinter import *
import sqlite3
import random
from tkinter import messagebox
import time

def call_reg():
    conn = sqlite3.connect('Test.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS information (
        username text,
        password text,
        transfercode integer
        )""")

    conn.commit()
    conn.close()

    def blank_error():
        messagebox.showwarning("ERROR", "Missing one or more required entries")

    def confirm_error():
        messagebox.showwarning("ERROR", "Passwords do not match")

    def user_length_error():
        messagebox.showwarning("ERROR", "The username isnt within the required region (3-20 characters)")

    def user_repeat_error():
        messagebox.showwarning("ERROR", "Entered username is already in use")

    def user_alphanumeric():
        messagebox.showwarning("ERROR", "The username uses unnacceptable characters make sure there arent any special characters or spaces")

    def pass_length_error():
        messagebox.showwarning("ERROR", "The password isnt within the required region (3-20 characters)")

    def transfer_integer_error():
        messagebox.showwarning("ERROR", "The memorable number must only contain numbers")

    def transfer_length_error():
        messagebox.showwarning("ERROR", "The memorable number isnt within the required region (6-10 characters)")


    def submit():
        conn = sqlite3.connect('Test.db')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS information (
            username text,
            password text,
            transfer integer
            )""")

        c.execute("INSERT INTO information VALUES (:username, :password , :transfer)",
        
            {
                'username' : username.get(),
                'password' : password.get(),
                'transfer' : transfer.get()
            })

        conn.commit()

        conn.close()

        username.delete(0, END)
        password.delete(0, END)
        password_2.delete(0, END)
        transfer.delete(0, END)
        messagebox.showinfo("Info Confirmed", "You have succesfully registered \n (Make sure you note down your memorable number as you'll need it to reset password ;) )")
        time.sleep(1)
        Reg.destroy()

    def last_checks():
        user_check = username.get()
        conn = sqlite3.connect('Test.db')

        c = conn.cursor()

        transfer_check = transfer.get()
        try:
            int(transfer_check)
        except:
            transfer_integer_error()    
        else:
            c.execute("""SELECT * 

            FROM information
            """)
            dupe_check = c.fetchall()
            v = True
            for i in dupe_check:
                if str(i[0]) == user_check:
                    v = False
                    break

            if v == False:
                user_repeat_error()
            else:
                submit()

        conn.commit()
        conn.close()                
                    

    def check():
        user_check = username.get()
        pass_check = password.get()
        pass_2_check = password_2.get()
        transfer_check = transfer.get()


        #BLANK CHECK
        if user_check == "":
            blank_error()
        elif pass_check == "":
            blank_error()
        elif pass_2_check == "":
            blank_error()
        elif transfer_check == "":
            blank_error()

        #CONFIRM CHECK
        elif pass_2_check != pass_check:
            confirm_error()

        #LENGTH CHECKS
        elif len(user_check) < 3:
            user_length_error()
        elif len(pass_check) < 3:
            pass_length_error()
        elif len(user_check) > 20:
            user_length_error()
        elif len(pass_check) > 20:
            pass_length_error()
        elif len(transfer_check) > 10:
            transfer_length_error()
        elif len(transfer_check) < 6:
            transfer_length_error()
        #REPEAT CHECK

        #ALPHANUMERIC CHECK
        elif user_check.isalnum() == False:
            user_alphanumeric() 

        #DATA TYPE CHECK
        else:
            last_checks()
        
    Reg = Tk()  
    Reg.geometry('250x200')  
    Reg.title('Reg window')
    Reg.resizable(False,False)
        
    U_L= Label(Reg, text="Input Username:")
    U_L.grid(row =1, column = 1)
    username = Entry(Reg, width = 30)
    username.grid(row =2, column = 1)

    P_L= Label(Reg, text="Input password:")
    P_L.grid(row =3, column = 1)
    password = Entry(Reg, width = 30)
    password.grid(row =4, column = 1)

    P_L_2= Label(Reg, text="Confirm Password:")
    P_L_2.grid(row =5, column = 1)
    password_2 = Entry(Reg, width = 30)
    password_2.grid(row =6, column = 1)

    C_L = Label(Reg, text = "Memorable number")
    C_L.grid(row =7, column = 1)
    transfer = Entry(Reg, width = 30)
    transfer.grid(row =8, column = 1)

    E_B = Button(Reg, text = "ENTER!", command = check)
    E_B.grid(row =9, column = 1,pady = 10, ipadx  = 100)

    Reg.mainloop()

