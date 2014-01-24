from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("250x200+400+100")
    app.title("Meelelahustus")

    canvas = Canvas(app,width = 500, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Rakvere/muuRakvere.gif')
    canvas.create_image(0,0, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://rakbowl.ee/")
    button = ttk.Button(app, text = "Bowling", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)

    app.mainloop()
