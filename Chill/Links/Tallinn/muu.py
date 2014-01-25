from tkinter import *
from tkinter import ttk
import webbrowser

def näita():

    app = Toplevel()
    app.geometry("400x200")
    app.title("Meelelahutus")

    canvas = Canvas(app,width = 500, height = 500, bg="white")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tallinn/TallinnMuu.gif')
    canvas.create_image(150, 15, image = gif1, anchor = NW)

    def Link0():
        app = Tk()
        app.geometry("300x200+400+100")
        app.title("Paintball")
        
        def Link():
            webbrowser.open("http://www.paintwar.ee/est/")
        button = ttk.Button(app, text = "Paintwar", command = Link)
        button.pack()
        button.place(x=30, y=10, width=60)
        def Link3():
            webbrowser.open("http://estpaintball.eu/")
        button3 = ttk.Button(app, text = "EstPaintball", command = Link3)
        button3.pack()
        button3.place(x=130, y=10, width=100)


    button0 = ttk.Button(app, text = "Paintball", command = Link0)
    button0.pack()
    button0.place(x=60, y=45, width=60)


    # kuna bowlingi kohta on mõned lingid, siis teeme ni:
    def Link4():
        app = Tk()
        app.geometry("300x150")
        app.title("Pubid")
        def Link5():
            webbrowser.open("http://www.shooters.ee/")
        button5 = ttk.Button(app,text="Shooters", command=Link5)
        button5.pack()
        button5.place(x=10, y=30, width=100)

        def Link6():
            webbrowser.open("http://www.nimetabaar.ee/")
        button6 = ttk.Button(app,text="Nimeta", command=Link6)
        button6.pack()
        button6.place(x=120, y=30, width=100)

        def Link7():
            webbrowser.open("http://www.beerhouse.ee/")
        button7 = ttk.Button(app,text="Beer house", command=Link7)
        button7.pack()
        button7.place(x=10, y=80, width=100)
            
        def Link8():
            webbrowser.open("http://www.beerhouse.ee/")
        button8 = ttk.Button(app,text="Beer house", command=Link8)
        button8.pack()
        button8.place(x=120, y=80, width=100)

        def Link9():
            webbrowser.open("https://www.facebook.com/LaborBaar")
        button9 = ttk.Button(app,text="Labor", command=Link9)
        button9.pack()
        button9.place(x=120, y=120, width=100)

        def Link10():
            webbrowser.open("http://www.dubliner.ee/")
        button10 = ttk.Button(app,text="Dubliner", command=Link10)
        button10.pack()
        button10.place(x=120, y=120, width=100)

        app.mainloop()
                
    button4 = ttk.Button(app, text = "Pubid", command = Link4)
    button4.pack()
    button4.place(x=60, y=80, width=60)

    def Link13():
        app = Tk()
        app.geometry("300x100")
        app.title("Lingid")
        def Link11():
            webbrowser.open("http://www.grandrose.ee/tallinn-viimsi-spa/")
        button11 = ttk.Button(app,text="Viimsi SPA", command=Link11)
        button11.pack()
        button11.place(x=10, y=30, width=100)

        def Link12():
            webbrowser.open("http://www.meritonhotels.com/konverents_spa_hotell/")
        button12 = ttk.Button(app,text="Meriton", command=Link12)
        button12.pack()
        button12.place(x=120, y=30, width=100)

    button13 = ttk.Button(app, text = "SPA", command = Link13)
    button13.pack()
    button13.place(x=60, y=115, width=60)

    app.mainloop()
