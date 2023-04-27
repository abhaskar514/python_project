from tkinter import *
window=Tk()
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Ratin  - ')
        self.lbl2=Label(win, text='Power Factor  - ')
        self.lbl3 = Label(win, text='copper loss  - ')
        self.lbl4 = Label(win, text='iron loss  - ')
        self.lbl5 = Label(win, text='Efficiency  - ')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd = 3)
        self.t3=Entry(bd = 3)
        self.t4=Entry(bd = 3)
        self.t5 = Entry(bd = 3)
        self.btn1 = Button(win, text='Calculate')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        self.lbl5.place(x=100, y=300)
        self.t5.place(x=200, y=300)
        self.b1=Button(win, text='Calculate', command=self.add)
        self.b1.place(x=250, y=250)
    def add(self):

        num1=float(self.t1.get())
        num2=float(self.t2.get())
        num3=float(self.t3.get())
        num4=float(self.t4.get())
        a = num1*num2
        b = a + num3 + num4
        result = a/b*100

        self.t5.insert(END, str(result))



my=MyWindow(window)
window.title('Transformer efficiency')
window.geometry("400x350")
window.mainloop()