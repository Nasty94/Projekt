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
        for i in range(4, len(elemendid)):
            asi = q(q(klass)[i]).text()
            if asi not in vajalik and asi != '':
                vajalik.append(asi)
        return(vajalik)

    app = Toplevel()
    app.geometry("650x450+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500,bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Pärnu/kinoPärnu.gif')
    canvas.create_image(100, 0, image = gif1, anchor = NW)

    
    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=80)
    lst.insert(END,"Pärnu kino:")
    lst.insert(END,"       ")

    lehekülg = 'http://www.maikino.ee/index.php?page=93'
    filmid = scrapimine('p span', lehekülg)
    for i in range(0, len(filmid)-1, 2):
        vajalik = filmid[i] \
              + ' , ' + filmid[i+1] \
              + ' , '
        lst.insert(END,vajalik)

    lehekülg = 'http://www.maikino.ee/index.php?page=36'
    hinnakiri = scrapimine('p', lehekülg)
    for i in range(0, len(hinnakiri)-2, 3):
        vajalik = hinnakiri[i] \
              +' , ' + hinnakiri[i+1] + ' , ' \
              +hinnakiri[i+2] + ' , '
        lst.insert(END,vajalik)


    
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=250)


    def Link():
        webbrowser.open("http://www.maikino.ee/")
    button = ttk.Button(app, text = "Maikino", command = Link)
    button.pack()
    button.place(x=10, y=50, width=60)

            
    app.mainloop()


