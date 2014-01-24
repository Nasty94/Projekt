# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
import locale
from urllib.request import urlopen
from xml.dom.minidom import parse
import webbrowser
import tkinter as lingid
import easygui

def meist():
    messagebox.showwarning(title='About',message='''
   Anastassia Ivanova
    Dmitri Tsumak
All copyrights reserved
         (2013-2014)''')
def valju():
    mexit= messagebox.askyesno(title='Välju', message='Kas Teie olete kindel?')
    if mexit > 0:
        raam.destroy()
        return 

def Link1():
    # loome akna
    raam = Tk()
    raam.title("Otsi uudist")
    raam.geometry("470x400+400+100")
    # Loeme sisse ERR uudiste ülevaate XML kujul 
    f = urlopen('http://uudised.err.ee/uudised_rss.php')
    dom = parse(f) # parse annab lehekülje sisu struktuursel kujul
    pealkirjad = dom.getElementsByTagName("title")

    scrollbar = ttk.Scrollbar(raam, orient="vertical")
    lb = Listbox(raam, width=70, height=20, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)
    scrollbar.pack(side="right", fill="y")
    lb.pack(side="right",fill="both", expand=True)

    info={}
    for pealkiri in pealkirjad:
        link = pealkiri.parentNode.attributes['rdf:about'].value
        tekst = pealkiri.childNodes[0].data
        if lingid != "http://www.etv.ee/" and tekst != "uudised.err.ee - online":
            info[tekst]= link   
            lb.insert(END,tekst)

    def ava_url(event):
        # küsin selle elemendi, mis on listbox'is parasjagu aktiivne
        tekst= lb.get(ACTIVE)
        webbrowser.open(info[tekst])
            
    lb.bind("<Double-Button-1>", ava_url)
    lb.place(x=10,y=20)

    def otsi():
        uudised=[]
        for pealkiri in pealkirjad:
            tekst = pealkiri.childNodes[0].data
            if tekst != "uudised.err.ee - online": 
                uudised.append(tekst)

        def otsija(otsitav, uudised):
            sobivad_uudised=[]
            for sona in uudised:
                if sona[:len(otsitav)]== otsitav:
                    sobivad_uudised.append(sona)

            return sobivad_uudised
       
        otsing = easygui.enterbox("Sisesta otsingu keyword")
        if otsing != None:
            sobivad_uudised=otsija(otsing, uudised)

            for uudised in sobivad_uudised:             
                if len(sobivad_uudised)==1:
                    easygui.msgbox (sobivad_uudised[0])
                else:
                    for j in sobivad_uudised:
                        easygui.msgbox (j) 

    # loome nupu
    nupp = ttk.Button(raam, text="Otsi", command=otsi)
    nupp.place(x=120, y=370, width=100)           
    f.close()

def valik_linn():
    number = lst.curselection()
    if number == ():
        return
    number = int(number[0])
    if number == 0:
        return 'Tallinn'
    elif number == 1:
        return 'Pärnu'
    elif number == 2:
        return 'Tartu'
    elif number == 3:
        return 'Narva'
    elif number == 4:
        return 'Haapsalu'
    elif number == 5:
        return 'Rakvere'
    elif number == 6:
        return 'Valga'
    elif number == 7:
        return 'Kuressaare'
    elif number == 8:
        return 'Viljandi'
    elif number == 9:
        return 'Võru'

def valik_huviala():
    arv = var.get()
    if arv == 1:
        pilti_lisamine('Esiakna pildid/klubi.gif')
        return 'Klubi'
    elif arv == 2:
        pilti_lisamine('Esiakna pildid/kino.gif')
        return 'Kino'
    elif arv == 3:
        pilti_lisamine('Esiakna pildid/teater.gif')
        return 'Teater'
    elif arv == 4:
        pilti_lisamine('Esiakna pildid/sport.gif')
        return 'Sport'
    elif arv == 5:
        pilti_lisamine('Esiakna pildid/bowling.gif')
        return 'Bowling'
    elif arv == 6:
        pilti_lisamine('Esiakna pildid/piljard.gif')
        return 'Piljard'
    else:
        pilti_lisamine('Esiakna pildid/Free.gif')
        return 'Rohkem meelelahustusi'
        

