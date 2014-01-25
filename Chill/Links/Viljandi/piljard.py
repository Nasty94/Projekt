from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests
import easygui

def näita():
    easygui.msgbox("Kahjuks, infot, mida te otsite pole meie andmebaasis."
               "Äkki leiate midagi alltoodud nimekirjas."
               "Vajutage OK nuppu jätkamisesks.")

    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        p = page.text.find('<tbody>')
        contents = page.text[p + 12:]
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)-10):
            if i == 0:
                vajalik.append('BOWLING')
            if i == 5:
                vajalik.append('PILJARD')
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.fsbowling.ee/?id=2&ids=1'
    vajalik = scrapimine('blockquote p', lehekülg)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Meelelahustus")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Viljandi/ViljandiMuu.gif')
    canvas.create_image(250,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=65)
    lst.insert(END,"FS piljard:")
    lst.insert(END,"       ")

    for i in range(len(vajalik)):
        lst.insert(END,vajalik[i])

    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=150)

    def Link1():
        webbrowser.open("http://www.turismiweb.ee/et/category/spa-anlaggningar/51/Viljandi.html")
    button1 = ttk.Button(app, text = "SPA", command = Link1)
    button1.pack()
    button1.place(x=10, y=10, width=60)

    def Link4():
            app = Tk()
            app.geometry("300x100")
            app.title("Pubid")
            def Link2():
                webbrowser.open("http://www.zakzak.ee/")
            button2=ttk.Button(app,text="Zak-Zak", command=Link2)
            button2.pack()
            button2.place(x=10, y=30, width=100)

            def Link3():
                webbrowser.open("http://www.turismiweb.ee/et/company/kilpkonna-trahter/8528/")
            button3=ttk.Button(app,text="Kilpkonna trahter", command=Link3)
            button3.pack()
            button3.place(x=120, y=30, width=100)
          
    button4 = ttk.Button(app, text = "Pubid", command = Link1)
    button4.pack()
    button4.place(x=10, y=70, width=60)

    app.mainloop()
