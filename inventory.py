from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x650")
        self.resizable(False,False)

    def label(self):
        # self.backGroundImage = PhotoImage(file="backgb.png")
        # self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        # self.backGroundImageLabel.place(x=0,y=0)

        self.canvas=Canvas(self,width=240,height=650, background="grey")
        self.canvas.place(x=0,y=0)

        self.title=Label(self,text="Clutch Center",font="Bold 25", background="grey")
        self.title.place(x=2,y=20)

        self.name=Label(self,text="name",font=" 8",background="black", foreground="white",width=20)
        self.name.place(x=15,y=570)

        self.date=Label(self,text="date",font=" 8",background="black", foreground="white",width=20)
        self.date.place(x=15,y=595)
        
        self.time=Label(self,text="time",font=" 8",background="black", foreground="white",width=20)
        self.time.place(x=15,y=620)

        
        #self.canvas1=Canvas(self,width=180,height=520, background="white")
        #self.canvas1.place(x=250,y=60)        
        
    def entry(self):
        self.search=Text(self,borderwidth=0, highlightthickness=0, background="white", width=28, height=1.5)
        self.search.place(x=7,y=75)
        
    def button(self):
        self.searchButton=Button(self,text="Search",font="italic 12", command=self.login, width=12,height=2,background="lightgrey", foreground="black", border=0)
        self.searchButton.place(x=40,y=130)

        self.viewStockButton=Button(self,text="View Stock",font="italic 12", command=self.login, width=18,height=2,background="lightgrey", foreground="black", border=0)
        self.viewStockButton.place(x=20,y=250)

        self.addStockButton=Button(self,text="Add Stock",font="italic 12", command=self.login, width=18,height=2,background="lightgrey", foreground="black", border=0)
        self.addStockButton.place(x=20,y=320)

        self.reportButton=Button(self,text="Report",font="italic 12", command=self.login, width=18,height=2,background="lightgrey", foreground="black", border=0)
        self.reportButton.place(x=20,y=390)

        self.mainMenuButton=Button(self,text="Main Menu",font="italic 12", command=self.login, width=18,height=2,background="lightgrey", foreground="black", border=0)
        self.mainMenuButton.place(x=20,y=460)

       


        
    
    
    
    
    
    def treeview(self):
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
        productlist.place(x=243,y=2,width=951,height=648)






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
    
