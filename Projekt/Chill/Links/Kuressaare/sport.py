from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("250x150+400+100")
    app.title("Sport")

    canvas = Canvas(app,width = 500, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Kuressaare/KurSport.gif')
    canvas.create_image(0, 0, image = gif1, anchor = NW)

    def Link1():
        webbrowser.open("https://www.oesel.ee/kg/?a=1&i=9")
    button1 = ttk.Button(app, text = "Ujumine", command = Link1)
    button1.pack()
    button1.place(x=150, y=120, width=60)


    def Link2():
        webbrowser.open("http://www.kuressaarespordikeskus.ee/main/?s=5")
    button2 = ttk.Button(app, text = "Tennis", command = Link2)
    button2.pack()
    button2.place(x=10, y=120, width=100)


    app.mainloop()
