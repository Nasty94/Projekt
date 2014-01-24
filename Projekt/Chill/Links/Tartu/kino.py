from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests
import datetime

def näita():
    def scrapimine(klass, lehekülg, data):
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
    lehekülg = 'https://www.forumcinemas.ee/Websales/SelectShow/#page=%2FWebsales%2FSelectShow%2F'
    data = {
        'TheatreArea':'1005',
        'dt':kuupäev,
        'tm':'',
        'genre':'',
        'X-Requested-With':'XMLHttpRequest',
        'area':'1005'}

    järjend = scrapimine('div a', lehekülg, data)
    filmid = movies(järjend, 1, 4)
    aeg = movies(järjend, 0, 4)
    saalid = movies(järjend, 2, 4)


    app = Toplevel()
    app.geometry("470x350+400+100")
    app.title("Kino")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/kinoTartu.gif')
    canvas.create_image(100,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=65)
    lst.insert(END,"Ekraan:")
    lst.insert(END,"       ")

    for j in range(len(filmid)):
        asi = filmid[j]
        if '\n' in asi:
           filmid[j] = asi.replace('\n', '')
                   
    for i in range(len(filmid)):
        vajalik = filmid[i] \
                  + ' , ' + aeg[i] \
                  + ' , ' + saalid[i]
        lst.insert(END,vajalik)
    lst.insert(END,"       ")
    lst.insert(END,"Rohkem info saamiseks vajuta sobivat nuppu")
    lst.place(x=50,y=150)

    def Link():
        webbrowser.open("http://www.cinamon.ee/")
    button = ttk.Button(app, text = "Cinamon", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)

    def Link7():
        webbrowser.open("https://www.forumcinemas.ee/Websales/SelectShow/")
    button7 = ttk.Button(app, text = "Ekraan", command = Link7)
    button7.pack()
    button7.place(x=10, y=60, width=60)
            
    app.mainloop()
