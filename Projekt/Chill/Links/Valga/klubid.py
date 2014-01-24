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
        for i in range(len(elemendid)-1):
            asi = q(q(klass)[i]).text().replace('\xa0', ' ')
            if '-' in asi:
                asi = asi.split('-')[0].strip()
            if asi.isupper() and asi not in vajalik:
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.tollihostel.ee/clubyes/index.php?option=com_content&view=article&id=18&Itemid=33&lang=et'
    üritused = scrapimine('span strong span', lehekülg)
    
    app = Toplevel()
    app.geometry("500x550+400+100")
    app.title("Klubi")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaKlubi.gif')
    canvas.create_image(200, 0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=70)
    lst.insert(END,"Club Yes:")
    lst.insert(END,"       ")

    
    for element in üritused:
        lst.insert(END,element)

    lst.insert(END,"       ")
    lst.insert(END,"Veel klubisid saad leida linkides")
    lst.place(x=50,y=300)

    def Link():
        webbrowser.open("http://www.clubexotica.ee/")
    button = Button(app, text = "Club Exotica", command = Link)
    button.pack()
    button.place(x=50, y=20, width=100)

    def Link1():
        webbrowser.open("http://www.tollihostel.ee/clubyes/")
    button1 = Button(app, text = "Club Yes", command = Link1)
    button1.pack()
    button1.place(x=120, y=70, width=60)

    def Link2():
        webbrowser.open("https://www.facebook.com/pages/Valga-Rockiklubi/141376155934174")
    button2 = ttk.Button(app, text = "Rock Club", command = Link2)
    button2.pack()
    button2.place(x=20, y=70, width=60)

    app.mainloop()
