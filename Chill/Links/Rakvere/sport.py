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
    rakvere = linna_valimine('Rakvere', spordiüritused)

    
    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Rakvere/Rakveresport.gif')
    canvas.create_image(70,50, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Rakvere spordiüritused:")
    lst.insert(END,"       ")

    for i in range(len(rakvere)):
        for j in range(len(rakvere[i])):
            if rakvere[i][j]== "":
                lst.insert(END, "Sellel aastal Rakveres rohkem ei ole suureamid spordiüritusi!")
            else:
                lst.insert(END,rakvere[i][j])
                
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)
       

    def Link1():
        webbrowser.open("http://rivaal.ri.ee/")
    button1 = ttk.Button(app, text = "Võrkpall", command = Link1)
    button1.pack()
    button1.place(x=170, y=10, width=60)


    def Link2():
        webbrowser.open("http://www.rakveretennis.ee/")
    button2 = ttk.Button(app, text = "Tennis", command = Link2)
    button2.pack()
    button2.place(x=320, y=10, width=60)

    def Link3():
        webbrowser.open("http://www.aqvahotels.ee/vee-ja-saunakeskus/hinnakiri")
    button3 = ttk.Button(app, text = "Veekeskus", command = Link3)
    button3.pack()
    button3.place(x=20, y=10, width=100)


    def Link4():
        webbrowser.open("https://www.facebook.com/rakverejktarvas")
    button4 = ttk.Button(app, text = "Jalgpall", command = Link4)
    button4.pack()
    button4.place(x=250, y=10, width=60)


    app.mainloop()
