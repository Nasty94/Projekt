from tkinter import *
from tkinter import ttk
import webbrowser
from pyquery import PyQuery as pq
import requests

def näita():
    page = requests.get('http://www.tartupiljard.ee/hinnakiri/')
    page_html = page.text
    q = pq(page_html)
    hinnakiri = q(q('div.entry p')[1]).text()

    järjend1 = hinnakiri.split('T')
    järjend2 = []
    for i in range(len(järjend1)):
        if järjend1[i] == '':
            pass
        else:
            järjend2.append('T' + järjend1[i])

    järjend1 = []
    for element in järjend2:
        if 'S' in element:
            järjend1.append(element.split('S'))
        else:
            järjend1.append(element)

    järjend2 = []
    for i in range(len(järjend1)):
        if type(järjend1[i]) != list:
            järjend2.append(järjend1[i])
        else:
            järjend2.append(järjend1[i][0])
            järjend2.append('S' + järjend1[i][1])
            järjend2.append('S' + järjend1[i][2])

    app = Toplevel()
    app.geometry("700x400+400+100")
    app.title("Vaba aeg")

    canvas = Canvas(app,width = 500, height = 500, bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'LinksPildid/Tartu/muuTartu.gif')
    canvas.create_image(200,30, image = gif1, anchor = NW)


    lst = Listbox(app, activestyle='dotbox',\
              fg='black', highlightbackground='blue',\
              highlightcolor='green', width=110)
    lst.insert(END,"Piljard:")
    lst.insert(END, "        ")

    for j in range(len(järjend2)):
        lst.insert(END,järjend2[j])

    lst.insert(END, "         ")
    lst.insert(END,"NB! Rohkem info saamiseks vajutage sobivat nuppu")
    lst.place(x=10, y=200)


    def Link1():
        webbrowser.open("http://www.tartupiljard.ee/")
    button1 = ttk.Button(app, text = "Piljard", command = Link1)
    button1.pack()
    button1.place(x=70, y=50, width=60)

    app.mainloop()
