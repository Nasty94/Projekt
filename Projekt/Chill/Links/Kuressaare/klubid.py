from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("250x150+400+100")
    app.title("Klubid")

    canvas = Canvas(app,width = 500, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Kuressaare/KurKlubi.gif')
    canvas.create_image(0, 0, image = gif1, anchor = NW)

    def Link1():
        webbrowser.open("http://www.clubdiva.ee/")
    button1 = ttk.Button(app, text = "Club Diva", command = Link1)
    button1.pack()
    button1.place(x=10, y=10, width=60)

    def Link2():
        webbrowser.open("http://privilege.ee")
    button2 = ttk.Button(app, text = "Privilege", command = Link2)
    button2.pack()
    button2.place(x=10, y=40, width=60)


    app.mainloop()

