from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("250x150+400+100")
    app.title("Vaba aeg")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/muuTartu.gif')
    canvas.create_image(0,0, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://www.paintwar.ee/est/")
    button = ttk.Button(app, text = "Paintball", command = Link)
    button.pack()
    button.place(x=10, y=10, width=60)


    def Link3():
        webbrowser.open("http://www.shooters.ee/tartu.html")
    button3 = ttk.Button(app, text = "Shooters", command = Link3)
    button3.pack()
    button3.place(x=10, y=110, width=60)


    app.mainloop()
