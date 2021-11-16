from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview


class cashier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1330x650")
        self.resizable(False,False)

    def label(self):
        self.backGroundImage = PhotoImage(file="backgb.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)

        self.canvas=Canvas(self,width=1080,height=580, background="grey")
        self.canvas.place(x=130,y=20)

        self.title=Label(self,text="Clutch Center",font="Bold 35")
        self.title.place(x=500,y=30)

        self.position=Label(self,text="position",font="italic 10",width=20)
        self.position.place(x=135,y=35)

        self.name=Label(self,text="name",font="italic 10",width=20)
        self.name.place(x=135,y=70)

        self.date=Label(self,text="date",font=" 8",width=20)
        self.date.place(x=995,y=35)
        
        self.time=Label(self,text="time",font=" 8", width=20)
        self.time.place(x=995,y=70)

        
        #self.canvas1=Canvas(self,width=180,height=520, background="white")
        #self.canvas1.place(x=250,y=60)        
        
    def entry(self):
        self.userName=Text(self,borderwidth=0, highlightthickness=0, background="white", width=32, height=1.75)
        self.userName.place(x=190,y=200)
        
    def button(self):
        self.searchButtonImage=PhotoImage(file="search.png")
        self.searchButton=Button(self,image=self.searchButtonImage,command=self.login, width=118,height=36, border=0)
        self.searchButton.place(x=480,y=201)

        self.addButtonImage=PhotoImage(file="addbtn.png")
        self.addButton=Button(self,image=self.addButtonImage,command=self.login, width=110,height=31,borderwidth=0, border=0)
        self.addButton.place(x=480,y=289)

        self.checkoutButtonImage=PhotoImage(file="checkout.png")
        self.checkoutButton=Button(self,image=self.checkoutButtonImage,command=self.login, width=118,height=35, border=0)
        self.checkoutButton.place(x=480,y=455)
        
    def treeview(self):
        tv = ttk.Treeview(self)
        tv['columns'] = ('Rank', 'Name', 'Badge')
        tv.column('#0', width = 0, stretch = NO)
        tv.column('Rank', anchor = CENTER, width = 80)
        tv.column('Name', anchor = CENTER, width = 80)
        tv.column('Badge', anchor = CENTER, width = 80)

        tv.heading('#0', text = '', anchor = CENTER)
        tv.heading('Rank', text = 'Id', anchor = CENTER)
        tv.heading('Name', text = 'rank', anchor = CENTER)
        tv.heading('Badge', text = 'Badge', anchor = CENTER)

        tv.insert(parent = '', index = 0, iid = 0, text = '', values = ('1', 'Vineet', 'Alpha'))
        tv.insert(parent = '', index = 1, iid = 1, text = '', values = ('2', 'Anil', 'Bravo'))
        tv.insert(parent = '', index = 2, iid = 2, text = '', values = ('3', 'Vinod', 'Charlie'))
        tv.insert(parent = '', index = 3, iid = 3, text = '', values = ('4', 'Vimal', 'Delta'))
        tv.insert(parent = '', index = 4, iid = 4, text = '', values = ('5', 'Manjeet', 'Echo'))
        tv.place(x=200,y=280)

        productlist = ttk.Treeview(self)
        productlist['columns'] = ('Rank', 'Name', 'Badge')
        productlist.column('#0', width = 0, stretch = NO)
        productlist.column('Rank', anchor = CENTER, width = 10)
        productlist.column('Name', anchor = CENTER, width = 20)
        productlist.column('Badge', anchor = CENTER, width = 10)

        productlist.heading('#0', text = '', anchor = CENTER)
        productlist.heading('Rank', text = 'Id', anchor = CENTER)
        productlist.heading('Name', text = 'rank', anchor = CENTER)
        productlist.heading('Badge', text = 'Badge', anchor = CENTER)

        productlist.insert(parent = '', index = 0, iid = 0, text = '', values = ('1', 'Vineet', 'Alpha'))
        productlist.insert(parent = '', index = 1, iid = 1, text = '', values = ('2', 'Anil', 'Bravo'))
        productlist.insert(parent = '', index = 2, iid = 2, text = '', values = ('3', 'Vinod', 'Charlie'))
        productlist.insert(parent = '', index = 3, iid = 3, text = '', values = ('4', 'Vimal', 'Delta'))
        productlist.insert(parent = '', index = 4, iid = 4, text = '', values = ('5', 'Manjeet', 'Echo'))
        productlist.place(x=650,y=120,width=550,height=440)






    def login(self):
        print("gigo")  


        
     
        
    
if __name__=="__main__":
    login=Login()
    login.label()
    login.entry()
    login.button()
    login.login()
    login.treeview()
    login.mainloop()     
    
