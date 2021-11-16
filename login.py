import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error
import datetime

from posCashier import *

  
#database
def database():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                    database='pos',
                                    user='ben',
                                    # password='*Nr2?Zh?8^6e5Lap'
                                    password='dnwE$8z-M8XqE#Bk')
    cursor = conn.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
    cursor.execute("SELECT @@session.transaction_isolation")
    

#exit
def exit(root):
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#Register to login
def switch1(root):
    if 'normal' == root.state():
        root.destroy()
        login()

#login to Register 
def switch2(root):
    if 'normal' == root.state():
        root.destroy()
        register()

def switch4(root):
    if 'normal' == root.state():
        root.destroy()
        cashier()

def switch5(root):
    if 'normal' == root.state():
        root.destroy()
        inventory()

def switch6(root):
    if 'normal' == root.state():
        root.destroy()
        addProduct()
def switch7(root):
    if 'normal' == root.state():
        root.destroy()
        home()




   


def home(): 
    root = tk.Tk()
    root.geometry("900x450")
    root.resizable(False,False)
    
    backGroundImage = PhotoImage(file="background_img.png")
    backGroundImageLabel=Label(root,image=backGroundImage)
    backGroundImageLabel.place(x=0,y=0)

    canvas=Canvas(root,width=390,height=300,background="white")
    canvas.place(x=250,y=60)
    
    title=Label(root,text="Mainmenu",font="Bold 30",background="white")
    title.place(x=355,y=80)
        
   
    cashierButton=Button(root,text="Cashier page",font="italic 12", command= lambda : switch4(root), width=10,height=3,background="lightgrey", foreground="black", border=0)
    cashierButton.place(x=280,y=150)

    AdminButton=Button(root,text="Admin Page",font="italic 12", command= lambda : switch5(root), width=10,height=3,background="lightgrey", foreground="black", border=0)
    AdminButton.place(x=476,y=150)

    logoutButton=Button(root,text="Logout",font="italic 12", command=lambda : exit(root), width=18,height=2,background="lightgrey", foreground="black", border=0)
    logoutButton.place(x=350,y=250)
    root.mainloop()  

def switch3(root):
    if 'normal' == root.state():
        root.destroy()
        home()

#entry point login
def loginCheck(root,username,password):
    username = str(username.get("1.0",'end-1c'))
    password = str(password.get("1.0",'end-1c'))
    
    database()
    if  username == "" or  password == "":
        result = tkMessageBox.showerror('Error', 'You need to fill all fields')
    else:
        cursor.reset()
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s",(username,password))
        x = cursor.fetchone()
        print(cursor.rowcount)
        if x :
            switch3(root)  
        else:
            result = tkMessageBox.showerror('Error', 'user or password not correct', icon="warning") 
            
        cursor.close()
        conn.close()

def login(): 
    root = tk.Tk()
    
    root.geometry("900x450")
    root.resizable(False,False)
    root.title("bkAfrica POS")

    root.backGroundImage = PhotoImage(file="background_img.png")
    root.backGroundImageLabel=Label(root,image=root.backGroundImage)
    root.backGroundImageLabel.place(x=0,y=0)
    root.canvas=Canvas(root,width=390,height=300)
    root.canvas.place(x=250,y=60)    
    title=Label(root,text="Login",font="Bold 30")
    title.place(x=395,y=80)    
    userNameLabel=Label(root,text="Username",font="Bold 10")
    userNameLabel.place(x=310,y=150)
    passwordLabel=Label(root,text="Password",font="Bold 10")
    passwordLabel.place(x=310,y=200)
    username=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1.2)
    username.place(x=390,y=150)
    password=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1.2)
    password.place(x=390,y=200)

    loginButtonImage=PhotoImage(file="button.png")
    submitbtn1=Button(root,image=loginButtonImage,command = lambda:  loginCheck(root,username,password), width=118,height=35, border=0)
    submitbtn1.place(x=310,y=255)
        
    registerButtonImage=PhotoImage(file="regbutton.png")
    submitbtn3=Button(root,image=registerButtonImage,command= lambda: switch2(root),  width=118,height=35, border=0)
    submitbtn3.place(x=470,y=255)

    submitbtn2=Button(root,text="Exit",font="italic 12", command= lambda: exit(root), foreground="red" ,width=10,height=1,background="grey", border=0)
    submitbtn2.place(x=395,y=305)
    

    
    root.mainloop()  

##############################################RegisterUser###############################################

