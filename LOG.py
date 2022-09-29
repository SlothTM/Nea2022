from tkinter import *
import sqlite3
from tkinter import messagebox

def call_log():
    Log = Tk()  
    Log.geometry('250x120')  
    Log.title('Log window')
    Log.resizable(False,False)

    def submit():
        user_check = username.get()
        pass_check = password.get()

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
                if str(i[1]) == pass_check:
                    username.delete(0, END)
                    password.delete(0, END)
                    messagebox.showinfo("CORRECT","lOGIN SUCCESFUL.")
                    Log.destroy()
                else:
                    messagebox.showwarning("WRONG","Invalid username or password")

        conn.commit()

        conn.close()
        
        
    U_L= Label(Log, text="Input Username:")
    U_L.grid(row =1, column = 1)
    username = Entry(Log, width = 30)
    username.grid(row =2, column = 1)

    P_L= Label(Log, text="Input password:")
    P_L.grid(row =3, column = 1)
    password = Entry(Log, width = 30)
    password.grid(row =4, column = 1)

    E_B = Button(Log, text = "ENTER!", command = submit)
    E_B.grid(row =9, column = 1,pady = 10, ipadx  = 100)


    Log.mainloop()

    conn = sqlite3.connect('Test.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS information (
        username text,
        password text,
        transfer integer
        )""")


    conn.commit()

    conn.close()

