from tkinter import *
q=Tk()
q.title("CHOOSE TRAILER")
pic=PhotoImage(file="C:\\Users\\jayad\\OneDrive\\Pictures\\jseats1.png")
pic1=Label(q,image=pic)
pic1.place(x=0,y=0)
q.geometry("1000x750")
q.configure(bg="orange")
def can():
    messagebox.showwarning("cancel","sucessfully canceled")
    q.destroy()
def  ps1():
    import webbrowser as wb
    wb.open_new_tab("https://www.youtube.com/watch?v=D4qAQYlgZQs")
bt1=Button(q,text="PONNIYIN SELVAN -1",command=ps1)
bt1.place(x=400,y=150)
def lt1():
    import webbrowser as wb
    wb.open_new_tab("https://www.youtube.com/watch?v=FaQe8JFGdaM&t=17s")
bt2=Button(q,text="LOVE TODAY ",command=lt1)
bt2.place(x=400,y=200)
def rrr1():
    import webbrowser as wb
    wb.open_new_tab("https://www.youtube.com/watch?v=oO8TTM2FgIA")
bt3=Button(q,text="RRR",command=rrr1)
bt3.place(x=400,y=250)
def vm1():
    import webbrowser as wb
    wb.open_new_tab("https://www.youtube.com/watch?v=OKBMCL-frPU")
bt4=Button(q,text="VIKRAM",command=vm1)
bt4.place(x=400,y=300)
def tm1():
    import webbrowser as wb
    wb.open_new_tab("https://www.youtube.com/watch?v=tNnPHz1u3RM")
bt5=Button(q,text="THIRUCHITRAMBALAM",command=tm1)
bt5.place(x=400,y=350)
