from tkinter import *
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
    järgmist_3_päeva = täna + datetime.timedelta(days=7)
    kuupäev1 = '{0}.{1}.{2}'.format(täna.day, täna.month, täna.year)
    kuupäev2 = '{0}.{1}.{2}'.format(järgmist_3_päeva.day, järgmist_3_päeva.month, \
                                    järgmist_3_päeva.year)

    nimetused =  scrapimine(kuupäev1, kuupäev2, 'a.eventslist_item_title', '43176')
    kuupäev = scrapimine(kuupäev1, kuupäev2, 'div.eventslist_item_date', '43176')
    piletihind = scrapimine(kuupäev1, kuupäev2, 'div.eventslist_item_price_primary', '43176')
    
    app = Toplevel()
    app.geometry("500x400+400+100")  
    app.title("Teater")
    
    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/HaapsaluTeater.gif')
    canvas.create_image(150,0, image = gif1, anchor = NW)

    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=70)
    lst.insert(END,"Haapsalu teater:")
    lst.insert(END, "        ")

    for i in range(len(nimetused)):
        lst.insert(END,nimetused[i] + '\n' + kuupäev[i] + '\n' + piletihind[i] + '\n')


    lst.insert(END, "         ")
    
    lst.place(x=50, y=200)


    app.mainloop()
    
