from tkinter import *
from login import *


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x450")
        self.resizable(False,False)



    def label(self):
        self.backGroundImage = PhotoImage(file="background_img.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)

        self.canvas=Canvas(self,width=390,height=300)
        self.canvas.place(x=250,y=60)
        
        self.title=Label(self,text="Login",font="Bold 30")
        self.title.place(x=395,y=80)
        
        self.userNameLabel=Label(self,text="Username",font="Bold 10")
        self.userNameLabel.place(x=310,y=150)
        
        self.passwordLabel=Label(self,text="Password",font="Bold 10")
        self.passwordLabel.place(x=310,y=200)
        
    def entry(self):
        self.username=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1.2)
        self.username.place(x=390,y=150)
        
        self.password=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1.2)
        self.password.place(x=390,y=200)
        
    def button(self):
        self.loginButtonImage=PhotoImage(file="button.png")
        self.loginButton=Button(self,image=self.loginButtonImage,command = lambda:  self.loginCheck(self,self.username,self.password), width=118,height=35, border=0)
        self.loginButton.place(x=310,y=255)
        
        self.registerButtonImage=PhotoImage(file="regbutton.png")
        self.registerButton=Button(self,image=self.registerButtonImage,command= lambda: switch1(self),  width=118,height=35, border=0)
        self.registerButton.place(x=470,y=255)

        self.exitButton=Button(self,text="Exit",font="italic 12", command= lambda:self (self), foreground="red" ,width=10,height=1,background="grey", border=0)
        self.exitButton.place(x=395,y=305)
        
    def login(self):
        print("gigo")


if __name__=="__main__":
    login=Login()
    login.label()
    login.entry()
    login.button()
    login.login()
    login.mainloop()        
