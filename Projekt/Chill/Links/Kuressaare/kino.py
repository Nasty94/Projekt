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
            if asi not in vajalik:
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.clubdiva.ee/index.php?page=269'
    vajalik = scrapimine('td p span', lehekülg)

    app = Toplevel()
    app.geometry("850x400+400+100")
    app.title("Diva Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Kuressaare/KurKino.gif')
    canvas.create_image(300, 10, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=135)
    lst.insert(END,"Kuressaare kino:")
    lst.insert(END,"       ")

    for j in range(len(vajalik)):
        lst.insert(END,vajalik[j])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=200)

    def Link():
        webbrowser.open("http://www.clubdiva.ee/")
    button = ttk.Button(app, text = "Kuressaare kino", command = Link)
    button.pack()
    button.place(x=50, y=100, width=150)

    app.mainloop()
