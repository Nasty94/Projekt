from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():

    def scrapimine(klass, lehekülg, vahemik):
        page = requests.get(lehekülg)
        contents = page.text
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(vahemik, len(elemendid)):
            asi = q(q(klass)[i]).text()
            asi = asi.replace('Ã¼', 'ü')
            asi = asi.replace('Ã¤', 'ä')
            asi = asi.replace('Ãµ', 'õ')
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.vorukannel.ee/index.php?ent=1&today=1'
    vajalik = scrapimine('tr td a strong', lehekülg, 3)
    pealkiri = scrapimine('td.txtvalge11px', lehekülg, 0)[1]


    app = Toplevel()
    app.geometry("600x450+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Võru/VõruKino.gif')
    canvas.create_image(200, 10, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=65)
    lst.insert(END,"Võru kino:")
    lst.insert(END,"       ")
    
    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=100,y=250)

    def Link1():
        webbrowser.open("http://www.vorukannel.ee/index.php?Menu=2&Lang=est")
    button1 = ttk.Button(app, text = "Kino Kannel", command = Link1)
    button1.pack()
    button1.place(x=80, y=50, width=100)

    app.mainloop()
