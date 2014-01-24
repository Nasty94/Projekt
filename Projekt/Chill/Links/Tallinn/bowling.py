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

    avatud = scrapimine('span.text13', 'http://www.kuulsaal.ee/est/hinnad/bowling/?')
    hinnad_bowling = scrapimine('tr td', 'http://www.kuulsaal.ee/est/hinnad/bowling/?')
    piljard = (scrapimine('span.w2text', 'http://www.kuulsaal.ee/est/hinnad/piljard/?'))[1].split("/")

    app = Toplevel()
    app.geometry("600x550+400+100")
    app.title("Meelelahutus")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnMuu.gif')
    canvas.create_image(150, 15, image = gif1, anchor = NW)
    
    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=90,heigh=15)
    lst.insert(END,"Kuusalu Bowling:")
    lst.insert(END,"        ")
    lst.insert(END,avatud[0])
    lst.insert(END,"        ")
    for i in range(0, len(hinnad_bowling)-10, 4):
        vajalik = hinnad_bowling[i]
        for j in range(i+1, i+3):
            vajalik += ' ' + hinnad_bowling[j]
        lst.insert(END, vajalik)

    lst.insert(END, "         ")
    lst.insert(END,"NB! Rohkem info saad lingi klõpsamisel.")
    lst.place(x=10, y=200)
 

    def Link1():
        webbrowser.open("http://www.kuulsaal.ee/avaleht/?")
    button1 = ttk.Button(app, text = "Bowling", command = Link1)
    button1.pack()
    button1.place(x=60, y=70, width=60)

    app.mainloop()
