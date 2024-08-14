from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LEFT
from tkinter import messagebox


def topla():
    sayi1 = metinKutusu1.get()
    sayi2 = metinKutusu2.get()
    sonuc = str(float(sayi1) + float(sayi2))
    sonucEtiketi.config(text=sonuc)
    
def cikar():
    sayi1 = metinKutusu1.get()
    sayi2 = metinKutusu2.get()
    sonuc = str(float(sayi1) - float(sayi2))
    sonucEtiketi.config(text=sonuc)

def carp():
    sayi1 = metinKutusu1.get()
    sayi2 = metinKutusu2.get()
    sonuc = str(float(sayi1) * float(sayi2))
    sonucEtiketi.config(text=sonuc)

def bol():
    sayi1 = metinKutusu1.get()
    sayi2 = metinKutusu2.get()
    if sayi2=='0':
        sonucEtiketi.config(text="Sıfıra bölme hatası!")
        messagebox.showinfo(title="HATA",message="Bölme işleminde bölenin sıfır olma durumu tanımlı değildir. Bu nedenle bölme işleminde bölen veya payda sıfır olamaz.")
    else:
        sonuc = str(round(float(sayi1) / float(sayi2),2))
        sonucEtiketi.config(text=sonuc)

pencere = Tk()
pencere.configure(background="#E2E2E2")
pencere.geometry("330x170")
pencere.title("Hesap Makinesi Uygulaması")

etiket1 = Label(pencere, text="Birinci sayıyı giriniz:", bg="#FFFFFF")
metinKutusu1 = Entry(pencere,text="")
metinKutusu1.insert(string="",index=0)
etiket2 = Label(pencere, text="İkinci sayıyı giriniz  :", bg="#FFFFFF")
metinKutusu2 = Entry(pencere,text="")
metinKutusu2.insert(string="",index=0)
dugme1 = Button(pencere, text="+", bg="#FF6633", fg="#000000",activebackground="#FF0000",activeforeground="#FFFFFF", command=topla)
dugme2 = Button(pencere, text="-", bg="#FF6633", fg="#000000",activebackground="#FF0000",activeforeground="#FFFFFF", command=cikar)
dugme3 = Button(pencere, text="x ", bg="#FF6633", fg="#000000",activebackground="#FF0000",activeforeground="#FFFFFF", command=carp)
dugme4 = Button(pencere, text=" / ", bg="#FF6633", fg="#000000",activebackground="#FF0000",activeforeground="#FFFFFF", command=bol)
etiket3 = Label(pencere, text="", bg="#E2E2E2")
sonucEtiketi = Label(pencere, text="Sonuc", bg="#3A33FF")

etiket1.place(x=25,y=25)
metinKutusu1.place(x=175,y=25)
etiket2.place(x=25,y=50)
metinKutusu2.place(x=175,y=50)
dugme1.place(x=25,y=85)
dugme2.place(x=105,y=85)
dugme3.place(x=175,y=85)
dugme4.place(x=250,y=85)
etiket3.place(x=25,y=125)
sonucEtiketi.place(x=125,y=125)

pencere.mainloop()


