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
    valga = linna_valimine('Valga', spordiüritused)

    app = Toplevel()
    app.geometry("370x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaSport.gif')
    canvas.create_image(30,10, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=50)
    lst.insert(END,"Valga spordiüritused")
    lst.insert(END,"       ")

    for i in range(len(valga)):
        for j in range(len(valga[i])):
            lst.insert(END,valga[i][j])



    
    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Valgas saad leida  lingides")
    lst.place(x=10,y=250)
   


    def Link1():
        webbrowser.open("http://www.valgapoks.org/")
    button1 = ttk.Button(app, text = "Poks", command = Link1)
    button1.pack()
    button1.place(x=130, y=10, width=60)


    def Link2():
        webbrowser.open("http://valgamaadlus.veebi.net/")
    button2 = ttk.Button(app, text = "Maadlus", command = Link2)
    button2.pack()
    button2.place(x=210, y=10, width=100)

    def Link3():
        webbrowser.open("http://www.valgasaalihoki.ee/")
    button3 = ttk.Button(app, text = "Saalihoki", command = Link3)
    button3.pack()
    button3.place(x=40, y=10, width=60)


    def Link4():
        webbrowser.open("http://www.valgasport.ee/spordiklubid")
    button4 = ttk.Button(app, text = "Rohkem info siin", command = Link4)
    button4.pack()
    button4.place(x=50, y=100, width=100)


    app.mainloop()
