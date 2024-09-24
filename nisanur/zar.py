import tkinter as tk
from tkinter import PhotoImage, Label
import random

def show_image(zar_sonucu):
    img= PhotoImage(file=f"C:/Users/Okul/Desktop/nisanur/zar{zar_sonucu}.png")
    Label.config(image=img)
    Label.image=img

def zar_sonucu():
    zar_sonucu = random.randint(1, 6)  
    etiket1["text"] = f"zar sonucu: {zar_sonucu}"   
    show_image(zar_sonucu)

pencere= tk.Tk()
pencere.title("zar ve resim gösterme")
pencere.geometry("400x600+50+100")
pencere.resizable(width="FALSE", height="FALSE" )

etiket1= tk.Label(pencere, fg="red", text=" sayı üretmek için butona basınız")
etiket1.pack()



button = tk.Button(pencere, text="Rastgele Sayı Üret", command=zar_sonucu)
button.pack(pady=10)

Label = Label(pencere)
Label.pack(pady=20)


pencere.mainloop()