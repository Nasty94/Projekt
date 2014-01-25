from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        page_html = page.text.find('<tbody>')
        contents = page.text[page_html + 12:]
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Meelelahutused")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Pärnu/muuPärnu.gif')
    canvas.create_image(200,20, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Pärnu kino:")
    lst.insert(END,"       ")

    lehekülg = 'http://www.peronabowling.ee/piljard.html'
    tööaeg = scrapimine('fieldset div', lehekülg)
    for i in range(len(tööaeg)):
        lst.insert(END,tööaeg[i])



    lehekülg = 'http://www.peronabowling.ee/piljard.html'
    piljard = scrapimine('p.bodytext', lehekülg)
    for i in range(len(piljard)):
        lst.insert(END,piljard[i])

    
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)

    def Link1():
        webbrowser.open("https://www.facebook.com/PiljardPokker")
    button1 = ttk.Button(app, text = "Piljard&Pokker", command = Link1)
    button1.pack()
    button1.place(x=50, y=110, width=100)

    app.mainloop()

