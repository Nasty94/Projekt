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
        for i in range(3, len(elemendid), 3):
            järjend = []
            for j in range(3):
                if (i + j) < len(elemendid) \
                   and q(q(klass)[i + j]).text() != '':
                    järjend.append(q(q(klass)[i + j]).text())
            if len(järjend) != 0:
                vajalik.append(järjend)
        return(vajalik)

    def linna_valimine(linn, järjend):
        lst = []
        for i in range(len(järjend)):
            if linn in järjend[i]:
                lst.append(järjend[i])
        return lst

    spordiüritused = scrapimine('tr td', 'http://www.sport.ee/et/tegevused/spordiuritused')
    narva = linna_valimine('Narva', spordiüritused)

    app = Toplevel()
    app.geometry("370x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Narva/NarvaSport.gif')
    canvas.create_image(30,10, image = gif1, anchor = NW)

    
    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=50)
    lst.insert(END,"Narva spordiüritused")
    lst.insert(END,"       ")

    for i in range(len(narva)):
        for j in range(len(narva[i])):
            lst.insert(END,narva[i][j])

    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Narvas saad leida  lingides")
    lst.place(x=10,y=250)
    
    def Link1():
        webbrowser.open("http://www.narva.ee/ee/calendars/index/cat/2")
    button1 = ttk.Button(app, text = "Spordiüritused", command = Link1)
    button1.pack()
    button1.place(x=50, y=170, width=100)


    def Link2():
        webbrowser.open("http://www.skenergia.ee/index.php?option=com_content&view=article&id=96&Itemid=92&lang=et")
    button2 = ttk.Button(app, text = "Ujula", command = Link2)
    button2.pack()
    button2.place(x=190, y=170, width=100)


    app.mainloop()
