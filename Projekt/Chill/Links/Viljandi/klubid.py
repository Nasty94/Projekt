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
        for i in range(1, len(elemendid)-1):
            asi = q(q(klass)[i]).text()
            asi = asi[1:].strip()
            if ')' in asi:
               asi = asi.replace(')', '')
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://qclub.ee/'
    vajalik = scrapimine('div.newsflash div div', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Viljandi/ViljandiKlubi.gif')
    canvas.create_image(300,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=65)
    lst.insert(END,"GClub:")
    lst.insert(END,"       ")

    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=150)


    def Link1():
        webbrowser.open("http://www.clublounge.ee")
    button1 = ttk.Button(app, text = "Club Lounge", command = Link1)
    button1.pack()
    button1.place(x=150, y=10, width=100)


    def Link2():
        webbrowser.open("http://qclub.ee/")
    button2 = ttk.Button(app, text = "Q Club", command = Link2)
    button2.pack()
    button2.place(x=100, y=60, width=100)

    def Link3():
        webbrowser.open("https://www.facebook.com/redclub")
    button3 = ttk.Button(app, text = "Red Club", command = Link3)
    button3.pack()
    button3.place(x=10, y=10, width=100)


    def Link4():
        webbrowser.open("https://www.facebook.com/Tudengiklubi")
    button4 = ttk.Button(app, text = "Rubiin", command = Link4)
    button4.pack()
    button4.place(x=10, y=60, width=60)


    app.mainloop()
