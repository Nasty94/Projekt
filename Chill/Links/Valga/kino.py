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
        a = q('#content_a')
        elemendid = pq(a)(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(pq(a)(klass)[i]).text()
            asi = asi.replace('Ã¼', 'ü')
            asi = asi.replace('Ã¤', 'ä')
            asi = asi.replace('Ãµ', 'õ')
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.valgakultuurikeskus.ee/sundmused/kino/'
    filmid = scrapimine('h3 a', lehekülg)
    kuupäev = scrapimine('div.dateLabel', lehekülg)
    
    app = Toplevel()
    app.geometry("680x450+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaKino.gif')
    canvas.create_image(200, 20, image = gif1, anchor = NW)

    
    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=90)
    lst.insert(END,"Valga kino:")
    lst.insert(END,"       ")

    for j in range(len(filmid)):
        lst.insert(END,filmid[j] + ' , ' \
              + kuupäev[j] + ' , ')

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajutage sobivat nuppu")
    lst.place(x=50,y=250)

    def Link():
        webbrowser.open("http://www.valgakultuurikeskus.ee/sundmused/kino/")
    button = ttk.Button(app, text = "Kino", command = Link)
    button.pack()
    button.place(x=50, y=30, width=60)
            
    app.mainloop()