def registerCommit(root,firstname, lastname, username, position,password,password1):
    firstname = firstname.get("1.0",'end-1c')
    lastname = lastname.get("1.0",'end-1c')
    username = username.get("1.0",'end-1c')
    position = position.get("1.0",'end-1c')
    password = password.get("1.0",'end-1c')
    password1 = password1.get("1.0",'end-1c')

    database()
    if firstname == "" or lastname == "" or username == "" or position == "" or password == "" or password1 == "":
        # lbl_result.config(text="Please complete the required field!", fg="orange")
        result = tkMessageBox.showerror('Error', 'You need to fill all fields')
        #if result == :
    else:
        cursor.reset()
        x = cursor.execute("SELECT * FROM `user` WHERE `username` = username")
        print(username)
        if x is not None:
        
            result = tkMessageBox.showerror('Error', 'Username Takken', icon="warning") 
        elif password != password1:
            result = tkMessageBox.showerror('Error', 'Password do not match', icon="warning") 
        else:
           
            cursor.reset() 
            cursor.execute("INSERT INTO `user` (firstname,lastname,username,position,password) VALUES( %s, %s, %s, %s, %s)", (str(firstname), str(lastname), str(username), str(position), str(password)))
            
            conn.commit()
            cursor.reset()
            cursor.execute("SELECT * FROM `user` WHERE `username` = username")
            y = ''
            if cursor.fetchone() is not None:
                x = cursor.fetchone()
                y = 'cc00' + str(x[0])
            result = tkMessageBox.showinfo('System', 'Registration for user ' + username + 'was successfull. Your user ID is ' + y)
            if result == 'ok':
                switch1(root) 
        cursor.close()
        conn.close()


def register(): 

    root = tk.Tk()
    root.geometry("1000x550")
    root.resizable(False,False)
    root.title("pos Registration")
    

    backGroundImage = PhotoImage(file="regbackground_img.png")
    backGroundImageLabel=Label(root,image=backGroundImage)
    backGroundImageLabel.place(x=0,y=0)
    canvas=Canvas(root,width=600,height=420)
    canvas.place(x=180,y=60)
    
    titles=Label(root,text="register",font="Bold 40")
    titles.place(x=375,y=80)
    
    firstNameLabel=Label(root,text="First Name :",font="Bold 10")
    firstNameLabel.place(x=200,y=200)
    
    lastNameLabel=Label(root,text="Last Name :",font="Bold 10")
    lastNameLabel.place(x=500,y=200)

    userNameLabel=Label(root,text="Username :",font="Bold 10")
    userNameLabel.place(x=200,y=275)
    
    positionLabel=Label(root,text="Postion",font="Bold 10")
    positionLabel.place(x=500,y=275)
    
    

    passwordLabel=Label(root,text="Password :",font="Bold 10")
    passwordLabel.place(x=200,y=350)


    cpasswordLabel=Label(root,text="Confrim Password :",font="Bold 10")
    cpasswordLabel.place(x=500,y=350)

    

    firstname=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    firstname.place(x=285,y=200)
    
    lastname=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    lastname.place(x=585,y=200)

    username=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    username.place(x=285,y=275)
    
    position=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    position.place(x=585,y=275)

    password=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    password.place(x=285,y=350)

    password1=Text(root,borderwidth=0, highlightthickness=0, width=22, height=1)
    password1.place(x=585,y=350)
    

    loginButtonImage=PhotoImage(file="button.png")
    loginButton=Button(root,image=loginButtonImage,command= lambda: switch1(root), width=118,height=35, border=0)
    loginButton.place(x=310,y=400)
    
    registerButtonImage=PhotoImage(file="regbutton.png")
    registerButton=Button(root,image=registerButtonImage,command = lambda : registerCommit(root,firstname, lastname, username, position,password,password1),  width=118,height=35, border=0)
    registerButton.place(x=470,y=400)

    exitButton=Button(root,text="Exit",font="italic 12", command= lambda: exit(root), foreground="red" ,width=10,height=2,background="grey", border=0)
    exitButton.place(x=645,y=425)
        


    
    root.mainloop()  




