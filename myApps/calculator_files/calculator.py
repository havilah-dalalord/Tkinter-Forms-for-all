from tkinter import *
from tkinter import messagebox
import ast
from tkinter import ttk

root=Tk()
root.title("HZE CALCULATOR")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username == 'admin' and password == '1234':
        screen=Toplevel(root)
        screen.title("Sign Up")
        screen.geometry('570x650+100+200')
        screen.config(bg="#fff")

        equation = ""

        def show(value):
            global equation
            equation+=value
            label_result.config(text=equation)

        def clear():
            global equation
            equation = ""
            label_result.config(text=equation)

        def calculate():
            global equation
            result = ""
            if equation !="":
                try:
                    result= eval(equation)
                except:
                    result = "Incorect Syntax"
                    equation = ""

                label_result.config(text=result)

                label_result= Label(screen, width=25, height=2, text="", font=("Poppins", 30), bg='#43d1d8', fg='#fff')
                label_result.pack()

                Button(screen,text="C", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: clear()).place(x=10,y=150)
                Button(screen,text="/", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("/")).place(x=150,y=150)
                Button(screen,text="%", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("%")).place(x=290,y=150)
                Button(screen,text="X", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("*")).place(x=430,y=150)

                Button(screen,text="1", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#00ff95",command=lambda: show("1")).place(x=10,y=250)
                Button(screen,text="2", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#ffc107",command=lambda: show("2")).place(x=150,y=250)
                Button(screen,text="3", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#0a58ca",command=lambda: show("3")).place(x=290,y=250)
                Button(screen,text="-", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("-")).place(x=430,y=250)

                Button(screen,text="4", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#f28366",command=lambda: show("4")).place(x=10,y=350)
                Button(screen,text="5", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#f8bd42",command=lambda: show("5")).place(x=150,y=350)
                Button(screen,text="6", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#b7ffff",command=lambda: show("6")).place(x=290,y=350)
                Button(screen,text="+", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("+")).place(x=430,y=350)

                Button(screen,text="7", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#e39c6d",command=lambda: show("7")).place(x=10,y=450)
                Button(screen,text="8", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#c0ebff",command=lambda: show("8")).place(x=150,y=450)
                Button(screen,text="9", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#eecd78",command=lambda: show("95")).place(x=290,y=450)
                Button(screen,text="0", width=11, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#e084ff",command=lambda: show("0")).place(x=10,y=550)

                Button(screen,text=".", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#41aaa9",command=lambda: show(".")).place(x=290,y=550)
                Button(screen,text="=", width=5, height=3, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: calculate()).place(x=430,y=450)


    screen.mainloop()

    
img = PhotoImage(file='login.png')
Label(root,image=img,bg='#fff').place(x=50,y=100)

frame=Frame(root,width=350,height=350,bg="#fff")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg="#57a1f8",bg='white',font=("Poppins",23))
heading.place(x=100,y=5)

###----------------------###

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=("Poppins",11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###----------------------###

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=("Poppins",11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

###----------------------###

Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0, command=signin,font=("Poppins",11)).place(x=25,y=204)
label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=("Poppins",9))
label.place(x=75, y=270)

sign_up= Button(frame, width=6, text='Sign Up', border=0, bg='white',cursor='hand2',fg='#57a1fb',font=("Poppins",9))
sign_up.place(x=230, y=268)

root.mainloop()
