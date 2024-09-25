import tkinter
from tkinter import *

root = Tk()
root.title("Hesap Makinesi")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""
def show(value):
    global equation
    equation+=value
    label_sonuc.config(text=equation)

def clear():
    equation= ""
    label_sonuc.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
            equation=""
        except:
            result="error"
            equation= ""
    equation=f"{result}"
    label_sonuc.config(text=result)


label_sonuc= Label(root,width=25,height=2,text="",font=("arial",30))
label_sonuc.pack()
 
Button(root,text="C",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#8b8970", command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#1c0f45",command=lambda:show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1,font=("arial",30,"bold"), bd=1, fg="#1c0f45",bg="#fffaf0",command=lambda:show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"), bd=1, fg="#fff",bg="#8b8970",command=lambda:calculate()).place(x=430,y=400)




root.mainloop()

