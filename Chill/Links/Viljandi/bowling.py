from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():

    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        p = page.text.find('<tbody>')
        contents = page.text[p + 12:]
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)-10):
            if i == 0:
                vajalik.append('BOWLING')
            if i == 5:
                vajalik.append('PILJARD')
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.fsbowling.ee/?id=2&ids=1'
    vajalik = scrapimine('blockquote p', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Meelelahustus")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Viljandi/ViljandiMuu.gif')
    canvas.create_image(250,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=65)
    lst.insert(END,"FS bowling:")
    lst.insert(END,"       ")

    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=150)


    def Link5():
        webbrowser.open("http://www.viljandibowling.ee/")
    button5=ttk.Button(app,text="Viljandi bowling", command=Link5)
    button5.pack()
    button5.place(x=10, y=30, width=100)

    def Link6():
        webbrowser.open("http://www.fsbowling.ee/")
    button6=ttk.Button(app,text="FS bowling", command=Link6)
    button6.pack()
    button6.place(x=120, y=30, width=100)

    app.mainloop()
