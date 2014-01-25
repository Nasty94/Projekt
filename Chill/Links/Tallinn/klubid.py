from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    url = 'http://clubhollywood.ee/tulemas/'
    page = requests.get(url)
    p = page.text.find('Tulemas</h1>')
    contents = page.text[p + 12:]
    q = pq(contents)
    events = q('article')

    app = Toplevel()
    app.geometry("700x450+400+100")
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnKlubi.gif')
    canvas.create_image(200, 10, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=105)
    lst.insert(END,"Hollywood:")
    lst.insert(END,"       ")

    for i in range(len(events)):
        a = events[i]
        vajalik = pq(a)('h2.title').text() \
                  + ' , ' + pq(a)('.date').text() \
                  + ' , ' + pq(a)('.artists').text()
        lst.insert(END,vajalik)
    lst.insert(END,"Veel klubisid saad leida linkides")
    lst.place(x=50,y=250)


    def Link():
        webbrowser.open("http://www.venusclub.ee/")
    button = ttk.Button(app, text = "Venus", command = Link)
    button.pack()
    button.place(x=20, y=20, width=70)

    def Link1():
        webbrowser.open("http://clubhollywood.ee/")
    button1 = ttk.Button(app, text = "Hollywood", command = Link1)
    button1.pack()
    button1.place(x=120, y=20, width=70)

    def Link2():
        webbrowser.open("http://www.clubprive.ee/")
    button2 = ttk.Button(app, text = "Club Prive", command = Link2)
    button2.pack()
    button2.place(x=20, y=70, width=70)

    def Link3():
        webbrowser.open("http://www.clubparlament.com/")
    button3 = ttk.Button(app, text = "Parlament", command = Link3)
    button3.pack()
    button3.place(x=70, y=110, width=70)

    def Link4():
        webbrowser.open("https://www.facebook.com/CatHouseNightclub?ref=ts")
    button4 = ttk.Button(app, text = "Cathouse", command = Link4)
    button4.pack()
    button4.place(x=120, y=70, width=60)

    app.mainloop()
