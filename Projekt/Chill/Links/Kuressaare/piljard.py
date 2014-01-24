from tkinter import *
from tkinter import ttk
import webbrowser
import easygui

def näita():
    easygui.msgbox("Kahjuks, infot, mida te otsite pole meie andmebaasis."
               "Äkki leiate midagi alltoodud nimekirjas."
               "Vajutage OK nuppu jätkamisesks.")

    app = Toplevel()
    app.geometry("250x180+400+100")
    app.title("SPA")
    canvas = Canvas(app,width = 500, height = 500)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Kuressaare/KurMuu.gif')
    canvas.create_image(0, 0, image = gif1, anchor = NW)

    def Link():
        webbrowser.open("http://www.saaremaaspahotels.eu/")
    button = ttk.Button(app, text = "SPA", command = Link)
    button.pack()
    button.place(x=10, y=150, width=60)


    app.mainloop()
            