def valik():
    lst = []
    lst.append(valik_linn())
    lst.append(valik_huviala())
    if lst[0] == None or lst[1] == None:
        messagebox.showwarning(title='Tähelepanu',\
                               message='Palun valige linn ja huviala')
    else:
        if lst[0]== "Tartu":
            if lst[1]=="Sport":
                import Links.Tartu.sport
                Links.Tartu.sport.näita()

            elif lst[1]=="Kino":
                import Links.Tartu.kino
                Links.Tartu.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Tartu.klubid
                Links.Tartu.klubid.näita() 

            elif lst[1]=="Teater":
                import Links.Tartu.teater
                Links.Tartu.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Tartu.bowling
                Links.Tartu.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Tartu.piljard
                Links.Tartu.piljard.näita()

            elif lst[1]=="Rohkem":
                import Links.Tartu.muu
                Links.Tartu.muu.näita()

        elif lst[0]=="Tallinn":
            if lst[1]=="Sport":
                import Links.Tallinn.sport
                Links.Tallinn.sport.näita()

            elif lst[1]=="Kino":
                import Links.Tallinn.kino
                Links.Tallinn.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Tallinn.klubid
                Links.Tallinn.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Tallinn.teater
                Links.Tallinn.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Tallinn.bowling
                Links.Tallinn.bowling.näita() # näitab info järjendi elemenditena

            elif lst[1]=="Piljard":
                import Links.Tallinn.piljard
                Links.Tallinn.piljard.näita()

            else:
                import Links.Tallinn.muu
                Links.Tallinn.muu.näita()

        elif lst[0]=="Pärnu":
            if lst[1]=="Sport":
                import Links.Pärnu.sport
                Links.Pärnu.sport.näita() 

            elif lst[1]=="Kino":
                import Links.Pärnu.kino
                Links.Pärnu.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Pärnu.klubid
                Links.Pärnu.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Pärnu.teater
                Links.Pärnu.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Pärnu.bowling
                Links.Pärnu.bowling.näita()#ainult link

            elif lst[1]=="Piljard":
                import Links.Pärnu.piljard
                Links.Pärnu.piljard.näita()

            else:
                import Links.Pärnu.muu
                Links.Pärnu.muu.näita()

        elif lst[0]=="Narva":
            if lst[1]=="Sport":
                import Links.Narva.sport
                Links.Narva.sport.näita()

            elif lst[1]=="Kino":
                import Links.Narva.kino
                Links.Narva.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Narva.klubi
                Links.Narva.klubi.näita()

            elif lst[1]=="Teater":
                import Links.Narva.teater
                Links.Narva.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Narva.bowling
                Links.Narva.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Narva.piljard #sama,mis muu
                Links.Narva.piljard.näita()

            else:
                import Links.Narva.muu
                Links.Narva.muu.näita()

        elif lst[0]=="Rakvere":
            if lst[1]=="Sport":
                import Links.Rakvere.sport
                Links.Rakvere.sport.näita()

            elif lst[1]=="Kino":
                import Links.Rakvere.kino
                Links.Rakvere.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Rakvere.klubid
                Links.Rakvere.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Rakvere.teater
                Links.Rakvere.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Rakvere.bowling
                Links.Rakvere.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Rakvere.piljard    # sama,mis muu
                Links.Rakvere.piljard.näita()

            else:
                import Links.Rakvere.muu #praegu seal ainult bowling
                Links.Rakvere.muu.näita()

        elif lst[0]=="Haapsalu":
            if lst[1]=="Sport":
                import Links.Haapsalu.sport
                Links.Haapsalu.sport.näita()

            elif lst[1]=="Kino":
                import Links.Haapsalu.kino
                Links.Haapsalu.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Haapsalu.klubid
                Links.Haapsalu.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Haapsalu.teater
                Links.Haapsalu.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Haapsalu.bowling
                Links.Haapsalu.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Haapsalu.piljard #sama,mis muu
                Links.Haapsalu.piljard.näita()

            else:
                import Links.Haapsalu.muu
                Links.Haapsalu.muu.näita()

        elif lst[0]=="Valga":
            if lst[1]=="Sport":
                import Links.Valga.sport
                Links.Valga.sport.näita()

            elif lst[1]=="Kino":
                import Links.Valga.kino
                Links.Valga.kino.näita() #ta ei näita "Ä" ja "Ü"(kodeeringu probleem)

            elif lst[1]=="Klubi":
                import Links.Valga.klubid
                Links.Valga.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Valga.teater
                Links.Valga.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Valga.bowling
                Links.Valga.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Valga.piljard 
                Links.Valga.piljard.näita()

            else:
                import Links.Valga.muu
                Links.Valga.muu.näita()

        elif lst[0]=="Kuressaare":
            if lst[1]=="Sport":
                import Links.Kuressaare.sport
                Links.Kuressaare.sport.näita()

            elif lst[1]=="Kino":
                import Links.Kuressaare.kino
                Links.Kuressaare.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Kuressaare.klubid
                Links.Kuressaare.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Kuressaare.teater
                Links.Kuressaare.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Kuressaare.bowling  #sama,mis muu
                Links.Kuressaare.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Kuressaare.piljard #sama,mis muu
                Links.Kuressaare.piljard.näita()

            else:
                import Links.Kuressaare.muu
                Links.Kuressaare.muu.näita()

        elif lst[0]=="Viljandi":
            if lst[1]=="Sport":
                import Links.Viljandi.sport
                Links.Viljandi.sport.näita()

            elif lst[1]=="Kino":
                import Links.Viljandi.kino
                Links.Viljandi.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Viljandi.klubid
                Links.Viljandi.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Viljandi.teater
                Links.Viljandi.teater.näita() 

            elif lst[1]=="Bowling":
                import Links.Viljandi.bowling
                Links.Viljandi.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Viljandi.piljard #sama,mis muu
                Links.Viljandi.piljard.näita()

            else:
                import Links.Viljandi.muu
                Links.Viljandi.muu.näita()

        elif lst[0]=="Võru":
            if lst[1]=="Sport":
                import Links.Võru.sport
                Links.Võru.sport.näita()

            elif lst[1]=="Kino":
                import Links.Võru.kino
                Links.Võru.kino.näita()

            elif lst[1]=="Klubi":
                import Links.Võru.klubid
                Links.Võru.klubid.näita()

            elif lst[1]=="Teater":
                import Links.Võru.teater
                Links.Võru.teater.näita()

            elif lst[1]=="Bowling":
                import Links.Võru.bowling #sama,mis muu
                Links.Võru.bowling.näita()

            elif lst[1]=="Piljard":
                import Links.Võru.piljard
                Links.Võru.piljard.näita()

            else:
                import Links.Võru.muu
                Links.Võru.muu.näita()

