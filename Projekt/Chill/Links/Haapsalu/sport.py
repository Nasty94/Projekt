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
    haapsalu = linna_valimine('Haapsalu', spordiüritused)

    app = Toplevel()
    app.geometry("700x550+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/HaapsaluSport.gif')
    canvas.create_image(150, 10, image = gif1, anchor = NW)
        
    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Pärnu kino:")
    lst.insert(END,"       ")

    for i in range(len(haapsalu)):
        for j in range(len(haapsalu[i])):
            lst.insert(END,haapsalu[i][j])

        
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=90,y=350)


    def Link1():
        webbrowser.open("http://www.spordibaasid.ee/?id=186")
    button1 = ttk.Button(app, text = "Jõusaal", command = Link1)
    button1.pack()
    button1.place(x=10, y=110, width=60)


    def Link2():
        webbrowser.open("http://www.spordibaasid.ee/?id=313")
    button2 = ttk.Button(app, text = "Tennis", command = Link2)
    button2.pack()
    button2.place(x=10, y=160, width=100)

    def Link3():
        webbrowser.open("http://www.spordibaasid.ee/?id=86")
    button3 = ttk.Button(app, text = "Ujula", command = Link3)
    button3.pack()
    button3.place(x=10, y=10, width=60)


    def Link4():
        webbrowser.open("http://www.spordibaasid.ee/?id=85")
    button4 = ttk.Button(app, text = "Jooks", command = Link4)
    button4.pack()
    button4.place(x=10, y=60, width=60)

    app.mainloop()