#create product
def addProductCommit(root,state,productId, productName, productDescription,productCategory,productPrice):

    productIdEntry = productId 
    productNameEntry = productName
    productCategoryEntry = productCategory
    productDescriptionEntry  = productDescription
    productPriceEntry = productPrice

    productId = productId.get()
    productName = productName.get()
    productCategory = productCategory.get()
    productDescription = productDescription.get()
    productPrice = productPrice.get()

    print('check')
    database()
    print(state)
    if state == 'search':
        cursor.reset()
        cursor.execute("SELECT * FROM `products` WHERE `productId` = %s AND `productName` = %s", (productId,productName,))
        product = cursor.fetchone()
        
        found = False
        if product is not None:
            print(product)
            y = [product[1],product[2],product[3],product[4],product[5]]
            found = True
        cursor.reset()
        cursor.execute("SELECT * FROM `products` WHERE `productId` = %s", (productId,))
        product1 = cursor.fetchone()
        if product1 is not None:
            print(product)
            y = [product1[1],product1[2],product1[3],product1[4],product1[5]]
            found = True
        if found == True:
            productIdEntry.delete(0,"end")
            productIdEntry.insert(0,y[0])
            productNameEntry.delete(0,"end")
            productNameEntry.insert(0,y[1])
            productDescriptionEntry.delete(0,"end")
            productDescriptionEntry.insert(0,y[2])
            productCategoryEntry.delete(0,"end")
            productCategoryEntry.insert(0,y[3])
            productPriceEntry.delete(0,"end")
            productPriceEntry.insert(0,y[4])    
            return

    elif state == 'edit':
        cursor.reset()
        cursor.execute("SELECT * FROM `products` WHERE `productId` = %s ", (productId,))
        product = cursor.fetchone()
        if product is not None:

            cursor.execute("UPDATE products SET productName=%s, productDescription = %s,productCategory = %s, productPrice = %s  WHERE productId = %s;", (productName,productDescription,productCategory,productPrice,productId,))
            conn.commit()
            root.destroy()
            addProduct()
            
            
        else:
            result = tkMessageBox.showerror('Error', 'Failed to update')


    elif state == 'add':
        try:
            x = float(productPrice )
        except ValueError:
            result = tkMessageBox.showerror('Error', 'Price must be a decimal or interger')
        if productId == "" or productName == "" or productDescription == "" or productCategory == "" or  productPrice== "" :
            result = tkMessageBox.showerror('Error', 'You need to fill all fields')
        else:
            cursor.reset()
            cursor.execute("SELECT * FROM `products` WHERE `productId` = %s", (productId,))
            if cursor.fetchone() is not None:
                result = tkMessageBox.showerror('Error', 'ProductId already Exists', icon="warning") 
            cursor.reset()
            cursor.execute("SELECT * FROM `products` WHERE `productName` = %s ", (productName,))
            if cursor.fetchone() is not None:
                result = tkMessageBox.showerror('Error', 'productName Exists', icon="warning") 
            else:
            
                cursor.reset() 
                cursor.execute("INSERT INTO `products` (productId,productName,productDescription,productCategory,productPrice) VALUES( %s, %s, %s, %s, %s)", (str(productId), str(productName), str(productDescription), str(productCategory), productPrice))      
                conn.commit()
                cursor.reset()
                cursor.execute("SELECT * FROM `products` WHERE `productId` = %s", (productId,))
                y = ''
                if cursor.fetchone() is not None:
                    x = cursor.fetchone()
                    y = productId
                result = tkMessageBox.showinfo('System', 'Registration for product ' + productName + 'was successfull. Your product ID is ' + y)
                if result == 'ok':
                    switch1(root)
                
    elif state == 'delete':
        cursor.reset()
        cursor.execute("SELECT * FROM `products` WHERE `productId` = %s", (productId,))
        product = cursor.fetchone()
        if product is not None:

            cursor.execute("DELETE FROM products  WHERE productId = %s", (productId,))
            conn.commit()
            root.destroy()
            addProduct()
        
        
    cursor.close()
    conn.close()

def selectItem(productlist,productId, productName,  productDescription,productCategory,productPrice):
    curItem = productlist.focus()
    productId.delete(0,"end")
    productId.insert(0,productlist.item(curItem)['values'][0])
    productName.delete(0,"end")
    productName.insert(0,productlist.item(curItem)['values'][1])
    productDescription.delete(0,"end")
    productDescription.insert(0,productlist.item(curItem)['values'][2])
    productCategory.delete(0,"end")
    productCategory.insert(0,productlist.item(curItem)['values'][3])
    productPrice.delete(0,"end")
    productPrice.insert(0,productlist.item(curItem)['values'][4])
    
    
