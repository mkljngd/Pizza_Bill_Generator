from tkinter import *
import sqlite3


def ClearScreen(master):
    masterList=master.winfo_children()
    for e in masterList:
        e.destroy()

def Back(master,func):
    ClearScreen(master)
    func(master)


def ForgotPage(master):
    ClearScreen(master)
    titleLabel = Label(root, text="                      Forgot Password", font=("Monotype Corsiva", 50))
    nameLabel = Label(root, text="Name", font=("Times New Roman", 32))
    nameEntry = Entry(root, font=("Times New Roman", 32))
    nameEntry.config(width=30)
    emailLabel = Label(root, text="Email ID     ", font=("Times New Roman", 32))
    emailEntry = Entry(root, font=("Times New Roman", 32))
    emailEntry.config(width=30)
    mobileLabel = Label(root, text="Mobile Number               ", font=("Times New Roman", 32))
    mobileEntry = Entry(root, font=("Times New ", 32))
    mobileEntry.config(width=30)
    passwordLabel = Label(root, text="Password             ", font=("Times New Roman", 32))
    passwordEntry = Entry(root, font=("Times New Roman", 32), show="*")
    passwordEntry.config(width=30)
    passwordLabel1 = Label(root, text="Confirm Password     ", font=("Times New Roman", 32))
    passwordEntry1 = Entry(root, font=("Times New Roman", 32), show="*")
    passwordEntry1.config(width=30)
    blankLabel = Label(text=" ", font=("Times New Roman", 72))
    messageLabel = Label(root, text="", font=("Times New Roman", 32))
    def Clear():
        nameEntry.delete(0, 'end')
        emailEntry.delete(0, 'end')
        mobileEntry.delete(0, 'end')
        addressEntry.delete("1.0",END)
    def FillDetails():
        name=nameEntry.get()
        mobile=mobileEntry.get()
        email = emailEntry.get()
        password = passwordEntry.get()
        password1 = passwordEntry1.get()

        if (password != password1):
            messageLabel.config(text="Passwords Do Not Match",fg="red")
        if (email or not password or not password1):
                messageLabel.config(text="Please Fill All The Fields",fg="red")
        else:
                with sqlite3.connect("database1.db") as db:
                    cursor = db.cursor()
                w = '''UPDATE users set password = ? where email = ? '''
                cursor.execute(w, [(password), (email)])
                db.commit()
    clearButton = Button(root, text="Clear", font=("Times New Roman", 30), command=Clear)
    submitButton = Button(root, text="Submit", font=("Times New Roman", 30), command=FillDetails)
    backButton = Button(root, text="Back", font=("Times New Roman", 30), command=lambda: Back(master, LoginPage))
    titleLabel.grid(sticky=W+E+N+S,columnspan=3)
    nameLabel.grid(row=1, column=0, sticky=W)
    nameEntry.grid(row=1, column=1, sticky=W + E + N + S)
    emailLabel.grid(row=2, column=0, sticky=W)
    emailEntry.grid(row=2, column=1, sticky=W + E + N + S)
    mobileLabel.grid(row=3, column=0, sticky=W)
    mobileEntry.grid(row=3, column=1, sticky=W + E + N + S)
    blankLabel.grid(row=4, column=0, sticky=W+E+N+S,columnspan=3)
    backButton.grid(row=5, column=0, sticky=W+E+N+S)
    submitButton.grid(row=5, column=1, sticky=W+E+N+S)
    clearButton.grid(row=5, column=2, sticky=W+E+N+S)
    messageLabel.grid(row=6,columnspan=2,sticky=W+E+N+S)


