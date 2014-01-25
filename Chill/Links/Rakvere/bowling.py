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
        a = q('tbody')[0]
        elemendid = pq(a)(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(pq(a)(klass)[i]).text()
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://rakbowl.ee/hinnad/'
    kuupäev = scrapimine('td strong', lehekülg)
    aeg = scrapimine('tr td', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Meelelahustus")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Rakvere/muuRakvere.gif')
    canvas.create_image(200,20, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Rakvere bowling:")
    lst.insert(END,"       ")

    for i in range(0, len(aeg), 5):
        lst.insert(END,aeg[i])
        for j in range(i+1, i+5, 2):
            lst.insert(END,aeg[j] + ' ' + aeg[j+1])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)

    def Link():
        webbrowser.open("http://rakbowl.ee/")
    button = ttk.Button(app, text = "Bowling", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)

    app.mainloop()
