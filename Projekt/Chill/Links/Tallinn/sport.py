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
    tallinn = linna_valimine('Tallinn', spordiüritused)

    app = Toplevel()
    app.geometry("370x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnSport.gif')
    canvas.create_image(80, 90, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=50)
    lst.insert(END,"Tallinna spordiüritused:")
    lst.insert(END,"       ")

    for i in range(len(tallinn)):
        for j in range(len(tallinn[i])):
            lst.insert(END,tallinn[i][j])

    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Tallinnas saad leida  lingides")
    lst.place(x=10,y=250)

    def Link1():
        webbrowser.open("http://www.kalevspa.ee/veekeskus/")
    button1 = ttk.Button(app, text = "Ujumine", command = Link1)
    button1.pack()
    button1.place(x=110, y=10, width=60)


    def Link2():
        webbrowser.open("http://www.nommeseikluspark.ee/")
    button2 = ttk.Button(app, text = "Nõmme seikluspark", command = Link2)
    button2.pack()
    button2.place(x=100, y=60, width=130)

    def Link3():
        webbrowser.open("http://www.myfitness.ee/")
    button3 = ttk.Button(app, text = "Fitness", command = Link3)
    button3.pack()
    button3.place(x=10, y=10, width=60)


    def Link4():
        webbrowser.open("http://www.kalevitenniseklubi.ee/")
    button4 = ttk.Button(app, text = "Tennis", command = Link4)
    button4.pack()
    button4.place(x=10, y=60, width=60)

    def Link5():
        webbrowser.open("http://www.icearena.ee/")
    button5 = ttk.Button(app, text = "Uisutamine", command = Link5)
    button5.pack()
    button5.place(x=10, y=110, width=80)

    app.mainloop()
