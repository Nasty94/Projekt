from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    
    def scrapimine(klass, lehekülg, vahemik):
        page = requests.get(lehekülg)
        page_html = page.text
        q = pq(page_html)
        elemendid = q(klass)
        vajalik = []
        if vahemik == 0:
            vahemik = len(elemendid)
        for i in range(vahemik):
            asi = q(q(klass)[i]).text()
            if asi != '':
                vajalik.append(asi)
        return(vajalik)

        
    lehekülg = 'http://www.valgabowling.ee/?page_id=124'
    töötamisaeg = scrapimine('div.post-content p', lehekülg, 0)
    
    app = Toplevel()
    app.geometry("650x500+400+100")
    app.title("Meelelahustused")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaMuu.gif')
    canvas.create_image(0, 30, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=90)
    lst.insert(END,"Vanalinna bowling:")
    lst.insert(END,"       ")

    for i in range(len(töötamisaeg)):
        lst.insert(END,töötamisaeg[i])

    lehekülg = 'http://www.valgabowling.ee/?page_id=15'
    bowling = scrapimine('div.post-content p', lehekülg, 6)

    for i in range(len(bowling)):
        lst.insert(END,bowling[i])

    lst.insert(END,"Rokem info saamiseks vajutage sobivat nuppu")
    lst.place(x=50,y=250)
    
  
    def Link():
        webbrowser.open("http://www.valgabowling.ee/")
    button = ttk.Button(app, text = "Bowling", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)

    app.mainloop()
