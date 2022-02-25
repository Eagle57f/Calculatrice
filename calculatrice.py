
from ast import Expression
from tkinter import *
from math import *
import math
import matplotlib.pyplot as mtl
import numpy as num
from threading import Thread
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 






expression = expecran = x = total = ""
bgclr = "green"
bgclr2 = "red"
list = []



def entree(num, numecran):
    global expression 
    global expecran
    expression = expression + str(num)
    expecran = expecran + str(numecran)
    calcul.set(expecran) 



def appuientree():

    try:
        global expression
        global expecran
        total = str(eval(expression))
        calcul.set(total) 
        expression = total
        expecran = total
    
    except: 
        if expression != "" :
            calcul.set(f" Erreur, ' {expecran} ' n'est pas un calcul valable ou une commande python ")


def feffacer():
    global expression
    global expecran
    expression = ""
    expecran = ""
    calcul.set("")


def variablex(num, numecran):

    try:
        global expression
        global expecran
        global x
        total = str(eval(expression))
        calcul.set(total)
        expression = total
        expecran = total
        x=total

    except: 
        if expression != "" :
            x=""
            calcul.set(f" Erreur, '{expecran}' n'est pas un calcul valable ou une commande python ")



def mode(varmode):
    global bgclr
    global bgclr2

    if varmode == 1:
        print(1)
        bgclr = "green"
        bgclr2 = "red"
        modebutton()   

    

    if varmode == 2:
        print(2)
        bgclr = "red"
        bgclr2 = "green"
        modebutton()


def modebutton():
        mode1 = Button(gui, text=' md1 ', fg='black', bg=bgclr, bd="1", command=lambda: mode(1), height=3, width=7) 
        mode1.grid(row=9, column=0)
        mode2 = Button(gui, text=' md2 ', fg='black', bg=bgclr2, bd="1", command=lambda: mode(2), height=3, width=7) 
        mode2.grid(row=9, column=1)

#def curseurg():
#    position = ecran.index(INSERT)
#    ecran.icursor(position-1)

#def curseurd():
#    position = ecran.index(INSERT)
#    ecran.icursor(position+1)


def plot():

    list = []
    fig = Figure(figsize = (4, 4), dpi = 100)
    global i
    for i in range(101):
        list.append(eval(expression))



    plot1 = fig.add_subplot(111) 


    plot1.plot(list)


    
    canvas = FigureCanvasTkAgg(fig, master = gui)   
    canvas.draw() 
  
    
    canvas.get_tk_widget().grid(row=1, column=11, rowspan=10, columnspan=10) 
  
    



    toolbar = NavigationToolbar2Tk(canvas, gui)
    toolbar.grid(row=0, column=12)



if __name__ == "__main__":

    gui=Tk()

    gui.configure(background="black")

    gui.title("Calculatrice en tkinter")

    gui.geometry("1000x1000")
#    gui.maxsize(width=228, height=499)
#    gui.minsize(width=228, height=427)

    calcul = StringVar()

    #ligne 1

    ecran = Entry(gui, textvariable=calcul, width="20")
    ecran.grid(columnspan=4, ipadx=52, ipady=15)

#chiffres

    #ligne 4
    
    boutton1 = Button(gui, text=' 1 ', fg='black', bg="white", bd="1", command=lambda: entree(1, 1), height=3, width=7) 
    boutton1.grid(row=4, column=0)

    boutton2 = Button(gui, text=' 2 ', fg='black', bg="white", bd="1", command=lambda: entree(2, 2), height=3, width=7) 
    boutton2.grid(row=4, column=1)

    boutton3 = Button(gui, text=' 3 ', fg='black', bg="white", bd="1", command=lambda: entree(3, 3), height=3, width=7) 
    boutton3.grid(row=4, column=2)

    #ligne 5

    boutton4 = Button(gui, text=' 4 ', fg='black', bg="white", bd="1", command=lambda: entree(4, 4), height=3, width=7) 
    boutton4.grid(row=5, column=0)

    boutton5 = Button(gui, text=' 5 ', fg='black', bg="white", bd="1", command=lambda: entree(5, 5), height=3, width=7) 
    boutton5.grid(row=5, column=1)

    boutton6 = Button(gui, text=' 6 ', fg='black', bg="white", bd="1", command=lambda: entree(6, 6), height=3, width=7) 
    boutton6.grid(row=5, column=2)

    #ligne 6

    boutton7 = Button(gui, text=' 7 ', fg='black', bg="white", bd="1", command=lambda: entree(7, 7), height=3, width=7) 
    boutton7.grid(row=6, column=0)

    boutton8 = Button(gui, text=' 8 ', fg='black', bg="white", bd="1", command=lambda: entree(8, 8), height=3, width=7) 
    boutton8.grid(row=6, column=1)

    boutton9 = Button(gui, text=' 9 ', fg='black', bg="white", bd="1", command=lambda: entree(9, 9), height=3, width=7)
    boutton9.grid(row=6, column=2)

    #ligne 7

    boutton0 = Button(gui, text=' 0 ', fg='black', bg="white", bd="1", command=lambda: entree(0, 0), height=3, width=7)
    boutton0.grid(row=7, column=1)


