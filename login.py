import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error

  
#database
def database():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                    database='pos',
                                    user='ben',
                                    password='*Nr2?Zh?8^6e5Lap')
    cursor = conn.cursor()
    

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


#entry point login
def loginCheck(root,username,password):
    username = str(username.get())
    password = str(password.get())
    
    database()
    if  username == "" or  password == "":
        result = tkMessageBox.showerror('Error', 'You need to fill all fields')
    else:
        cursor.reset()
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s",(username,password))
        x = cursor.fetchone()
        print(cursor.rowcount)
        if x :
            switch2(root)  
        else:
            result = tkMessageBox.showerror('Error', 'user or password not correct', icon="warning") 
            
        cursor.close()
        conn.close()

def login(): 
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Clutch Center Motor Spares")
    
    lblsecrow = tk.Label(root, text ="Welcome to CLutch Center", fg = 'blue',)
    lblsecrow.place(x = 170, y = 100)
    # Defining the first row
    lblfrstrow = tk.Label(root, text ="Username:", fg = 'blue', )
    lblfrstrow.place(x = 150, y = 200)
    
    username = tk.Entry(root, width = 35)
    username.place(x = 250, y = 200, width = 150)

    lblsecrow = tk.Label(root, text ="Password:", fg = 'blue',)
    lblsecrow.place(x = 150, y = 250)
    
    password = tk.Entry(root, width = 35)
    password.place(x = 250, y = 250, width = 150)
    
    submitbtn1 = tk.Button(root, text ="Login",bg ='blue', fg = 'white',command = lambda: loginCheck(root,username,password))
    submitbtn1.place(x = 200, y = 350, width = 70)

    submitbtn2 = tk.Button(root, text ="exit",bg ='blue', fg = 'white',command= lambda: exit(root))
    submitbtn2.place(x = 300, y = 350, width = 65)

    submitbtn3 = tk.Button(root, text ="Register",fg = 'blue',command= lambda: switch1(root))
    submitbtn3.place(x = 300, y = 400, width = 100)
    
    root.mainloop()  

##############################################RegisterUser###############################################

def registerCommit(root,firstname, lastname, username, position,password,password1):
    firstname = firstname.get()
    lastname = lastname.get()
    username = username.get()
    position = position.get()
    password = password.get()
    password1 = password1.get()

    database()
    if firstname == "" or lastname == "" or username == "" or position == "" or password == "" or password1 == "":
        # lbl_result.config(text="Please complete the required field!", fg="orange")
        result = tkMessageBox.showerror('Error', 'You need to fill all fields')
        #if result == :
    else:
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
    root.geometry("500x500")
    root.title("Clutch Center Motor Spares")
    
    lblsecrow = tk.Label(root, text ="CLutch Center Registry", fg = 'blue',)
    lblsecrow.place(x = 170, y = 10)
    # Defining the first row
    lblfrstrow = tk.Label(root, text ="First Name:", fg = 'blue', )
    lblfrstrow.place(x = 120, y = 50)
    firstname = tk.Entry(root, width = 35)
    firstname.place(x = 250, y = 50, width = 150)

    lblsecrow = tk.Label(root, text ="Last Name:", fg = 'blue', )
    lblsecrow.place(x = 120, y = 100)
    lastname = tk.Entry(root, width = 35)
    lastname.place(x = 250, y = 100, width = 150)

    lblrow6 = tk.Label(root, text ="Position:", fg = 'blue',)
    lblrow6.place(x = 120, y = 150)
    position = tk.Entry(root, width = 35)
    position.place(x = 250, y = 150, width = 150)

    lblrow3 = tk.Label(root, text ="Username:", fg = 'blue',)
    lblrow3.place(x = 120, y = 200)
    username = tk.Entry(root, width = 35)
    username.place(x = 250, y = 200, width = 150)

    lblrow4 = tk.Label(root, text ="password:", fg = 'blue',)
    lblrow4.place(x = 120, y = 250)
    password = tk.Entry(root, width = 35)
    password.place(x = 250, y = 250, width = 150)

    lblrow5 = tk.Label(root, text ="verify password:", fg = 'blue',)
    lblrow5.place(x = 120, y = 300)
    password1 = tk.Entry(root, width = 35)
    password1.place(x = 250, y = 300, width = 150)

    
    
    submitbtn3 = tk.Button(root, text ="Register",bg ='blue', fg = 'white',command = lambda: registerCommit(root,firstname, lastname, username, position,password,password1))
    submitbtn3.place(x = 200, y = 350, width = 70)

    submitbtn2 = tk.Button(root, text ="exit",bg ='blue', fg = 'white',command= lambda: exit(root))
    submitbtn2.place(x = 300, y = 350, width = 65)

    submitbtn1 = tk.Button(root, text ="login",fg = 'blue',command= lambda: switch1(root))
    submitbtn1.place(x = 300, y = 400, width = 100)
    
    root.mainloop()  


