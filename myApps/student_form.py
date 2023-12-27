from tkinter import *

root=Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False,False)

Label(root,text="Student Registration Form",font="Poppins 25").pack(pady=50)

Label(text="Name",font="Poppins 11").place(x=100,y=150)
Label(text="Phone",font="Poppins 11").place(x=100,y=200)
Label(text="Gender",font="Poppins 11").place(x=100,y=250)
Label(text="Email",font="Poppins 11").place(x=100,y=300)

#entry
nameValue=StringVar()
phoneValue=StringVar()
genderValue=StringVar()
emailValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,fg='black',border=0,bg='white',font=("Poppins",11))
phoneEntry=Entry(root,textvariable=phoneValue,width=30,fg='black',border=0,bg='white',font=("Poppins",11))
genderEntry=Entry(root,textvariable=genderValue,width=30,fg='black',border=0,bg='white',font=("Poppins",11))
emailEntry=Entry(root,textvariable=emailValue,width=30,fg='black',border=0,bg='white',font=("Poppins",11))

nameEntry.place(x=200,y=150)
phoneEntry.place(x=200,y=200)
genderEntry.place(x=200,y=250)
emailEntry.place(x=200,y=300)

#check button
checkValue=IntVar
checkbtn=Checkbutton(text="Remember me?",variable=checkValue,)
checkbtn.place(x=200,y=340)

Button(text="Register",width=25,height=2,bg='#57a1f8',fg='white',border=0,).place(x=250,y=380)

root.mainloop()
