from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("310x150+400+100")
    app.title("Klubid")
    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/HaapsaluKlubi.gif')
    canvas.create_image(100, 15, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://clubafrica.ee/klubi")
    button = ttk.Button(app, text = "Africa", command = Link)
    button.pack()
    button.place(x=20, y=60, width=60)


    app.mainloop()