kõik_pildid = set()
def pilti_lisamine(nimi):
    tahvel = Canvas(raam, width=100, height=100)
    tahvel.place(x=260, y=40)
    pilt = PhotoImage(file=nimi)
    kõik_pildid.add(pilt)
    tahvel.create_image(50, 50, image=pilt)
    tahvel.pilt = pilt
    
# loome akna
raam = Tk()
raam.title('Vaba aeg')
raam.geometry('430x205+400+200')

# loome sildid
silt1 = Label(raam, text='Valige linn', fg='blue', font=('Purisa', 12, 'bold'))
silt1.place(x=15, y=0)
silt2 = Label(raam, text='Valige huviala', fg='red', font=('Purisa', 12, 'bold'))
silt2.place(x = 125, y = 0)
locale.setlocale(locale.LC_ALL, '')
silt3 = Label(raam,text= strftime('%A, %d. %B %Y')).place(x=260, y=0)

#loome nuppu
nupp = ttk.Button(raam, text='OK', command=valik)
nupp.place(x=350, y=170)

#list box
lst = Listbox(raam, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=15)
lst.insert(1, 'Tallinn')
lst.insert(2, 'Pärnu')
lst.insert(3, 'Tartu')
lst.insert(4, 'Narva')
lst.insert(5, 'Haapsalu')
lst.insert(6, 'Rakvere')
lst.insert(7, 'Valga')
lst.insert(8, 'Kuressaare')
lst.insert(9, 'Viljandi')
lst.insert(10, 'Võru')
lst.place(x=10, y=25)

# radio nuppud
style = ttk.Style()
style.map('C.TRadiobutton',
          foreground=[('pressed', 'red'), ('active', 'black')])
var = IntVar()
klubi = ttk.Radiobutton(raam, text='Klubi',variable=var, value=1, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 27)
kino = ttk.Radiobutton(raam, text='Kino',variable=var, value=2, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 52)
teater = ttk.Radiobutton(raam, text='Teater',variable=var, value=3, style='C.TRadiobutton',\
                        command=valik_huviala).place(x = 150, y = 77)
sport = ttk.Radiobutton(raam, text='Sport',variable=var, value=4, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 102)
bowling = ttk.Radiobutton(raam, text='Bowling',variable=var, value=5, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 127)
piljard = ttk.Radiobutton(raam, text='Piljard',variable=var, value=6, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 152)
meelahustus = ttk.Radiobutton(raam, text='Rohkem',variable=var, value=7, style='C.TRadiobutton',\
                    command=valik_huviala).place(x = 150, y = 177)   
#menuu
menubar=Menu(raam)
menubar.add_command(label='Välju', command=valju)
menubar.add_command(label='Meist', command=meist)
menubar.add_command(label='Maailma uudised', command=Link1)
raam.config(menu=menubar)


# ilmutame akna ekraanile
raam.mainloop()
