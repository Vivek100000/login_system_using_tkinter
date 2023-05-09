from tkinter import *
import os

def main_menu():
	global main_window 
	main_window = Tk()
	main_window.geometry("300x300")
	main_window.title("login system")
	label1 = Label(main_window,text="choose an option",bg="grey",fg="blue")
	label1.pack(fill=X,pady=20)
	login_btn = Button(main_window,text="login",width="30",height="2",command=login)
	login_btn.pack(pady=20)
	register_btn = Button(main_window,text="New User",width="30",height="2",command=new_user)
	register_btn.pack(pady=20)
	main_window.mainloop()
def new_user():
    global new_user_window
    new_user_window = Toplevel(main_window)
    new_user_window.title("new_user")
    new_user_window.geometry("300x300")
    global username 
    username = StringVar()
    global password
    password = StringVar()
    global fullname
    fullname = StringVar()
    label1 = Label(new_user_window,text="please fill the info below",bg="white",fg="blue")
    label1.pack(fill=X,pady=20)
   
    
    user_info_panel = Frame(new_user_window)
    user_info_panel.pack(pady=20)
    username_label = Label(user_info_panel,text="Username: ")
    username_label.grid(row=0,column=0)
    global username_entry
    username_entry = Entry(user_info_panel,textvariable=username)
    username_entry.grid(row=0,column=1)
    
    Label(user_info_panel,text="").grid(row=1)
    
    password_label = Label(user_info_panel,text="Password: ")
    password_label.grid(row=2,column=0)
    global password_entry
    password_entry = Entry(user_info_panel,textvariable=password)
    password_entry.grid(row=2,column=1)
    Label(user_info_panel,text="").grid(row=3)
    fullname_label = Label(user_info_panel,text="Fullname: ")
    fullname_label.grid(row=4,column=0)
    global fullname_entry
    fullname_entry = Entry(user_info_panel,textvariable=fullname)
    fullname_entry.grid(row=4,column=1)
    
    reg_btn = Button(new_user_window,text="Register",command = register)
    reg_btn.pack(pady=20)

def register():
    registered = False
    username_text = username.get();
    password_text = password.get();
    fullname_text = fullname.get();
    file = open("credentials.txt","a")
    for line in open("credentials.txt","r").readlines():
         login_info = line.split()
         if(len(login_info)!=0 and login_info[1] == username_text):
             registered = True
    if registered:
        file.close()
        fullname_entry.delete(0,END)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        failure = Toplevel(new_user_window)
        failure.geometry("200x200")
        failure.title("Success")
        Label(failure,text="username already exist!!",bg="white",fg="red").pack(fill=X,pady=20)
        Button(failure,text="Try Again",command = lambda:failure.destroy()).pack(pady=20)
    else:
        file.write("Username: "+username_text+" password: "+password_text+" Name: "+fullname_text+"\n")
        file.close()
        fullname_entry.delete(0,END)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        success = Toplevel(new_user_window)
        success.geometry("200x200")
        success.title("Success")
        Label(success,text="successful registration!!",bg="white",fg="green").pack(fill=X,pady=20)
        Button(success,text="ok",command = lambda:success.destroy()).pack(pady=20)
def login():
        global login_window
        global l_username
        l_username = StringVar()
        global l_password
        l_password = StringVar()
        login_window = Toplevel(main_window)
        login_panel = Frame(login_window)
        login_panel.pack(pady=20)
        Label(login_panel,text="Username: ",bg="white",fg="black").grid(row=0,column=0)
        global login_username_entry
        login_username_entry=Entry(login_panel,textvariable=l_username)
        login_username_entry.grid(row=0,column=1)
        Label(login_panel,text="").grid(row=1)
        Label(login_panel,text="Password: ",bg="white",fg="black").grid(row=2,column=0)
        global login_password_entry
        login_password_entry=Entry(login_panel,textvariable=l_password)
        login_password_entry.grid(row=2,column=1)
        Label(login_panel,text="").grid(row=3)
        Button(login_window,text="Next",command=next).pack(pady=20)
def next():
        person_exist = False
        for line in open("credentials.txt","r").readlines():
             login_values = line.split()
             if(login_values[1] == l_username.get() and login_values[3] == l_password.get()):
                  person_exist = True
        if person_exist:
             login_username_entry.delete(0,END)
             login_password_entry.delete(0,END)
             succesful_login = Toplevel(login_window)
             succesful_login.geometry("200x200")
             succesful_login.title("succesful login")
             Label(succesful_login,text="successfully logged in!!!",bg="white",fg="green").pack(fill=X,pady=20)
             Button(succesful_login,text="OK",command = lambda:succesful_login.destroy()).pack(pady=20)
        else:
             login_username_entry.delete(0,END)
             login_password_entry.delete(0,END)
             failed_login = Toplevel(login_window)
             failed_login.geometry("200x200")
             failed_login.title("failed login")
             Label(failed_login,text="failed to login!!!",bg="white",fg="red").pack(fill=X,pady=20)
             Button(failed_login,text="OK",command = lambda:failed_login.destroy()).pack(pady=20)
main_menu()
	