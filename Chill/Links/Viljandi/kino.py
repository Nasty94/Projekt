from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        p = page.text.find('<div class="place times">')
        contents = page.text[p + 12:]
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            asi = asi.replace('Ã¼', 'ü')
            asi = asi.replace('Ã¤', 'ä')
            asi = asi.replace('Ãµ', 'õ')
            vajalik.append(asi)
        return(vajalik)
    
    lehekülg = 'http://www.kultuurikava.ee/places/mannimae-kulalistemaja/'
    vajalik = scrapimine('div.time', lehekülg)

    app = Toplevel()
    app.geometry("650x350+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Viljandi/ViljandiKino.gif')
    canvas.create_image(0,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=65)
    lst.insert(END,"Viljandi kino:")
    lst.insert(END,"       ")
    
    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=150)


    def Link():
        webbrowser.open("http://www.kinod.ee/")
    button = ttk.Button(app, text = "Kino", command = Link)
    button.pack()
    button.place(x=250, y=10, width=60)

        
    app.mainloop()
