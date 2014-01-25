from tkinter import *
from tkinter import ttk
import webbrowser
import easygui

def näita():
    easygui.msgbox("Kahjuks, infot, mida te otsite pole meie andmebaasis."
               "Äkki leiate midagi alltoodud nimekirjas."
               "Vajutage OK nuppu jätkamisesks.")

    app = Toplevel()
    app.geometry("280x180+400+100")
    app.title("Meelelahustused")
    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Haapsalu/HaapsaluMuu.gif')
    canvas.create_image(60, 0, image = gif1, anchor = NW)


    # kuna bowlingi kohta on mõned lingid, siis teeme ni:
    def Link4():
        app = Tk()
        app.geometry("300x100+400+100")
        app.title("Pubid")
        def Link5():
            webbrowser.open("http://clubafrica.ee/pubi-1")
        button5=ttk.Button(app,text="Africa", command=Link5)
        button5.pack()
        button5.place(x=10, y=30, width=100)

        def Link6():
            webbrowser.open("https://www.facebook.com/pages/Taksi-Pubi/182200098540351")
        button6=ttk.Button(app,text="Taksi pubi", command=Link6)
        button6.pack()
        button6.place(x=120, y=30, width=100)


        app.mainloop()
                
    button4 = ttk.Button(app, text = "Pubid", command = Link4)
    button4.pack()
    button4.place(x=10, y=80, width=60)

    app.mainloop()
