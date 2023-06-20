from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
import pymysql as m

q=Toplevel()
q.title("movie")
pic=PhotoImage(file="C:\\Users\\jayad\\OneDrive\\Pictures\\movieproject.png")
q.iconphoto(False,pic)
pic1=Label(q,image=pic)
pic1.place(x=0,y=0)
q.geometry("500x500")
q.configure(bg="orange")
a1=Label(q,text="BOOK MY SHOW",font=("System",12),bg="white",fg="black")
a1.place(x=140,y=40)
a2=Label(q,text="NAME")
a2.place(x=20,y=80)
a3=Label(q,text="PHONE_NUMBER")
a3.place(x=20,y=120)
a4=Label(q,text="E_MAIL ID")
a4.place(x=20,y=160)

#ENTRY BOX FOR NAME
name=Entry(q,width=20)
name.place(x=140,y=80)
#ENTRY BOX FOR PHONE_NUMBER
phone_number=Entry(q,width=20)
phone_number.place(x=140,y=120)
#ENTRY BOX FOR E-MAIL ID
e_mailid=Entry(q,width=20)
e_mailid.place(x=140,y=160)
#ENTRY BOX FOR OTP





def sub():
    A=name.get()
    B=phone_number.get()
    C=e_mailid.get()
    if A=="" or B=="" or C=="":                                                                                                                               
        messagebox.showerror("invalid","please fill the data")
    else:
        db=m.connect(host="localhost",user="root",password="",db="jk")
        cur=db.cursor()
        cur.execute("insert into sreekrishna values('"+A+"','"+B+"','"+C+"')")
        db.commit()
        
        messagebox.showinfo("submitted","successfully registered")
    
def can():
    messagebox.showwarning("cancel","sucessfully canceled")
    q.destroy()
def nt():
    import file2
def clr():
    name.delete(0,'end')
    phone_number.delete(0,'end')
    email_id.delete(0,'end')
#    addr.delete(0,'end')

def otp1():
    a5=Label(q,text="OTP")              
    a5.place(x=20,y=200)
    otp=Entry(q,width=20)
    otp.place(x=140,y=200)
    if otp==1234:
        print("successfully register")
    else:
        print("invalid number")
    bt3=Button(q,text="next_",command=nt)
    bt3.place(x=260,y=380)
    
bt1=Button(q,text="submit",command=sub)

    
bt1.place(x=100,y=380)
bt2=Button(q,text="cancel",command=can)
bt2.place(x=180,y=380)



bt4=Button(q,text="clear",command=clr)
bt4.place(x=320,y=380)
bt4=Button(q,text="getotp",command=otp1)
bt4.place(x=390,y=380)
