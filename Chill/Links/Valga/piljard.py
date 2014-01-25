from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():

    def scrapimine(klass, lehekülg, vahemik):
        page = requests.get(lehekülg)
        page_html = page.text
        q = pq(page_html)
        elemendid = q(klass)
        vajalik = []
        if vahemik == 0:
            vahemik = len(elemendid)
        for i in range(vahemik):
            asi = q(q(klass)[i]).text()
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

    def piljard (klass, lehekülg):
        vajalik = []
        page = requests.get(lehekülg)
        p = page.text.find('Teised mängud</strong>')
        contents = page.text[p + 12:]
        q = pq(contents)
        asi = q(q(klass)[1]).text()
        vajalik.append(asi)
        return(vajalik)
    
    app = Toplevel()
    app.geometry("600x500+400+100")
    app.title("Meelelahustused")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaMuu.gif')
    canvas.create_image(0, 30, image = gif1, anchor = NW)

    
    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=70)
    lst.insert(END,"Valga piljard:")
    lst.insert(END,"       ")

    lehekülg = 'http://www.valgabowling.ee/?page_id=15'
    piljard = piljard('p', lehekülg)

    for i in range(len(piljard)):
        lst.insert(END,piljard[i])
    lst.place(x=50,y=200)

    def Link1():
        webbrowser.open("http://www.valgakultuurikeskus.ee/sundmused/kalender/")
    button1 = ttk.Button(app, text = "Kultuuri sündmused", command = Link1)
    button1.pack()
    button1.place(x=250, y=10, width=115)

    def Link2():
        webbrowser.open("http://www.voorimehepubi.ee/")
    button2 = ttk.Button(app, text = "Voorimehe pubi", command = Link2)
    button2.pack()
    button2.place(x=250, y=60, width=110)

    def Link3():
        webbrowser.open("https://et-ee.facebook.com/events/164949527035193/?ref=22")
    button3 = ttk.Button(app, text = "Paintball", command = Link3)
    button3.pack()
    button3.place(x=250, y=110, width=60)

    app.mainloop()
