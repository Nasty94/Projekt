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
                webbrowser.open("http://www.bombey.ee/ru/")
        button = ttk.Button(app, text = "Bombey bowling", command = Link)
        button.pack()
        button.place(x=10, y=10, width=100)

        def Link1():
            webbrowser.open("http://www.astrikeskus.ee/vaba-aeg/bowling")
        button1 = ttk.Button(app, text = "Astri bowling", command = Link1)
        button1.pack()
        button1.place(x=10, y=100, width=100)

        app.mainloop()
