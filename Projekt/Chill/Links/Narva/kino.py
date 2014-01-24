from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests
import datetime

def näita():
    def scrapimine(klass, lehekülg, data,):
        path = 'cacert.pem'
        page = requests.get(lehekülg, params=data, verify=path)
        page_html = page.text
        q = pq(page_html)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            vajalik.append(asi)
        return(vajalik)

    def movies(järjend, x1, x2):
        lst = []
        for i in range(x1, len(järjend), x2):
            lst.append(järjend[i])
        return lst

    täna = datetime.date.today()
    kuupäev = '{0}.{1}.{2}'.format(täna.day, täna.month, täna.year)
    lehekülg = 'https://www.forumcinemas.ee/Websales/SelectShow/'
    data = {
        'TheatreArea':'1004',
        'dt':kuupäev,
        'tm':'',
        'genre':'',
        'X-Requested-With':'XMLHttpRequest',
        'area':'1004'}

    järjend = scrapimine('div a', lehekülg, data)
    filmid = movies(järjend, 1, 4)
    aeg = movies(järjend, 0, 4)
    saalid = movies(järjend, 2, 4)

    app = Toplevel()
    app.geometry("650x400+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Narva/NarvaKino.gif')
    canvas.create_image(200, 0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
                  fg='black', highlightbackground='blue',\
                  highlightcolor='green', width=90)
    lst.insert(END,"Kino Astri filmid:")
    lst.insert(END,"       ")
    for j in range(len(filmid)):
        asi = filmid[j]
        if '\n' in asi:
           filmid[j] = asi.replace('\n', '')
                   
    for i in range(len(filmid)):
        vajalik = filmid[i] \
                  + ' , ' + aeg[i] \
                  + ' , ' + saalid[i]
        lst.insert(END, vajalik)
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=200)

    def Link():
        webbrowser.open("https://www.forumcinemas.ee/Websales/SelectShow/")
    button = ttk.Button(app, text = "Astri", command = Link)
    button.pack()
    button.place(x=70, y=120, width=60)

            
    app.mainloop()
