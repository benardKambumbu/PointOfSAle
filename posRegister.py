from tkinter import *


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x550")
        self.resizable(False,False)
        self.title("pos Registration")

    def label(self):
        self.backGroundImage = PhotoImage(file="regbackground_img.png")
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)

        self.canvas=Canvas(self,width=600,height=420)
        self.canvas.place(x=180,y=60)
        
        self.titles=Label(self,text="register",font="Bold 40")
        self.titles.place(x=375,y=80)
        
        self.firstNameLabel=Label(self,text="First Name :",font="Bold 10")
        self.firstNameLabel.place(x=200,y=200)
        
        self.lastNameLabel=Label(self,text="Last Name :",font="Bold 10")
        self.lastNameLabel.place(x=500,y=200)

        self.userNameLabel=Label(self,text="Username :",font="Bold 10")
        self.userNameLabel.place(x=200,y=275)
        
        
        # self.refLabel=Label(self,text="Ref code",font="Bold 10")
        # self.refLabel.place(x=310,y=200)

        self.passwordLabel=Label(self,text="Password :",font="Bold 10")
        self.passwordLabel.place(x=505,y=275)


        self.passwordLabel=Label(self,text="Confrim Password :",font="Bold 10")
        self.passwordLabel.place(x=220,y=350)
        
    def entry(self):
        self.firstName=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1)
        self.firstName.place(x=285,y=200)
        
        self.lastName=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1)
        self.lastName.place(x=585,y=200)

        self.userName=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1)
        self.userName.place(x=285,y=275)
        
        # self.ref_code=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1.8)
        # self.ref_code.place(x=580,y=275)

        self.Password=Text(self,borderwidth=0, highlightthickness=0, width=22, height=1)
        self.Password.place(x=585,y=275)

        self.cPassword=Text(self,borderwidth=0, highlightthickness=0, width=25, height=1)
        self.cPassword.place(x=350,y=350)
        
    def button(self):
        self.loginButtonImage=PhotoImage(file="button.png")
        self.loginButton=Button(self,image=self.loginButtonImage,command=self.login, width=118,height=35, border=0)
        self.loginButton.place(x=310,y=400)
        
        self.registerButtonImage=PhotoImage(file="regbutton.png")
        self.registerButton=Button(self,image=self.registerButtonImage,command=self.login,  width=118,height=35, border=0)
        self.registerButton.place(x=470,y=400)

        self.exitButton=Button(self,text="Exit",font="italic 12", command=self.login, foreground="red" ,width=10,height=2,background="grey", border=0)
        self.exitButton.place(x=645,y=425)
        
    def login(self):
        print("gigo")


if __name__=="__main__":
    login=Login()
    login.label()
    login.entry()
    login.button()
    login.login()
    login.mainloop()        
