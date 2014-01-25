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
    võru = linna_valimine('Võru', spordiüritused)
   

    app = Toplevel()
    app.geometry("600x500+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Võru/VõruSport.gif')
    canvas.create_image(250, 20, image = gif1, anchor = NW)
    
    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=50)
    lst.insert(END,"Võru spordiüritused")
    lst.insert(END,"       ")

    
    for i in range(len(võru)):
        for j in range(len(võru[i])):
            lst.insert(END,võru[i][j])

    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Tallinnas saad leida  lingides")
    lst.place(x=250,y=250)

    def Link1():
        webbrowser.open("http://www.vsport.ee/")
    button1 = ttk.Button(app, text = "Spordiuudised", command = Link1)
    button1.pack()
    button1.place(x=80, y=110, width=100)
 

    def Link2():
        webbrowser.open("http://www.kajak.ee/index.php/forum/9-turvalisus/6745-basseini-kasutamine-vorus")
    button2 = ttk.Button(app, text = "Ujula", command = Link2)
    button2.pack()
    button2.place(x=80, y=160, width=100)

    def Link3():
        webbrowser.open("http://www.voruspordikeskus.ee/?D=201")
    button3 = ttk.Button(app, text = "Võru spordikeskus", command = Link3)
    button3.pack()
    button3.place(x=80, y=210, width=100)

    app.mainloop()
