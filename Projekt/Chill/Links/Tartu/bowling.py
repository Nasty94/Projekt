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
        for i in range(1, len(elemendid)):
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.funbowling.ee/index.php/lahtiolekuajad'
    aeg = scrapimine('div.item-page h1 strong', lehekülg)

    app = Toplevel()
    app.geometry("550x420+400+100")
    app.title("Vaba aeg")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/muuTartu.gif')
    canvas.create_image(180,20, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=70)
    lst.insert(END,"Fun bowling:")
    lst.insert(END,"       ")


    for i in range(len(aeg)):
        if '\xa0' in aeg[i]:
            aeg[i] = aeg[i].replace('\xa0', '')
        lst.insert(END,aeg[i])
    lst.insert(END,"Rohkem info leiad sobivat nuppu klõpsamisega")
    lst.place(x=20,y=200)


    def Link5():
        webbrowser.open("http://www.funbowling.ee/")
    button5=ttk.Button(app,text="Funbowling", command=Link5)
    button5.pack()
    button5.place(x=50, y=30, width=100)

    def Link6():
        webbrowser.open("http://www.tammebowling.ee/")
    button6=ttk.Button(app,text="Tammebowling", command=Link6)
    button6.pack()
    button6.place(x=50, y=90, width=100)

    app.mainloop()

