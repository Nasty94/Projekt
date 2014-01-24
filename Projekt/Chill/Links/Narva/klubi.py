from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("250x275+400+100")
    app.title("Klubi")

    canvas = Canvas(app,width = 500, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Narva/NarvaKlubi.gif')
    canvas.create_image(0, 0, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://geneva.ee/main/index.php?lang=ru")
    button = ttk.Button(app, text = "Geneva", command = Link)
    button.pack()
    button.place(x=20, y=20, width=60)

    app.mainloop()
