from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("550x250+400+100")
    app.title("Piljard")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Võru/VõruMuu.gif')
    canvas.create_image(200, 10, image = gif1, anchor = NW)

    def Link1():
        webbrowser.open("https://www.facebook.com/CHPiljard")
    button1 = ttk.Button(app, text = "CHPiljard", command = Link1)
    button1.pack()
    button1.place(x=100, y=30, width=60)

    app.mainloop()
