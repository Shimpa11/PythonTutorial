
import session23demo
from  session23demo import *



def register():
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x300")
    username=StringVar()
    password=StringVar()
    Label(screen1,text="username * ").pack()
    Entry(screen1,textVariable=username)
    Label(screen1,text="password * ").pack()
    Entry(screen1,textVariable=password)


def login():
    print("login session started")
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x300")
    screen.title("Welcome")
    label1=Label(screen,text="Welcome to tkinter",bg ="white",font=("arial",16,"bold")).pack()
    Button(text="Login", height="2",width="30",command=login).pack()

    Button(text="Register",height="2",width="30",command=register).pack()
    screen.mainloop()
main_screen()

