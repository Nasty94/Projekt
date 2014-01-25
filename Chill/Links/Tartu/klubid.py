from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        page_html = page.text
        q = pq(page_html)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.atlantis.ee/index.php?sisu=yritus&mid=31&lang=est'

    nimetused = scrapimine('div.sisu1 h3', lehekülg)
    aeg = scrapimine('div.teadaandepealkiri1', lehekülg)
    piletid = scrapimine('div.sisu2 p', lehekülg)

    for j in range(len(piletid)):
        asi = piletid[j]
        if '\r\n' in asi:
           piletid[j] = asi.replace('\r\n', '')

    app = Toplevel()
    app.geometry("700x500+400+100")  
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/TartuKlubi.gif')
    canvas.create_image(300,0, image = gif1, anchor = NW)
    
    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=130)
    lst.insert(END,"Atlantis:")
    lst.insert(END, "        ")
    
    for i in range(len(aeg)):
        vajalik = nimetused[i] \
              + ' , ' + aeg[i] \
              + ' , ' + piletid[i]
        lst.insert(END,vajalik)
    lst.insert(END, "         ")
    lst.insert(END,"NB! Teisi klubisid saad vaadata nuppu klõpsamisega")
    lst.place(x=10, y=200)


    def Link():
        webbrowser.open("http://www.atlantis.ee/")
    button = ttk.Button(app, text = "Atlantis", command = Link)
    button.pack()
    button.place(x=20, y=20, width=60)

    def Link1():
        webbrowser.open("http://www.illusion.ee/")
    button1 = ttk.Button(app, text = "Illusion", command = Link1)
    button1.pack()
    button1.place(x=120, y=20, width=60)

    def Link2():
        webbrowser.open("http://www.clubtallinn.ee/")
    button2 = ttk.Button(app, text = "Tallinn", command = Link2)
    button2.pack()
    button2.place(x=20, y=70, width=60)

    def Link3():
        webbrowser.open("http://klubiahi.ee/")
    button3 = ttk.Button(app, text = "Ahi", command = Link3)
    button3.pack()
    button3.place(x=120, y=70, width=60)

    app.mainloop()

