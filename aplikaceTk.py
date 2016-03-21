# -*- coding: utf8 -*- 
"""Ukazkovy priklad vyroby aplikace v Tkinter.
Musi byt ulozeno v kodovani utf8."""


from tkinter import *

class Hodnota:
    "Trida promennych, ktere se promiskuitne pouzivaji v nekolika funkcích."

    text=None
    vstup=None
    vek=None
    jazykPy=None
    jazykC=None
    jazykX=None


def start():
    "start vseho"
    
    hlavniOkno=Tk()
    hlavniOkno.title('Aplikace v Tk')
    # hlavniOkno.iconbitmap('systemova_ikona.ico')
    
    frame=Frame(hlavniOkno)
    frame.pack(fill=BOTH, expand=YES)
    nabidka(frame, hlavniOkno)
    oblastText(frame)
    vstupniRadek(frame)
    mezera(10)
    vek(frame)
    linka(frame)
    jazyk(frame)


def hello():
    "Slepa funkce, jen aby tu neco bylo."
    
    hlaska="hello, ja jsem funkce"
    print(hlaska)
    hodnota.text.insert(END, hlaska+'\n')


def tisk():
    "Tiskne hodnoty promennych svazanych s jednotlivymi widgety."

    print("-"*50)
    print("hodnota.vstup=", hodnota.vstup.get())
    print("hodnota.vek=", hodnota.vek.get())
    print("hodnota.jazykPy=", hodnota.jazykPy.get())
    print("hodnota.jazykC=", hodnota.jazykC.get())
    print("hodnota.jazykX=", hodnota.jazykX.get())

    n="\n"
    t= "-"*50+n
    t=t+ "hodnota.vstup="+ str(hodnota.vstup.get())+n
    t=t+ "hodnota.vek="+ str(hodnota.vek.get())+n
    t=t+ "hodnota.jazykPy="+ str(hodnota.jazykPy.get())+n
    t=t+ "hodnota.jazykC="+ str(hodnota.jazykC.get())+n
    t=t+ "hodnota.jazykX="+ str(hodnota.jazykX.get())+n
    hodnota.text.insert(END, t)

    
def nabidka(frame, root):
    "Vyrabi menu."

    menuLista = Menu(frame)
    menuSoubor=Menu(menuLista)
    menuSoubor.add_command(label="Otevřít", command=hello)
    menuSoubor.add_command(label="Uložit", command=hello)
    menuSoubor.add_command(label="Tisk", command=tisk)
    menuSoubor.add_separator()
    menuSoubor.add_command(label="Exit", command=root.destroy)

    menuLista.add_cascade(label="Soubor", menu=menuSoubor)
    menuLista.add_command(label="Tisk proměnných", command=tisk)
    menuLista.add_command(label="Nápověda", command=hello)

    root.config(menu=menuLista)


def oblastText(root):
    "Vyrabi oblast, kde se muze psat jako v poznamkovem bloku."
    
    textRamec=Frame(root)
    textRamec.pack(fill=BOTH, expand=YES)
    hodnota.text=Text(textRamec, height=10, width=50, wrap=NONE)
    posuvnik = Scrollbar(textRamec,command =hodnota.text.yview)
    hodnota.text.configure(yscrollcommand=posuvnik.set)
    posuvnik.pack(side=RIGHT, fill=Y)
    hodnota.text.pack(fill=BOTH, expand=YES)


def vstupniRadek(root):
    "Definuje jendoradkovy vstup."

    mezera(10)
    vstupRamec=Frame(root)
    hodnota.vstup=StringVar()
    hodnota.vstup.set("toto je vstup")
    Label(vstupRamec, text='Jméno').pack(side=LEFT)
    vstup=Entry(vstupRamec, width=40, textvariable=hodnota.vstup)
    vstup.pack(side=LEFT)
    vstupRamec.pack()


def linka(root):
    "oddelovaci linka"
    
    mezera(10)
    li=Frame(root, relief=RAISED, height=2, bd=1)
    li.pack(fill=BOTH)
    mezera(10)


def mezera(vyska):
    "Nastavitelna mezera"
    
    Frame(height=vyska).pack()
    

def vek(root):
    "Prepinace veku."

    hodnota.vek=IntVar()
    hodnota.vek.set(0)
    vekRamec=Frame(root)
    Label(vekRamec, text='Tvůj věk').pack(side=LEFT)
    r1=Radiobutton(vekRamec, text='<12', value=1, variable=hodnota.vek)
    r1.pack(side=LEFT)
    r1=Radiobutton(vekRamec, text='<15', value=2, variable=hodnota.vek)
    r1.pack(side=LEFT)
    r1=Radiobutton(vekRamec, text='<100', value=3, variable=hodnota.vek)
    r1.pack(side=LEFT)
    vekRamec.pack()


def jazyk(root):
    "Zaskrtavatka oblibeneho jazyka."

    jazykRamec=Frame(root)
    hodnota.jazykPy=IntVar()
    Label(jazykRamec, text='Tvůj oblíbený jazyk').pack(side=LEFT)
    Checkbutton(jazykRamec, text='Python', state=ACTIVE, variable=hodnota.jazykPy).pack(side=LEFT)
    hodnota.jazykPy.set(1)
    hodnota.jazykC=IntVar()
    Checkbutton(jazykRamec, text='C', variable=hodnota.jazykC).pack(side=LEFT)
    hodnota.jazykX=IntVar()
    Checkbutton(jazykRamec, text='X', variable=hodnota.jazykX).pack(side=LEFT)
    jazykRamec.pack(side=TOP)


hodnota=Hodnota()
start()
mainloop()

