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
            if asi != '' and not asi.isalnum():
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.vanalinnabowling.ee/?id=2'
    vajalik = scrapimine('p span', lehekülg)

    app = Toplevel()
    app.geometry("600x400+400+100")
    app.title("Meelelahustused")
    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/HaapsaluMuu.gif')
    canvas.create_image(60, 0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=90)
    lst.insert(END,"Vanalinna bowling:")
    lst.insert(END,"       ")

    for i in range(1, len(vajalik[:10])):
        lst.insert(END,vajalik[i])

    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=180)



    def Link():
        webbrowser.open("http://www.vanalinnabowling.ee/")
    button = ttk.Button(app, text = "Bowling", command = Link)
    button.pack()
    button.place(x=10, y=50, width=60)

    app.mainloop()
