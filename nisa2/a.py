
#Pencere Oluşturma
"""from tkinter import *
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Pencere Oluşturma")
tk.geometry("400x250")
Label(tk,text="Tkinter Pencere Oluşturma").pack()

tk.mainloop()"""

#Label ve Fontlar

"""from tkinter import *
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Label")
tk.geometry("400x300")
 
Label(tk,text="Verdana",font="Verdana 12", bg="red", fg="white").pack()
Label(tk,text="Verdana Bold",font="Verdana 12 bold underline").pack()
Label(tk,text="Verdana italic",font="Verdana 12 italic").pack()
Label(tk,text="Verdana roman",font="Verdana 12 roman").pack()
 
Label(tk,text="Helvetica",font="Helvetica 12", bg="green", fg="yellow").pack()
Label(tk,text="Helvetica bold",font="Helvetica 12 bold").pack()
Label(tk,text="Helvetica italic",font="Helvetica 12 italic").pack()
Label(tk,text="Helvetica roman",font="Helvetica 12 roman").pack()
 
Label(tk,text="Times",font="Times 12", bg="black", fg="white").pack()
Label(tk,text="Times Bold",font="Times 12 bold").pack()
Label(tk,text="Times italic",font="Times 12 italic").pack()
Label(tk,text="Times roman",font="Times 12 roman").pack()
 
tk.mainloop()"""


#Buton Ekleme

"""from tkinter import *
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Buton Ekleme")
tk.geometry("400x250")
 
def buton():
    lbl["text"] = "1. Butona Tıklandı"
def buton2():
    lbl["text"] = "2. Butona tıklandı"
 
btn = Button(tk,
            text="Buton",
            padx="20",pady="5",
            command=buton)
btn.pack()
 
btn2 = Button(tk,
            text = "Buton 2", font="Times 12 bold",
            padx="25", pady="10", 
            bg="red", fg="white", cursor="hand2",
            activeforeground="green", activebackground="black",
            command=buton2)
btn2.pack()
 
lbl = Label(tk)
lbl.pack()
 
tk.mainloop()"""

#Messagebox

"""from tkinter import *
from tkinter import messagebox
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Messagebox")
tk.geometry("400x250")
 
def show():
    messagebox.showinfo("Başlık", "İnfo")
    messagebox.showerror("Başlık","Hata")
    messagebox.showwarning("Başlık","Uyarı")
 
def ask():
    messagebox.askyesno("Başlık","askyesno")
    messagebox.askokcancel("Başlık","askokcancel")
    messagebox.askquestion("Başlık","askquestion")
    messagebox.askretrycancel("Başlık","askretrycancel")
    messagebox.askyesnocancel("Başlık","askyesnocancel")
 
L1 = Label(tk,text="MESSAGEBOX",font="Verdana 12 bold")
L1.pack()
B1 = Button(tk, text="show", command=show)
B1.pack()
B2 = Button(tk, text="ask", command=ask)
B2.pack()
 
tk.mainloop()"""

#Entry Kullanımı

"""from tkinter import *
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Entry")
tk.geometry("400x250")
 
lbl = Label(tk,text="Entry")
lbl.pack()
 
entry = Entry(tk, width=25)
entry.pack()
entry2 = Entry(tk,textvariable=StringVar(), show='*', width=25)
entry2.pack()
tk.mainloop()"""

#Widget Hizalama

"""from tkinter import *
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Hizalama")
tk.geometry("400x250")
 
# Grid
G1 = Label(tk, text="Grid Label 1")
G1.grid(row=0, column=0, pady=5, padx=5)
G2 = Button(tk, text="Grid Button 1")
G2.grid(row=0, column=1, pady=5, padx=5)
G3 = Label(tk, text="Grid Label 2")
G3.grid(row=1, column=0)
G4 = Button(tk, text="Grid Button 2")
G4.grid(row=1, column=1)
 
# Place
P1 = Label(tk, text="Place Label")
P1.place(x=170,y=140)
P2 = Button(tk, text="Place Button")
P2.place(x=165,y=165)
 
tk.mainloop()"""

#Görsel Ekleme

"""from tkinter import *
from PIL import ImageTk, Image
 
tk = Tk()
tk.title("Yazılım Furyası | Tkinter - Resim Ekleme ve Boyutlandırma")
tk.geometry("500x500")
 
resim = ImageTk.PhotoImage(Image.open("Desktop/cat.png"))
Label(tk,image=resim).pack()
 
# Yeniden Boyutlandırma
image = Image.open("Desktop/cat.png")
# resize(width, height)
resize_image = image.resize((110,160))
 
img = ImageTk.PhotoImage(resize_image)
Label(tk,image=img).pack()
 
tk.mainloop()"""

#Kullanıcı Giriş Ekranı Yapımı

"""from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
 
 
# Tk sınıfını 'window'a atadık.
window = Tk()
 
# Pencere Başlığı
window.title("Kullanıcı Giriş Ekranı")
 
# Pencereye ikon ekleme
window.iconbitmap("Desktop/scorp.ico")
 
window.geometry("390x220")
 
# Pencerenin yeniden boyutlandırılmasını engelledik
window.resizable(width=False, height=False)
 
 
# Resim ekledik
resim = ImageTk.PhotoImage(Image.open("Desktop/login.jpg"))
lresim = Label(window,image=resim)
lresim.place(x=250,y=10)
 
 
# Hata mesajımızı bu Label'e yazdıracaz
L3 = Label(window)
L3.place(x=148,y=200)
 
def giris():
    # E1 ve E2 adlı Entry'e girilen değeri, get() fonksiyonuyla çekip sorguluyoruz. 
    if (E1.get() == str("admin")) and (E2.get() == str("1234")):
        L3['text'] = ("Giriş Başarılı...")
        messagebox.showinfo("Başlık", "Giriş Başarılı")
        print("başarılı")
    else:
        L3['text'] = ("Hatalı Giriş !")
        messagebox.showerror("Hata Başlık", "Hatalı Giriş")
 
L1 = Label(window, text="Kullanıcı Adı")
L1.place(x=75, y=15)
 
E1 = Entry(window, width=25)
E1.place(x=77,y=45)
 
L2 = Label(window, text="Şifre")
L2.place(x=75, y=80)
 
E2 = Entry(window, textvariable=StringVar(),show='*', width=25)
E2.place(x=77, y=110)
 
bt = Button(window, text="Giriş Yap", padx="20",pady="5", command=giris)
bt.place(x=75,y=150)
 
window.mainloop()"""