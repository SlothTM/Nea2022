from tkinter import *
import sqlite3
from tkinter import messagebox

def call_Fog():
    Fog = Tk()  
    Fog.geometry('250x120')  
    Fog.title('Fog window')
    Fog.resizable(False,False)

    def Reset():
        Res = Tk()  
        Res.geometry('250x120')  
        Res.title('Res window')
        Res.resizable(False,False)
        def blank_error():
            messagebox.showwarning("ERROR", "Missing one or more required entries")

        def confirm_error():
            messagebox.showwarning("ERROR", "Passwords do not match")
        
        def pass_length_error():
            messagebox.showwarning("ERROR", "The password isnt within the required region (3-20 characters)")

        def check():
            p1_check = password1.get()
            p2_check = password2.get()
            user_check = username.get()

            if p1_check == "":
                blank_error()
            
            elif len(p1_check) < 3:
                pass_length_error()
            
            elif len(p1_check) > 20:
                pass_length_error()
            
            elif p1_check != p2_check:
                confirm_error()

            else:
                Reset_Password(p1_check,user_check)

        def Reset_Password(pas1,user):
            
            user_check = username.get()
            pass_check = password1.get()
            conn = sqlite3.connect('Test.db')

            print(user_check)

            c = conn.cursor()
            update_q = """UPDATE information SET password = ? where username = ?"""
            data = (pas1,user)
            c.execute(update_q,data)
            conn.commit
            conn.close
            
        global password1
        global password2

        P1= Label(Res, text="Input new password")
        P1.grid(row =1, column = 1)
        password1 = Entry(Res, width = 30)
        password1.grid(row =2, column = 1)

        P2= Label(Res, text="Confirm new password")
        P2.grid(row =3, column = 1)
        password2 = Entry(Res, width = 30)
        password2.grid(row =4, column = 1)

        E_B = Button(Res, text = "ENTER!", command = check)
        E_B.grid(row =9, column = 1,pady = 10, ipadx  = 100)

    def submit():
        user_check = username.get()
        transfer_check = transfer_num.get()

        conn = sqlite3.connect('Test.db')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS information (
            username text,
            password text,
            transfer integer
            )""")

        c.execute("""SELECT *

            FROM information
            """)

        u_check = c.fetchall()

        for i in u_check:
            if str(i[0]) == user_check:
                if str(i[2]) == transfer_check:
                    Reset()
                    break
                else:
                    messagebox.showwarning("WRONG","Invalid Memorable Number")
                    break
            else:
                messagebox.showwarning("WRONG","Username doesnt exist")
                break

        conn.commit()

        conn.close()
        
    global username        
    U_L= Label(Fog, text="Input Username:")
    U_L.grid(row =1, column = 1)
    username = Entry(Fog, width = 30)
    username.grid(row =2, column = 1)

    T_L= Label(Fog, text="Input Memorable Number:")
    T_L.grid(row =3, column = 1)
    transfer_num = Entry(Fog, width = 30)
    transfer_num.grid(row =4, column = 1)

    E_B = Button(Fog, text = "ENTER!", command = submit)
    E_B.grid(row =9, column = 1,pady = 10, ipadx  = 100)


    Fog.mainloop()

    conn = sqlite3.connect('Test.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS information (
        username text,
        password text
        )""")


    conn.commit()

    conn.close()

call_Fog()