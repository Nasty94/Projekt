from tkinter import *
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
    app.geometry("600x450+400+100")
    app.title("Meelelahutus")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnMuu.gif')
    canvas.create_image(150, 15, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=90,heigh=10)
    lst.insert(END,"Kuusalu piljard:")
    lst.insert(END,"     ")

    for inform in range(len(piljard)):
        lst.insert(END,piljard[inform])

    lst.place(x=10, y=200)

    def Link2():
        webbrowser.open("http://www.bamba.ee/")
    button2 = ttk.Button(app, text = "Piljard", command = Link2)
    button2.pack()
    button2.place(x=10, y=60, width=60)

    app.mainloop()
