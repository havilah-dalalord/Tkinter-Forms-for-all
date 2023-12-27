import tkinter
from tkinter import *

root=Tk()
root.title("HZE calculator")
root.geometry('570x650+100+200')
#root.configure(bg='#17161b')
root.configure(bg='#fff')
root.resizable(False,False)

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

label_result= Label(root, width=25, height=2, text="", font=("Poppins", 30), bg='#43d1d8', fg='#fff')
label_result.pack()

Button(root,text="C", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: clear()).place(x=10,y=150)
Button(root,text="/", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("/")).place(x=150,y=150)
Button(root,text="%", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("%")).place(x=290,y=150)
Button(root,text="X", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("*")).place(x=430,y=150)

Button(root,text="1", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#00ff95",command=lambda: show("1")).place(x=10,y=250)
Button(root,text="2", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#ffc107",command=lambda: show("2")).place(x=150,y=250)
Button(root,text="3", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#0a58ca",command=lambda: show("3")).place(x=290,y=250)
Button(root,text="-", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("-")).place(x=430,y=250)

Button(root,text="4", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#f28366",command=lambda: show("4")).place(x=10,y=350)
Button(root,text="5", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#f8bd42",command=lambda: show("5")).place(x=150,y=350)
Button(root,text="6", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#b7ffff",command=lambda: show("6")).place(x=290,y=350)
Button(root,text="+", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: show("+")).place(x=430,y=350)

Button(root,text="7", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#e39c6d",command=lambda: show("7")).place(x=10,y=450)
Button(root,text="8", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#c0ebff",command=lambda: show("8")).place(x=150,y=450)
Button(root,text="9", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#eecd78",command=lambda: show("9")).place(x=290,y=450)
Button(root,text="0", width=11, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#e084ff",command=lambda: show("0")).place(x=10,y=550)

Button(root,text=".", width=5, height=1, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#41aaa9",command=lambda: show(".")).place(x=290,y=550)
Button(root,text="=", width=5, height=3, font=("Poppins",25,"bold"), bd=0,fg="#fff",bg="#dc3545",command=lambda: calculate()).place(x=430,y=450)

root.mainloop()
