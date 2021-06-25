import tkinter
from tkinter import *
import math
import operator

root = Tk()
root.title("Kalkulator")

def klikTombol(nomer):
    operator = layar.get()
    layar.delete(0, END)
    layar.insert(0, str(operator) + str(nomer))

def hapus():
    layar.delete(0, END)

def samadengan():
    sama = layar.get()
    layar.delete(0, END)
    if math == "tambah":
        layar.insert(0, operator + int(sama))
    if math == "kurang":
        layar.insert(0, operator - int(sama))
    if math == "kali":
        layar.insert(0, operator * int(sama))
    if math == "bagi":
        layar.insert(0, operator / int(sama))
def tambah():
    angkaPertama = layar.get()
    layar.delete(0, END)
    global operator
    global math
    operator = int(angkaPertama)
    math = "tambah"

def kurang():
    angkaPertama = layar.get()
    layar.delete(0, END)
    global operator
    global math
    operator = int(angkaPertama)
    math = "kurang"

def kali():
    angkaPertama = layar.get()
    layar.delete(0, END)
    global operator
    global math
    operator = int(angkaPertama)
    math = "kali"

def bagi():
    angkaPertama = layar.get()
    layar.delete(0, END)
    global operator
    global math
    operator = int(angkaPertama)
    math = "bagi"

layar = Entry(root, width=30, borderwidth=10, bg="powder blue", fg="black")
layar.grid(column=0, row=0, columnspan=4)

tombol1 = Button(root, text="1", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(1))
tombol2 = Button(root, text="2", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(2))
tombol3 = Button(root, text="3", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(3))
tombol4 = Button(root, text="4", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(4))
tombol5 = Button(root, text="5", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(5))
tombol6 = Button(root, text="6", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(6))
tombol7 = Button(root, text="7", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(7))
tombol8 = Button(root, text="8", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(8))
tombol9 = Button(root, text="9", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(9))
tombol0 = Button(root, text="0", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = lambda: klikTombol(0))
tombol00 = Button(root, text="00", padx=18, pady=10, borderwidth=3, bg="powder blue", fg="black")
c = Button(root, text="C", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = hapus)
tambah = Button(root, text="+", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = tambah)
kurang = Button(root, text="-", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = kurang)
bagi = Button(root, text="/", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = bagi)
kali = Button(root, text="X", padx=20, pady=10, borderwidth=3, bg="powder blue", fg="black", command = kali)
samadengan = Button(root, text="=", padx=50, pady=10, borderwidth=3, bg="powder blue", fg="black", command = samadengan)


tombol1.grid(column=0, row=1)
tombol2.grid(column=1, row=1)
tombol3.grid(column=2, row=1)
tombol4.grid(column=0, row=2)
tombol5.grid(column=1, row=2)
tombol6.grid(column=2, row=2)
tombol7.grid(column=0, row=3)
tombol8.grid(column=1, row=3)
tombol9.grid(column=2, row=3)
tombol0.grid(column=0, row=4)
tombol00.grid(column=1, row=4)
c.grid(column=2, row=4)
tambah.grid(column=3, row=1)
kurang.grid(column=3, row=2)
bagi.grid(column=3, row=3)
kali.grid(column=3, row=4)
samadengan.grid(column=2, row=5, columnspan=2)

by = Label(root, text="yoga3911", fg="white", bg="black")
by.grid(column=0, row=5, columnspan=2)


root.mainloop()