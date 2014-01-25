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
       elemendid = q(klass).not_('.readmore')
       vajalik = []
       for i in range(len(elemendid)):
           asi = q(q(klass).not_('.readmore')[i]).text()
           vajalik.append(asi)
       return(vajalik)

   lehekülg = 'http://www.mirage.ee/uritused'
   nimetused = scrapimine('div.page-header', lehekülg)
   aeg = scrapimine('div p', lehekülg)

   app = Toplevel()
   app.geometry("500x450+400+100")
   app.title("Klubid")

   canvas = Canvas(app,width = 500, height = 500, bg="white")
   canvas.pack(expand = YES, fill = BOTH)
   gif1 = PhotoImage(file = 'LinksPildid/Pärnu/clubPärnu.gif')
   canvas.create_image(200,30, image = gif1, anchor = NW)

   lst = Listbox(app, activestyle='dotbox',\
               fg='black', highlightbackground='blue',\
               highlightcolor='green', width=70)
   lst.insert(END,"Mirage:")
   lst.insert(END,"       ")

   for i in range(len(nimetused)):
       üritus = nimetused[i] + ' , ' \
                + aeg[i] + ' , '
       lst.insert(END,üritus)
   lst.insert(END,"       ")
   lst.insert(END,"Veel klubisid saad leida linkides")
   lst.place(x=30,y=250)


   def Link():
      webbrowser.open("http://www.sunset.ee/")
   button = ttk.Button(app, text = "Sunset", command = Link)
   button.pack()
   button.place(x=20, y=40, width=60)

   def Link1():
       webbrowser.open("http://www.sugarclub.ee/")
   button1 = ttk.Button(app, text = "Sugarclub", command = Link1)
   button1.pack()
   button1.place(x=120, y=40, width=60)

   def Link2():
       webbrowser.open("http://www.mirage.ee/")
   button2 = ttk.Button(app, text = "Mirage", command = Link2)
   button2.pack()
   button2.place(x=20, y=90, width=60)

   def Link3():
       webbrowser.open("https://www.facebook.com/bravo.nightclub")
   button3 = ttk.Button(app, text = "Bravo", command = Link3)
   button3.pack()
   button3.place(x=120, y=90, width=60)


   app.mainloop()

