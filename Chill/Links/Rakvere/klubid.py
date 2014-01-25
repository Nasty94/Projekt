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
            if asi not in vajalik and asi != '' and len(asi)< 50:
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.mjau.ee/'
    vajalik = scrapimine('p span strong span', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Rakvere/klubiRakvere.gif')
    canvas.create_image(20,40, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Rakvere klubi:")
    lst.insert(END,"       ")

    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)

    def Link():
        webbrowser.open("http://www.clubrakvere.eu/")
    button = ttk.Button(app, text = "Club Rakvere", command = Link)
    button.pack()
    button.place(x=20, y=20, width=100)

    def Link1():
        webbrowser.open("http://www.mjau.ee/")
    button1 = ttk.Button(app, text = "Club Mjau", command = Link1)
    button1.pack()
    button1.place(x=130, y=20, width=80)


    app.mainloop()