#signes


    plus = Button(gui, text=' + ', fg='black', bg="white", bd="1", command=lambda: entree("+", "+"), height=3, width=7)
    plus.grid(row=4, column=3)

    moins = Button(gui, text=' - ', fg='black', bg="white", bd="1", command=lambda: entree("-", "-"), height=3, width=7)
    moins.grid(row=5, column=3)

    multiplier = Button(gui, text=' * ', fg='black', bg="white", bd="1", command=lambda: entree("*", "*"), height=3, width=7)
    multiplier.grid(row=6, column=3)

    diviser = Button(gui, text=' / ', fg='black', bg="white", bd="1", command=lambda: entree("/", "/"), height=3, width=7) 
    diviser.grid(row=7, column=3)


#special


    racine = Button(gui, text=' √ ', fg='black', bg="white", bd="1", command=lambda: entree("sqrt(", "√("), height=3, width=7) 
    racine.grid(row=2, column=0)

    par1 = Button(gui, text=' ( ', fg='black', bg="white", bd="1", command=lambda: entree("(", "("), height=3, width=7) 
    par1.grid(row=2, column=1) 

    par2 = Button(gui, text=' ) ', fg='black', bg="white", bd="1", command=lambda: entree(")", ")"), height=3, width=7) 
    par2.grid(row=2, column=2)

    egal = Button(gui, text=' = ', fg='black', bg="white", bd="1", command=appuientree, height=3, width=7) 
    egal.grid(row=7, column=2) 

    effacer = Button(gui, text='Effacer', fg='black', bg="white", bd="1", command=feffacer, height=3, width=7) 
    effacer.grid(row=2, column=3) 

    Decimal= Button(gui, text='.', fg='black', bg="white", bd="1", command=lambda: entree('.','.'), height=3, width=7) 
    Decimal.grid(row=7, column=0)

    pi = Button(gui, text=' π ', fg='black', bg="white", bd="1", command=lambda: entree(math.pi,'π'), height=3, width=7) 
    pi.grid(row=1, column=0)

    vari = Button(gui, text=' i (mpl) ', fg='black', bg="white", bd="1", command=lambda: entree('i','i'), height=3, width=7) 
    vari.grid(row=9, column=2)

    mathplot = Button(master=gui, text=' Mathplot ', fg='black', bg="white", bd="1", command=plot, height=3, width=7) 
    mathplot.grid(row=9, column=3)

    #trigonometrie

    cosinus= Button(gui, text=' cos() ', fg='black', bg="white", bd="1", command=lambda: entree('math.cos(','cos('), height=3, width=7) 
    cosinus.grid(row=1, column=1)

    sinus= Button(gui, text=' sin() ', fg='black', bg="white", bd="1", command=lambda: entree('math.sin(','sin('), height=3, width=7) 
    sinus.grid(row=1, column=2)

    tangante= Button(gui, text=' tan() ', fg='black', bg="white", bd="1", command=lambda: entree('math.tan(','tan('), height=3, width=7) 
    tangante.grid(row=1, column=3)

    radian= Button(gui, text=' deg->rad ', fg='black', bg="white", bd="1", command=lambda: entree('math.radians(','rad('), height=3, width=7) 
    radian.grid(row=8, column=3)

    degres= Button(gui, text=' rad->deg ', fg='black', bg="white", bd="1", command=lambda: entree('math.degres(','deg('), height=3, width=7) 
    degres.grid(row=8, column=2)


#variables perso (ligne 8)


    varx = Button(gui, text=' --> x ', fg='black', bg="white", bd="1", command=lambda: variablex(x,x), height=3, width=7) 
    varx.grid(row=8, column=0)

    sortiex = Button(gui, text=' x --> ', fg='black', bg="white", bd="1", command=lambda: entree(x,x), height=3, width=7) 
    sortiex.grid(row=8, column=1)

    #mtlstop = Button(gui, text=' mtlstop ', fg='black', command=lambda: fmtlstop() , height=3, width=7) 
    #mtlstop.grid(row=9, column=1)
    
#modes

    modebutton() 

    def thr():
        gui.mainloop()











if __name__ == '__main__':
    t1=Thread(target = thr()).start()


