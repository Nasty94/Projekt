from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    def scrapimine(klass, lehekülg):
        page = requests.get(lehekülg)
        page_html = page.text.find('<tbody>')
        contents = page.text[page_html + 12:]
        q = pq(contents)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

    lehekülg = 'http://www.kultuurimaja.ee/index.php?option=com_content&task=view&id=60&Itemid=74'
    filmid = scrapimine('p', lehekülg)

    app = Toplevel()
    app.geometry("550x400+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/Haapsalukino.gif')
    canvas.create_image(100, 15, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=60)
    lst.insert(END,"Kultuuri keskuse filmid:")
    lst.insert(END,"       ")

    for i in range(len(filmid)):
       lst.insert(END,filmid[i])

    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=180)




    def Link():
        webbrowser.open("http://www.kultuurimaja.ee/index.php?option=com_content&task=view&id=60&Itemid=74")
    button = ttk.Button(app, text = "Kino", command = Link)
    button.pack()
    button.place(x=10, y=60, width=60)

            
    app.mainloop()