def addProduct(): 
    root = tk.Tk()
    root.geometry("1180x560")
    root.title("bkAfrica Motor Spares")
    database()

    canvas=Canvas(root,width=350,height=1000, background="grey")
    canvas.place(x=0,y=0)

    lblsecrow = tk.Label(root, text ="bkAfrica Registry", fg = 'blue', font="25")
    lblsecrow.place(x = 20, y = 20)
    # Defining the first row
    lblfrstrow = tk.Label(root, text ="Product id :", fg = 'blue', )
    lblfrstrow.place(x = 20, y = 80)
    productId = tk.Entry(root, width = 35)
    productId.place(x = 165, y = 80, width = 160)

    lblsecrow = tk.Label(root, text ="Product Name :", fg = 'blue', )
    lblsecrow.place(x = 20, y = 130)
    productName = tk.Entry(root, width = 35)
    productName.place(x = 165, y = 130, width = 160)

    lblrow6 = tk.Label(root, text ="Product Cartegory :", fg = 'blue',)
    lblrow6.place(x = 20, y = 180)
    productCategory = tk.Entry(root, width = 35)

    productCategory.place(x = 165, y = 180, width = 160)

    lblrow3 = tk.Label(root, text ="Product Description :", fg = 'blue',)
    lblrow3.place(x = 20, y = 230)
    productDescription = tk.Entry(root, width = 35, )
    productDescription.place(x = 165, y = 230, width = 160)
    

    lblrow4 = tk.Label(root, text ="Product Price :", fg = 'blue',)
    lblrow4.place(x = 20, y = 280)
    productPrice = tk.Entry(root, width = 35)
    productPrice.place(x = 165, y = 280, width = 160)

    # Using treeview widget
    productlist = ttk.Treeview(root, selectmode ='browse')
    productlist.place(x = 355, y = 5, width = 800, height = 550)
    productlist.bind('<ButtonRelease-1>', lambda eff: selectItem(productlist,productId, productName,  productDescription,productCategory,productPrice))
    scrollbar = Scrollbar(root)
    scrollbar.place(x = 1154, y = 6, width = 12, height = 551)
    
    productlist.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = productlist.yview)
    
    productlist["columns"] = ("1", "2", "3", "4","5")
    productlist['show'] = 'headings'
    productlist.column("1", width = 90, anchor ='c')
    productlist.column("2", width = 90, anchor ='se')
    productlist.column("3", width = 90, anchor ='se')
    productlist.column("4", width = 90, anchor ='se')
    productlist.column("5", width = 90, anchor ='se')
    
    productlist.heading("1", text ="Product Id")
    productlist.heading("2", text ="Product Name")
    productlist.heading("3", text ="Product Descr")
    productlist.heading("4", text ="Product Cat")
    productlist.heading("5", text ="Product Price")
    cursor.reset()
    cursor.execute("SELECT * FROM `products` ")
    for row in cursor.fetchall():
        print(row)
        productlist.insert("", 'end', text ="L1",
                    values =(row[1],row[2],row[3],row[4],row[5]))
    
 
   
    #productlist = Listbox(root, fg = 'blue',)
    
    
    
    submitbtn3 = tk.Button(root, text ="Save",bg ='blue', fg = 'white',command = lambda: addProductCommit(root,'add',productId, productName,  productDescription,productCategory,productPrice))
    submitbtn3.place(x = 20, y = 350, width = 100)

    submitbtn2 = tk.Button(root, text ="Edit",bg ='blue', fg = 'white',command= lambda: addProductCommit(root,'edit',productId, productName,  productDescription,productCategory,productPrice))
    submitbtn2.place(x = 150, y = 350, width = 100)

    submitbtn1 = tk.Button(root, text ="delete",fg = 'red',bg='blue',command= lambda: addProductCommit(root,'delete',productId, productName,  productDescription,productCategory,productPrice))
    submitbtn1.place(x = 20, y = 400, width = 100)

    submitbtn4 = tk.Button(root, text ="search",bg ='blue', fg = 'white',command= lambda: addProductCommit(root,'search',productId, productName,  productDescription,productCategory,productPrice))
    submitbtn4.place(x = 150, y = 400, width = 100)

    exitButton=Button(root,text="Menu",font="italic 12", command=lambda : switch7(root), foreground="red" ,width=10,height=2, border=0)
    exitButton.place(x=5,y=500)
    


    root.mainloop()  

