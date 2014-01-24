from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests
import datetime

def näita():

    def scrapimine(kuupäev1, kuupäev2, klass, linn):
        page = requests.get('http://www.piletilevi.ee/est/piletid/?startdate='\
                        + kuupäev1 + '&enddate=' + kuupäev2 \
                        + '&place=' + linn +'&category=&promoter=&fastsearch=1')
        page_html = page.text
        q = pq(page_html)
        elemendid = q(klass)
        vajalik = []
        for i in range(len(elemendid)):
            asi = q(q(klass)[i]).text()
            if '/' in asi:
                lst = asi.split('/')
                vajalik.append(lst[1].strip().encode('latin-1').decode('utf-8'))
            else:
                vajalik.append(asi.encode('latin-1').decode('utf-8'))
        return(vajalik)

    täna = datetime.date.today()
    järgmist_3_päeva = täna + datetime.timedelta(days=3)
    kuupäev1 = '{0}.{1}.{2}'.format(täna.day, täna.month, täna.year)
    kuupäev2 = '{0}.{1}.{2}'.format(järgmist_3_päeva.day, järgmist_3_päeva.month, \
                                    järgmist_3_päeva.year)

    nimetused =  scrapimine(kuupäev1, kuupäev2, 'a.eventslist_item_title', '43162')
    kuupäev = scrapimine(kuupäev1, kuupäev2, 'div.eventslist_item_date', '43162')
    piletihind = scrapimine(kuupäev1, kuupäev2, 'div.eventslist_item_price_primary', '43162')
    
    app = Toplevel()
    app.geometry("550x600+400+100")  
    app.title("Teater")
    
    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnTeater.gif')
    canvas.create_image(150,10, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=70, heigh=20)
    lst.insert(END,"Hetkel Tallinna teatrides:")
    lst.insert(END, "        ")

    for i in range(len(nimetused)):
        lst.insert(END,nimetused[i] + ' , ' + kuupäev[i] + ' , ' + piletihind[i] + ' , ')

    lst.insert(END, "         ")
    
    lst.place(x=80, y=250)

    def Link():
        webbrowser.open("http://www.draamateater.ee/")
    button = ttk.Button(app, text = "Eesti draamateater", command = Link)
    button.pack()
    button.place(x=20, y=20, width=110)

    def Link1():
        webbrowser.open("http://www.linnateater.ee/")
    button1 = ttk.Button(app, text = "Linnateater", command = Link1)
    button1.pack()
    button1.place(x=20, y=160, width=70)

    def Link2():
        webbrowser.open("http://www.opera.ee/")
    button2 = ttk.Button(app, text = "Rahvusooper", command = Link2)
    button2.pack()
    button2.place(x=20, y=210, width=75)

    def Link3():
        webbrowser.open("http://www.concert.ee/")
    button3 = ttk.Button(app, text = "Eesti kontserdimaja", command = Link3)
    button3.pack()
    button3.place(x=20, y=115, width=110)

    def Link4():
        webbrowser.open("http://www.nukuteater.ee/")
    button4 = ttk.Button(app, text = "Nukuteater", command = Link4)
    button4.pack()
    button4.place(x=20, y=70, width=67)


    app.mainloop()
    
