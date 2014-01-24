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
    tartu = linna_valimine('Tartu', spordiüritused)

    app = Toplevel()
    app.geometry("400x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/sportTartu.gif')
    canvas.create_image(0,75, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=50)
    lst.insert(END,"Tartu spordiüritused")
    lst.insert(END,"       ")

    for i in range(len(tartu)):
        for j in range(len(tartu[i])):
            lst.insert(END,tartu[i][j])

    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Tallinnas saad leida  lingides")
    lst.place(x=50,y=250)

    def Link1():
        webbrowser.open("http://www.aurakeskus.ee/")
    button1 = ttk.Button(app, text = "Ujumine", command = Link1)
    button1.pack()
    button1.place(x=170, y=10, width=60)


    def Link2():
        webbrowser.open("http://www.volley.ee/")
    button2 = ttk.Button(app, text = "Võrkpall", command = Link2)
    button2.pack()
    button2.place(x=170, y=60, width=60)

    def Link3():
        webbrowser.open("http://www.myfitness.ee/tartu/t")
    button3 = ttk.Button(app, text = "Fitness", command = Link3)
    button3.pack()
    button3.place(x=270, y=10, width=60)


    def Link4():
        webbrowser.open("http://www.tartutennis.ee/")
    button4 = ttk.Button(app, text = "Tennis", command = Link4)
    button4.pack()
    button4.place(x=270, y=60, width=60)

    def Link5():
        webbrowser.open("http://sport.ut.ee/")
    button5 = ttk.Button(app, text = "Jõusaal", command = Link5)
    button5.pack()
    button5.place(x=170, y=120, width=60)

    app.mainloop()