def selectItem(productlist,productId, productName,  productDescription,productCategory,productPrice):
    curItem = productlist.focus()
    productId.delete(0,"end")
    productId.insert(0,productlist.item(curItem)['values'][0])
    productName.delete(0,"end")
    productName.insert(0,productlist.item(curItem)['values'][1])
    productDescription.delete(0,"end")
    productDescription.insert(0,productlist.item(curItem)['values'][2])
    productCategory.delete(0,"end")
    productCategory.insert(0,productlist.item(curItem)['values'][3])
    productPrice.delete(0,"end")
    productPrice.insert(0,productlist.item(curItem)['values'][4])
    
 
#home()    
dict = []
def selectItem1(productlist):
    curItem = productlist.focus()
    x1 = productlist.item(curItem)['values'][0]
    x2 = productlist.item(curItem)['values'][1]
    x3 = productlist.item(curItem)['values'][2]
    x = [x1,x2,x3]
    dict.append(x)
    print(productlist.item(curItem)['values'][2])
    print(dict)
    
 
    

def cashier():
    root = root = tk.Tk()
    root.geometry("1330x650")
    root.resizable(False,False)
    database()
    backGroundImage = PhotoImage(file="backgb.png")
    backGroundImageLabel=Label(root,image=backGroundImage)
    backGroundImageLabel.place(x=0,y=0)

    canvas=Canvas(root,width=1080,height=580, background="grey")
    canvas.place(x=130,y=20)

    title=Label(root,text="bkAfrica",font="Bold 35")
    title.place(x=500,y=30)

    position=Label(root,text="position",font="italic 10",width=20)
    position.place(x=135,y=35)

    name=Label(root,text="name",font="italic 10",width=20)
    name.place(x=135,y=70)

    now = datetime.datetime.now()
    t1 = now.strftime("%Y-%m-%d")
    t2 = now.strftime("%H:%M:%S")
    date=Label(root,text=t1,font=" 8",width=20)
    date.place(x=995,y=35)
    
    time=Label(root,text=t2,font=" 8", width=20)
    time.place(x=995,y=70)

    searchButtonImage=PhotoImage(file="search.png")
    searchButton=Button(root,image=searchButtonImage,command=login, width=118,height=36, border=0)
    searchButton.place(x=480,y=201)

    addButtonImage=PhotoImage(file="addbtn.png")
    addButton=Button(root,image=addButtonImage,command=login, width=110,height=31,borderwidth=0, border=0)
    addButton.place(x=480,y=289)

    checkoutButtonImage=PhotoImage(file="checkout.png")
    checkoutButton=Button(root,image=checkoutButtonImage,command=login, width=118,height=35, border=0)
    checkoutButton.place(x=480,y=455)

    userName=Text(root,borderwidth=0, highlightthickness=0, background="white", width=37, height=1.75)
    userName.place(x=150,y=200)
    
    exitButton=Button(root,text="Exit",font="italic 12",  command=lambda : exit(root), foreground="red" ,width=10,height=2,background="grey", border=0)
    exitButton.place(x=2,y=1)

    menuButton=Button(root,text="Menu",font="italic 12",  command=lambda : switch7(root), foreground="black" ,width=10,height=2,background="grey", border=0)
    menuButton.place(x=2,y=1)
    
    productlist = ttk.Treeview(root)
    productlist.bind('<ButtonRelease-1>', lambda eff : selectItem1(productlist))
    # productlist['columns'] = ('Rank', 'Name', 'Badge
    # productlist.column('#0', width = 0, stretch = NO)
    # productlist.column('Rank', anchor = CENTER, width = 10)
    # productlist.column('Name', anchor = CENTER, width = 20)
    # productlist.column('Badge', anchor = CENTER, width = 10)

    productlist["columns"] = ("1", "2", "3")
    productlist['show'] = 'headings'
    productlist.column("1", width = 9, anchor ='c')
    productlist.column("2", width = 9, anchor ='se')
    productlist.column("3", width = 9, anchor ='se')

    
    productlist.heading("1", text =" Name")
    productlist.heading("2", text =" Descr")
    productlist.heading("3", text ="Price")
    cursor.reset()
    cursor.execute("SELECT * FROM `products` ")
    for row in cursor.fetchall():
        print(row)
        productlist.insert("", 'end', text ="L1",
                    values =(row[2],row[3],row[5]))
    productlist.place(x=150,y=270,width=301,height=268)
    # productlist.place(x=200,y=280)

    cart = ttk.Treeview(root)
    
    cart["columns"] = ("1", "2", "3", "4","5")
    cart['show'] = 'headings'
    cart.column("1", width = 90, anchor ='c')
    cart.column("2", width = 90, anchor ='se')
    cart.column("3", width = 90, anchor ='se')
    cart.column("4", width = 90, anchor ='se')
    cart.column("5", width = 90, anchor ='se')
    
    cart.heading("1", text ="Product Id")
    cart.heading("2", text ="Product Name")
    cart.heading("3", text ="Product Descr")
    cart.heading("4", text ="Product Cat")
    cart.heading("5", text ="Product Price")
    cursor.reset()
    cursor.execute("SELECT * FROM `products` ")
    for row in cursor.fetchall():
        print(row)
        cart.insert("", 'end', text ="L1",
                    values =(row[1],row[2],row[3],row[4],row[5]))
    
    cart.place(x=650,y=120,width=550,height=440)

    root.mainloop() 


