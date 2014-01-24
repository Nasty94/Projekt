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
        lb = []
        for i in range(len(järjend)):
            if linn in järjend[i]:
                lb.append(järjend[i])
            
        return lb

    spordiüritused = scrapimine('tr td', 'http://www.sport.ee/et/tegevused/spordiuritused')
    pärnu = linna_valimine('Pärnu ', spordiüritused)

    app = Toplevel()
    app.geometry("370x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Pärnu/sportPärnu.gif')
    canvas.create_image(100,20, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
          fg='black', highlightbackground='blue',\
          highlightcolor='green', width=50)
    lst.insert(END,"       ")
    lst.insert(END,"Pärnu spordiüritused")
    lst.insert(END,"       ")


    msg="Praegu ei toimu mingit sportdiüritust Pärnus."
    for i in range(len(pärnu)):
        for j in range(len(pärnu[i])):      
            if len(pärnu[i][j])==0:
                lst.insert(END,msg)

            else:
                lst.insert(END,pärnu[i][j])

    lst.insert(END,"     ")
    lst.insert(END,"Rohkem spordivõimalusi Pärnu saad leida  lingides")
    lst.place(x=50,y=250)

    def Link1():
        webbrowser.open("http://www.kkparnu.ee/")
    button1 = ttk.Button(app, text = "Korvpall", command = Link1)
    button1.pack()
    button1.place(x=10, y=60, width=60)


    def Link2():
        webbrowser.open("http://www.pvk.ee/")
    button2 = ttk.Button(app, text = "Võrkpall", command = Link2)
    button2.pack()
    button2.place(x=10, y=10, width=60)

    def Link3():
        webbrowser.open("http://www.parnusport.ee/et/tegutsevad-spordialad")
    button3 = ttk.Button(app, text = "Rohkem info", command = Link3)
    button3.pack()
    button3.place(x=10, y=120, width=70)


    app.mainloop()
