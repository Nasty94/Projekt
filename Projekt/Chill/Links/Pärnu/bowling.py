from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("240x150+400+100")
    app.title("Meelelahutused")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Pärnu/muuPärnu.gif')
    canvas.create_image(0,0, image = gif1, anchor = NW)

    def Link2():
        webbrowser.open("http://www.peronabowling.ee/")
    button2 = ttk.Button(app, text = "Bowling", command = Link2)
    button2.pack()
    button2.place(x=10, y=60, width=60)

    app.mainloop()
