from tkinter import *
q2=Toplevel()
q2.title("TRAILER")
pic=PhotoImage(file="C:\\Users\\jayad\\OneDrive\\Pictures\\movieproject.png")
q2.iconphoto(False,pic)
pic1=Label(q2,image=pic)
pic1.place(x=0,y=0)
q2.geometry("1000x750")
q2.configure(bg="orange")
def can():
    messagebox.showwarning("cancel","sucessfully canceled")
    q2.destroy()

def tr():
    import file5
def bk():
    import file3
bt1=Button(q2,text="TRAILER",command=tr)
bt1.place(x=450,y=350)
bt2=Button(q2,text="BOOK MOVIE",command=bk)
bt2.place(x=550,y=350