def RegisterPage(master):
    ClearScreen(master)
    titleLabel = Label(root, text="                         Register", font=("Monotype Corsiva", 50))
    nameLabel = Label(root, text="Name      ", font=("Times New Roman", 32))
    nameEntry = Entry(root, font=("Times New Roman", 32))
    nameEntry.config(width=30)
    emailLabel = Label(root, text="Email ID", font=("Times New Roman", 32))
    emailEntry = Entry(root, font=("Times New Roman", 32))
    emailEntry.config(width=30)
    mobileLabel = Label(root, text="Mobile Number       ", font=("Times New Roman", 32))
    mobileEntry = Entry(root, font=("Times New ", 30))
    mobileEntry.config(width=30)
    addressLabel = Label(root, text="Address        ", font=("Times New Roman", 32))
    addressEntry = Text(root,height=5,width=30, font=("Times New Roman", 32))
    passwordLabel = Label(root, text="Password", font=("Times New Roman", 32))
    passwordEntry = Entry(root, font=("Times New Roman", 32),show="*")
    passwordEntry.config(width=30)
    passwordLabel1 = Label(root, text="Confirm Password     ", font=("Times New Roman", 32))
    passwordEntry1 = Entry(root, font=("Times New Roman", 32),show="*")
    passwordEntry1.config(width=30)
    messageLabel=Label(root,text="",font=("Times New Roman", 32))
    def Register():
        name=nameEntry.get()
        email = emailEntry.get()
        mobile = mobileEntry.get()
        address= addressEntry.get("1.0",END)
        address = address[:-1]
        password=passwordEntry.get()
        password1=passwordEntry1.get()
        if mobile.isdigit()==False:
            messageLabel.config(text="Invalid Mobile Number",fg="red")
        elif(password!=password1):
            messageLabel.config(text="Passwords Do Not Match",fg="red")
        elif(not name or not email or not mobile or not address or not password or not password1 ):
            messageLabel.config(text="Please Fill All The Fields")
        else:
            with sqlite3.connect("database1.db") as db:
                cursor = db.cursor()
            z = '''INSERT INTO users(name,email,mobile,address,password)
                          VALUES(?,?,?,?,?)'''
            cursor.execute(z, [(name), (email), (mobile), (address), (password)])
            db.commit()
            #f = open("data.txt", "a+")
            #data=name+"\t"+email+"\t"+mobile+"\t"+address+"\t"+password
            #f.write(data+"\n")
        Clear()
    def Clear():
        nameEntry.delete(0, 'end')
        emailEntry.delete(0, 'end')
        mobileEntry.delete(0, 'end')
        addressEntry.delete("1.0",END)
        passwordEntry.delete(0, 'end')
        passwordEntry1.delete(0, 'end')
    clearButton=Button(root,text="Clear",font=("Times New Roman", 30),command=Clear)
    submitButton=Button(root,text="Submit",font=("Times New Roman", 30),command=Register)
    backButton = Button(root, text="Back", font=("Times New Roman", 30),command=lambda:Back(master,LoginPage))
    titleLabel.grid(sticky=W+E+N+S,columnspan=2)
    nameLabel.grid(row=1,column=0,sticky=W)
    nameEntry.grid(row=1,column=1,sticky=E)
    emailLabel.grid(row=2, column=0,sticky=W)
    emailEntry.grid(row=2, column=1, sticky=E)
    mobileLabel.grid(row=3, column=0,sticky=W)
    mobileEntry.grid(row=3, column=1, sticky=E)
    addressLabel.grid(row=4, column=0,sticky=W)
    addressEntry.grid(row=4, column=1, sticky=E)
    passwordLabel.grid(row=5, column=0,sticky=W)
    passwordEntry.grid(row=5, column=1, sticky=E)
    passwordLabel1.grid(row=6, column=0,sticky=W)
    passwordEntry1.grid(row=6, column=1, sticky=E)
    messageLabel.grid(row=7,columnspan=3,sticky=W+E+N+S)
    backButton.grid(row=8,column=0,sticky=W)
    submitButton.grid(row=8, column=1, sticky=W)
    clearButton.grid(row=8,column=2,sticky=W,)


def LoginPage(master):
    blankLabel = Label(text=" ", font=("Times New Roman", 72))
    blankLabel1 = Label(text=" ", font=("Times New Roman", 72))
    titleLabel = Label(root, text="                         Title", font=("Monotype Corsiva", 72))
    emailLabel = Label(root, text="Email ID     ", font=("Times New Roman", 48))
    emailEntry = Entry(root, font=("Times New Roman", 48))
    passwordEntry = Entry(root, font=("Times New Roman", 48), show="*")
    passwordLabel = Label(root, text="Password      ", font=("Times New Roman", 48))
    messageLabel=Label(text="",fg="red",font=("Times New Roman", 48))
    def Login():
        email = emailEntry.get()
        password = passwordEntry.get()
        with sqlite3.connect("database1.db") as db:
            cursor = db.cursor()
        x = '''SELECT * FROM users WHERE email = ? AND password = ?'''
        cursor.execute(x, [(email), (password)])
        result = cursor.fetchall()
        if result:
            messageLabel.config(fg="green", text="Login Successful")
        else:
            messageLabel.config(fg="red", text="Incorrect Username/Password")
            timesleep(1)
    loginButton = Button(text="Login", font=("Times New Roman", 32),command=Login)
    registerButton = Button(text="Register", font=("Times New Roman", 32), command=lambda: RegisterPage(root))
    forgotButton = Button(text="Forgot Password", font=("Times New Roman", 32),command=lambda : ForgotPage(root))
    titleLabel.grid(row=0, column=0, columnspan=2)
    emailLabel.grid(row=2, column=0)
    emailEntry.grid(row=2, column=1, columnspan=2,sticky=E)
    blankLabel.grid(row=3, column=0)
    passwordLabel.grid(row=4, column=0)
    passwordEntry.grid(row=4, column=1, columnspan=2)
    blankLabel1.grid(row=5, column=0)
    messageLabel.grid(row=5,columnspan=3,sticky=W+E+N+S)
    loginButton.grid(row=6, column=0)
    registerButton.grid(row=6, column=1, sticky=W+E)
    forgotButton.grid(row=6, column=2, columnspan=2,sticky=E)
root=Tk()
LoginPage(root)
root.mainloop()