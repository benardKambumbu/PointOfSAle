from tkinter import *


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x450")
        self.resizable(False,False)
    def label(self):
        self.backGroundImage = PhotoImage(file="background_img.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)

        self.canvas=Canvas(self,width=390,height=300,background="white")
        self.canvas.place(x=250,y=60)
        
        self.title=Label(self,text="Mainmenu",font="Bold 30",background="white")
        self.title.place(x=355,y=80)
        
        
        
   
        
    def button(self):
        self.cashierButton=Button(self,text="Cashier page",font="italic 12", command=self.login, width=10,height=3,background="lightgrey", foreground="black", border=0)
        self.cashierButton.place(x=280,y=150)

        self.AdminButton=Button(self,text="Admin Page",font="italic 12", command=self.login, width=10,height=3,background="lightgrey", foreground="black", border=0)
        self.AdminButton.place(x=476,y=150)

        self.logoutButton=Button(self,text="Logout",font="italic 12", command=self.login, width=18,height=2,background="lightgrey", foreground="black", border=0)
        self.logoutButton.place(x=350,y=250)

    def login(self):
        print("gigo")


if __name__=="__main__":
    login=Login()
    login.label()
    login.button()
    login.login()
    login.mainloop()        
