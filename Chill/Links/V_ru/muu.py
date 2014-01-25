from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("450x200+400+100")
    app.title("Meelelahutus")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Võru/VõruMuu.gif')
    canvas.create_image(250, 10, image = gif1, anchor = NW)

    def Link2():
        webbrowser.open("http://www.puhkaeestis.ee/et/avasta-eestimaad/aktiivne-puhkus/seikluspargid")
    button2 = ttk.Button(app, text = "Seikluspark", command = Link2)
    button2.pack()
    button2.place(x=100, y=60, width=100)

    app.mainloop()
