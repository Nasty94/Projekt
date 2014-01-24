from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("250x200+400+100")
    app.title("Meelelahustused")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Narva/NarvaMuu.gif')
    canvas.create_image(0, 30, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://tourism.narva.ee/?mid=30")
    button = ttk.Button(app, text = "Rohkem meelelahutusi", command = Link)
    button.pack()
    button.place(x=10, y=160, width=170)


    app.mainloop()
