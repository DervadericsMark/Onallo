from tkinter import *
from math import pi

def eredmenyszamolasa():
    vas_suruseg = 7.8
    fa_suruseg = 0.70
    sugara = int(sugar.get())
    magassaga = int(magassag.get())
    eredmeny = pi * sugara * sugara * magassaga
    terfogat.delete(0, END)
    vashenger.delete(0, END)
    fahenger.delete(0, END)
    terfogat.insert(0, "{:.2f}".format(eredmeny) + " cm3")
    vashenger_tomeg = vas_suruseg * eredmeny
    vashenger.insert(0, "{:.2f}".format(vashenger_tomeg) + " g")
    fahenger_tomeg = fa_suruseg * eredmeny
    fahenger.insert(0, "{:.2f}".format(fahenger_tomeg) + " g")

window = Tk()
window.title("Henger")
sugarfelirata = Label(window, text="Sugár (cm):")
sugarfelirata.grid(row=0, column=0)
sugar = Entry(window)
sugar.grid(row=0, column=1)
magassag_felirata = Label(window, text="Magasság (cm):")
magassag_felirata.grid(row=1, column=0)
magassag = Entry(window)
magassag.grid(row=1, column=1)
szamolgomb = Button(window, text="Kiszámít", command=eredmenyszamolasa)
szamolgomb.grid(row=3, column=1)
terfogat_felirata = Label(window, text="Térfogat:")
terfogat_felirata.grid(row=4, column=0)
terfogat = Entry(window)
terfogat.grid(row=4, column=1)
vashengerfelirata = Label(window, text="Vashenger:")
vashengerfelirata.grid(row=5, column=0)
vashenger = Entry(window)
vashenger.grid(row=5, column=1)
fahengerfelirata = Label(window, text="Fahenger:")
fahengerfelirata.grid(row=6, column=0)
fahenger = Entry(window)
fahenger.grid(row=6, column=1)


window.mainloop()