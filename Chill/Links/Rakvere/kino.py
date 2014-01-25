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
        elemendid = q('<tbody>')
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            if '\n' in asi:
               asi = asi.replace('\n', '')
            vajalik.append(asi.strip())
        return(vajalik)

    lehekülg = 'http://www.rakvereteater.ee/kino/kava/'
    lisst = scrapimine('tr', lehekülg)
    nimetus = scrapimine('strong.name', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Rakvere/kinoRakvere.gif')
    canvas.create_image(20,50, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Hetkel kinos:")
    lst.insert(END,"       ")
    
    vajalik = []
    for i in range(len(lisst)):
        a = lisst[i].split('/')
        vajalik = a[0].strip().replace(16*' ', '')
        if nimetus[i] in vajalik:
            vajalik = vajalik.replace(nimetus[i], '')
        lst.insert(END,nimetus[i] + '\n' + vajalik)
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)


    def Link():
        webbrowser.open("http://www.rakvereteater.ee/kino/kava/")
    button = ttk.Button(app, text = "Kino", command = Link)
    button.pack()
    button.place(x=20, y=10, width=60)

            
    app.mainloop()
