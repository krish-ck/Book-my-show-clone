from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

q=Toplevel()
q.title("PAYMENT")
pic=PhotoImage(file="C:\\Users\\jayad\\OneDrive\\Pictures\\jseats1.png")
pic1=Label(q,image=pic)
pic1.place(x=0,y=0)

q.geometry("1000x750")
q.configure(bg="pink")
a1=Label(q,text="PAYMENT",font=("System",12),bg="pink",fg="blue")
a1.place(x=450,y=40)
a2=Label(q,text="TICKET COST")
a2.place(x=350,y=80)
a3=Label(q,text="NO.OF.TICKET")
a3.place(x=350,y=120)
a4=Label(q,text="SNACKS")
a4.place(x=350,y=160)
a5=Label(q,text="TOTAL.NO.OF.COST")
a5.place(x=350,y=200)
a5=Label(q,text="PAYMENT")
a5.place(x=350,y=240)
#ENTRY BOX FOR NAME
r1=Radiobutton(q,text="60",value=0)
r1.place(x=500,y=80)
r2=Radiobutton(q,text="120",value=1)
r2.place(x=550,y=80)
r3=Radiobutton(q,text="180",value=2)
r3.place(x=610,y=80)

#SPIN BOX FOR TICKET
age=Spinbox(q,from_=0,to=25)
age.place(x=500,y=120)
#COMBO BOX FOR SNACKS
col=Combobox(q)
col["values"]="SELECT","SKIP","POP CORN-70rs","VEG PUFF-25rs","COKE-40rs","WATER BOTTLE-20rs","TEA-15rs","COFFEE-20rs"
col.current(0)
col.place(x=500,y=160)

#ENTRY BOX FOR TOTAL.NO.OF.COST
cost=Entry(q,width=20)
cost.place(x=500,y=200)

#COMBO BOX FOR PAYMENT
col1=Combobox(q)
col1["values"]="SELECT","VISA CARD","UPI","DIGITAL WALLETS","PAYTM","DEBT CARD","BHIM(Bharat Interface for Money)","AMAZON PAY","PHONEPE"

col1.current(0)
col1.place(x=500,y=240)
def sub():
    A=name.get()
    B=age.get()
    C=col.get()
    if A=="" or B=="" or C=="":
        messagebox.showerror("invalid","please fill the data")
    else:
        db=m.connect(host="localhost",user="root",password="",db="student_info")
        cur=db.cursor()
        cur.execute("insert into detail1 values('"+A+"','"+B+"','"+C+"')")
        db.commit()
        
        messagebox.showinfo("submitted","successfully registerd")
    
def can():
    messagebox.showwarning("cancel","sucessfully canceled")
    q.destroy()

    
def clr():
    ticket_cost.delete(0,'end')
    no.of.tickets.delete(0,'end')
    snacks.delete(0,'end')
    total.no.of.cost.delete(0,'end')
    payment.delete(0,'end')
#    addr.delete(0,'end')
bt1=Button(q,text="submit",command=sub)
bt1.place(x=350,y=380)
bt2=Button(q,text="cancel",command=can)
bt2.place(x=430,y=380)

bt4=Button(q,text="clear",command=clr)
bt4.place(x=500,y=380)
