from tkinter import *
from tkinter import ttk
import webbrowser

def näita():
    app = Toplevel()
    app.geometry("300x220")
    app.title("Meelelahustus")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Viljandi/ViljandiMuu.gif')
    canvas.create_image(0,0, image = gif1, anchor = NW)

    def Link1():
        webbrowser.open("http://www.turismiweb.ee/et/category/spa-anlaggningar/51/Viljandi.html")
    button1 = ttk.Button(app, text = "SPA", command = Link1)
    button1.pack()
    button1.place(x=130, y=100, width=60)

    def Link4():
            app = Tk()
            app.geometry("300x100+400+100")
            app.title("Pubid")

            def Link2():
                webbrowser.open("http://www.zakzak.ee/")
            button2=ttk.Button(app,text="Zak-Zak", command=Link2)
            button2.pack()
            button2.place(x=10, y=30, width=100)

            def Link3():
                webbrowser.open("http://www.turismiweb.ee/et/company/kilpkonna-trahter/8528/")
            button3=ttk.Button(app,text="Kilpkonna trahter", command=Link3)
            button3.pack()
            button3.place(x=120, y=30, width=100)
          
    button4 = ttk.Button(app, text = "Pubid", command = Link4)
    button4.pack()
    button4.place(x=30, y=100, width=60)

    app.mainloop()