def inventory():
    root = tk.Tk()
    root.geometry("1200x650")
    root.resizable(False,False)

    database()
    canvas=Canvas(root,width=240,height=650, background="grey")
    canvas.place(x=0,y=0)

    title=Label(root,text="bkAfrica Motors",font="Bold 20", background="grey")
    title.place(x=2,y=20)

    # cursor.reset()
    # cursor.execute("SELECT * FROM `products` WHERE `productId` = %s AND `productName` = %s", (productId,productName,))
    # product = cursor.fetchone()
        
    name=Label(root,text="name",font=" 8",background="black", foreground="white",width=20)
    name.place(x=15,y=570)

    now = datetime.datetime.now()
    t1 = now.strftime("%Y-%m-%d")
    t2 = now.strftime("%H:%M:%S")
    date=Label(root,text= t1 ,font=" 8",background="black", foreground="white",width=20)
    date.place(x=15,y=595)
    
    time=Label(root,text=t2,font=" 8",background="black", foreground="white",width=20)
    time.place(x=15,y=620)
    search=Text(root,borderwidth=0, highlightthickness=0, background="white", width=28, height=1.5)
    search.place(x=7,y=75)
        
    searchButton=Button(root,text="Search",font="italic 12", command=login, width=12,height=2,background="lightgrey", foreground="black", border=0)
    searchButton.place(x=40,y=130)

    viewStockButton=Button(root,text="View Stock",font="italic 12", command=login, width=18,height=2,background="lightgrey", foreground="black", border=0)
    viewStockButton.place(x=20,y=250)

    addStockButton=Button(root,text="Add Stock",font="italic 12", command=lambda : switch6(root), width=18,height=2,background="lightgrey", foreground="black", border=0)
    addStockButton.place(x=20,y=320)

    reportButton=Button(root,text="Report",font="italic 12", command=login, width=18,height=2,background="lightgrey", foreground="black", border=0)
    reportButton.place(x=20,y=390)

    mainMenuButton=Button(root,text="Main Menu",font="italic 12", command=lambda : switch7(root), width=18,height=2,background="lightgrey", foreground="black", border=0)
    mainMenuButton.place(x=20,y=460)       

    productlist = ttk.Treeview(root)
    # productlist['columns'] = ('Rank', 'Name', 'Badge')
    # productlist.column('#0', width = 0, stretch = NO)
    # productlist.column('Rank', anchor = CENTER, width = 10)
    # productlist.column('Name', anchor = CENTER, width = 20)
    # productlist.column('Badge', anchor = CENTER, width = 10)
    
    productlist["columns"] = ("1", "2", "3", "4","5")
    productlist['show'] = 'headings'
    productlist.column("1", width = 90, anchor ='c')
    productlist.column("2", width = 90, anchor ='se')
    productlist.column("3", width = 90, anchor ='se')
    productlist.column("4", width = 90, anchor ='se')
    productlist.column("5", width = 90, anchor ='se')
    
    productlist.heading("1", text ="Product Id")
    productlist.heading("2", text ="Product Name")
    productlist.heading("3", text ="Product Descr")
    productlist.heading("4", text ="Product Cat")
    productlist.heading("5", text ="Product Price")
    cursor.reset()
    cursor.execute("SELECT * FROM `products` ")
    for row in cursor.fetchall():
        print(row)
        productlist.insert("", 'end', text ="L1",
                    values =(row[1],row[2],row[3],row[4],row[5]))
    productlist.place(x=243,y=2,width=951,height=648)

    root.mainloop() 




    


login()
