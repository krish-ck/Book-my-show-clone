from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
import trailer as tr

q3=Toplevel()
q3.title("CHOOSE MOVIE")
pic3=PhotoImage(file="C:\\Users\\jayad\\OneDrive\\Pictures\\jseats1.png")
pic11=Label(q3,image=pic3)
pic11.place(x=0,y=0)
q3.geometry("1000x750")
#q3.configure(bg="orange")
a1=Label(q3,text="SELECT MOVIES",font=("System",12),bg="orange",fg="black")
a1.place(x=450,y=40)
a2=Label(q3,text="MOVIE_NAME")
a2.place(x=350,y=80)
a3=Label(q3,text="TICKETS")
a3.place(x=350,y=120)
a4=Label(q3,text="TIMING")
a4.place(x=350,y=160)
a5=Label(q3,text="ADDRESS")
a5.place(x=350,y=200)

#COMBO BOX FOR MOVIE_NAME
movie_name=Combobox(q3)
movie_name["values"]="SELECT","PONNIYIN SELVAN -1","VIKRAM","LOVE TODAY","HEY SINAMIKA","THIRUCHITRAMBALAM"
movie_name.current(0)
movie_name.place(x=500,y=80)
#SPIN BOX FOR TICKETS
age=Spinbox(q3,from_=0,to=25)
age.place(x=500,y=120)

#RADIOBUTTON FOR TIMING
r1=Radiobutton(q3,text="10",value=0)
r1.place(x=500,y=160)
r1=Radiobutton(q3,text="11",value=1)
r1.place(x=560,y=160)
r1=Radiobutton(q3,text="2",value=2)
r1.place(x=620,y=160)
r1=Radiobutton(q3,text="6",value=3)
r1.place(x=680,y=160)

#SCROLLED TEXT FOR ADDRESS
addr=scrolledtext.ScrolledText(q3,height=7,width=14)
addr.place(x=500,y=200)
def sub():
  
        import file4
        messagebox.showinfo("submitted","successfully registerd")
    
def can():
    messagebox.showwarning("cancel","sucessfully canceled")
    q3.destroy()

def clr():
   movie_name.delete(0,'end')
   tickets.delete(0,'end')
   timing.delete(0,'end')
#    addr.delete(0,'end')
bt1=Button(q3,text="submit",command=sub)
bt1.place(x=350,y=380)
bt2=Button(q3,text="cancel",command=can)
bt2.place(x=420,y=380)



bt4=Button(q3,text="clear",command=clr)
bt4.place(x=550,y=380)
