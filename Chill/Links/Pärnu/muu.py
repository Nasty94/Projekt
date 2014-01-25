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

    def Link():
        webbrowser.open("http://www.nastydog.ee/")
    button = ttk.Button(app, text = "Paintball", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)

    def Link3():
        webbrowser.open("http://viiking.ee/loogastuspaketid-2012")
    button3 = ttk.Button(app, text = "Viiking SPA", command = Link3)
    button3.pack()
    button3.place(x=10, y=60, width=100)

    app.mainloop()
