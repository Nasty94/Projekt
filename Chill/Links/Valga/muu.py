from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("300x200+400+100")
    app.title("Meelelahustused")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Valga/ValgaMuu.gif')
    canvas.create_image(0, 50, image = gif1, anchor = NW)

    def Link1():
        webbrowser.open("http://www.valgakultuurikeskus.ee/sundmused/kalender/")
    button1 = ttk.Button(app, text = "Kultuuri sündmused", command = Link1)
    button1.pack()
    button1.place(x=100, y=150, width=150)

    def Link2():
        webbrowser.open("http://www.voorimehepubi.ee/")
    button2 = ttk.Button(app, text = "Voorimehe pubi", command = Link2)
    button2.pack()
    button2.place(x=10, y=10, width=100)

    def Link3():
        webbrowser.open("https://et-ee.facebook.com/events/164949527035193/?ref=22")
    button3 = ttk.Button(app, text = "Paintball", command = Link3)
    button3.pack()
    button3.place(x=10, y=150, width=60)

    app.mainloop()
