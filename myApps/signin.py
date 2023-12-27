from tkinter import *
from tkinter import messagebox
import ast
from tkinter import ttk

root=Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username == 'admin' and password == '1234':
        screen=Toplevel(root)
        screen.title("Sign Up")
        screen.geometry('500x500')
        #screen.config(bg="teal")

        Label(screen,text="Secret",font="Poppins 11").place(x=100,y=150)
        
        #entry
        secretValue=StringVar()

        secretEntry=Entry(screen,textvariable=secretValue,width=30,fg='black',border=0,bg='white',font=("Poppins",11))

        secretEntry.place(x=200,y=150)
        
        #check button
        checkValue=IntVar
        checkbtn=Checkbutton(screen,text="That is my secret",variable=checkValue,)
        checkbtn.place(x=200,y=340)

        Button(screen,text="Register",width=25,height=2,bg='#57a1f8',fg='white',border=0,).place(x=250,y=380)

    if username == 'Nightspy2907' and password == '2907': 
        screen=Toplevel(root)
        screen.title("Sign Up")
        screen.geometry('925x500+300+200')
        screen.config(bg="teal")

        Label(screen,text='Hello Everyone!!! This is the Nightspy team', bg='teal', fg='white',font=('Poppins',20)).pack(expand=True)


    if username == 'UANE' and password == 'eri_the##gi**l':
        screen = Toplevel(root)
        screen.title("Sign Up")
        screen.geometry('925x500+300+200')
        screen.config(bg="teal")

        Label(screen, text='Hello Everyone!!! This is the The Girls learning team', bg='teal', fg='white',font=('Poppins', 20)).pack(expand=True)


    #elif username!='admin' and password!='1234':
        #messagebox.showerror("Invalid","Invalid username or Password")

    #elif password!='1234':
        #messagebox.showerror("Invalid","Invalid password")
        
    #elif username!='Nightspy2907' and password!='2907':
        #messagebox.showerror("Invalid","Invalid username or Password")

    #elif password!='2907':
        #messagebox.showerror("Invalid","Invalid password")

    screen.mainloop()

    
img = PhotoImage(file='login (1).png')
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