#login()    


#create product

def addProduct(): 
    root = tk.Tk()
    root.geometry("1500x1000")
    root.title("Clutch Center Motor Spares")
    
    lblsecrow = tk.Label(root, text ="CLutch Center Registry", fg = 'blue',)
    lblsecrow.place(x = 170, y = 10)
    # Defining the first row
    lblfrstrow = tk.Label(root, text ="Product id:", fg = 'blue', )
    lblfrstrow.place(x = 120, y = 50)
    productId = tk.Entry(root, width = 35)
    productId.place(x = 250, y = 50, width = 150)

    lblsecrow = tk.Label(root, text ="Product Name:", fg = 'blue', )
    lblsecrow.place(x = 120, y = 100)
    ProductName = tk.Entry(root, width = 35)
    ProductName.place(x = 250, y = 100, width = 150)

    lblrow6 = tk.Label(root, text ="Product Cartegory", fg = 'blue',)
    lblrow6.place(x = 120, y = 150)
    ProductCartegory = tk.Entry(root, width = 35)
    ProductCartegory.place(x = 250, y = 150, width = 150)

    lblrow3 = tk.Label(root, text ="Product Description", fg = 'blue',)
    lblrow3.place(x = 120, y = 200)
    ProductDescription = tk.Entry(root, width = 35)
    ProductDescription.place(x = 250, y = 200, width = 150)

    lblrow4 = tk.Label(root, text ="Product Price", fg = 'blue',)
    lblrow4.place(x = 120, y = 250)
    ProductPrice = tk.Entry(root, width = 35)
    ProductPrice.place(x = 250, y = 250, width = 150)

    lblrow5 = tk.Label(root, text ="Option:", fg = 'blue',)
    lblrow5.place(x = 120, y = 300)
    password1 = tk.Entry(root, width = 35)
    password1.place(x = 250, y = 300, width = 150)


    # listbox = Listbox(root, bg, fg, bd, height, width, font, ..)
    productlist = Listbox(root, fg = 'blue',)
    productlist.place(x = 550, y = 10, width = 1000, height = 1000)

    scrollbar = Scrollbar(root)
    for values in range(100):
        productlist.insert(END, values)
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

    submitbtn3 = tk.Button(root, text ="Register",bg ='blue', fg = 'white',command = lambda: registerCommit(root,firstname, lastname, username, position,password,password1))
    submitbtn3.place(x = 200, y = 350, width = 70)

    submitbtn2 = tk.Button(root, text ="exit",bg ='blue', fg = 'white',command= lambda: exit(root))
    submitbtn2.place(x = 300, y = 350, width = 65)

    submitbtn1 = tk.Button(root, text ="login",fg = 'blue',command= lambda: switch1(root))
    submitbtn1.place(x = 300, y = 400, width = 100)
    


    root.mainloop()  

addProduct()