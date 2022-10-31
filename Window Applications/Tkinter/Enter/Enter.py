from tkinter import *
from tkinter import messagebox
import sys
from Enter_text import *

root=Tk()
root.resizable(width=False,height=False)
root.geometry('400x230')
root.title('Enter')

root['bg']='#ccc'

def Login_cheker(string, valid, flag=False):
    for i in string:
        if i in valid:
            flag = True
            break

    return flag


def Password_cheker(string, valid, flag=True, maxi=8):
    if len(string) >= maxi:
        for j in string:
            if j in valid:
                flag = False
    else:
        flag = False

    return flag


def init_child():
    l = login.get()
    p = password.get()
    if (Login_cheker(l, login_words) is True) and (Password_cheker(p, password_no_words) is True):
        return messagebox.showinfo('Congratulations', congratulations)

    elif (Login_cheker(l, login_words) is False) and (Password_cheker(p, password_no_words) is True):
        return messagebox.showerror('Incorrectly entered login', no_login)

    elif (Login_cheker(l, login_words) is True) and (Password_cheker(p, password_no_words) is False):
        return messagebox.showerror('Incorrectly entered password', no_password)
    else:
        return messagebox.showerror('Incorrectly entered login and password',
                                    no_login_password)
def btn_exit():
    sys.exit()


text_login=Label(text='Login',font='Consolas 25',fg='#2e2525',bg='#ccc')
login=Entry(root,font='Consolas 20',fg='#5100ff',bg='#f00'
            ,relief='solid',justify='center')

text_password=Label(text='Password',font='Consolas 25',fg='#2e2525',bg='#ccc')
password=Entry(root,font='Consolas 20',fg='#5100ff',bg='#f00',
               relief='solid',justify='center',show='$')


enter = Button(text='Enter',font='Consolas 15',fg='#2e2525',bg='#ccc',
               relief='solid',justify='center',command=init_child)

exit = Button(text='Exit',font='Consolas 15',fg='#2e2525',bg='#ccc',
              relief='solid',justify='center', command=btn_exit)

text_login.pack()
login.pack()

text_password.pack()
password.pack()


enter.place(relx=0.32, rely=0.75)
exit.place(relx=0.53, rely=0.75)


root.mainloop()
