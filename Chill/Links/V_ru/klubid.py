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
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.clubtartu.ee/'
    aeg = scrapimine('div h3', lehekülg)
    nimetused = scrapimine('div h2', lehekülg)

    app = Toplevel()
    app.geometry("550x450+400+100")
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Võru/VõruKlubi.gif')
    canvas.create_image(200, 10, image = gif1, anchor = NW)

    
    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=70)
    lst.insert(END,"Võru klubi:")
    lst.insert(END,"       ")

    for i in range(len(aeg)):
        lst.insert(END,nimetused[i] + '\n' \
              + aeg[i] + '\n')

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=100,y=250)

    def Link1():
        webbrowser.open("https://www.facebook.com/KlubiIndustriaal")
    button1 = ttk.Button(app, text = "Industriaal", command = Link1)
    button1.pack()
    button1.place(x=80, y=60, width=100)


    def Link2():
        webbrowser.open("http://www.clubtartu.ee/kontakt")
    button2 = ttk.Button(app, text = "Club Tartu", command = Link2)
    button2.pack()
    button2.place(x=80, y=100, width=100)

    app.mainloop()
