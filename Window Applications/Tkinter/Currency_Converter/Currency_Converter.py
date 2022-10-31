from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from bs4 import BeautifulSoup
import requests
import copy

# BeautifulSoup
url = 'https://finance.i.ua/bank/115/'

r = requests.get(url=url)

soup = BeautifulSoup(r.text, 'lxml')

currency = soup.find_all('span', class_='value')

# tkinter

# window
window = Tk()
window.resizable(height=False, width=False)
window.geometry('500x150')
window.title('Currency converter')

# constants
dict_buy = {
    'Dollar': float(currency[1].text[:7]),
    'Euro': float(currency[3].text[:7]),
    'Hryvnia': 1,
}

dict_sell = {
    'Dollar': float(currency[2].text[:7]),
    'Euro': float(currency[0].text[:7]),
    'Hryvnia': 1,
}

list_currency = ['Dollar', "Euro", "Hryvnia"]

list_course = ['Buy', "Sell"]

list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# functions
def check_request():
    if str(combobox_request.get()) == 'Sell':
        return dict_sell
    elif str(combobox_request.get()) == 'Buy':
        return dict_buy


def check_combobox(vf):
    global result
    try:
        if str(entry1.focus_get()) == '.!entry2' \
                or str(entry1.focus_get()) == '.!combobox2':
            result = check_request()[combobox_currency1.get()] \
                     / check_request()[combobox_currency2.get()] * float(
                vf.get())
        elif str(entry1.focus_get()) == '.!entry' \
                or str(entry1.focus_get()) == '.!combobox' \
                or str(entry1.focus_get()) == '.!combobox3'\
                or combobox_currency1.winfo_x() == 200:
            result = check_request()[combobox_currency2.get()] \
                     / check_request()[combobox_currency1.get()] * float(
                vf.get())
    except ValueError:
        vf.delete(0, END)
    return str(round(result, 3))


def check_entry():
    try:
        if str(entry1.focus_get()) == '.!entry2' \
                or str(entry1.focus_get()) == '.!combobox' \
                and entry1.get() != check_combobox(entry2):

            entry1.delete(0, END)
            entry1.insert(0, check_combobox(entry2))

        elif str(entry1.focus_get()) == '.!entry' \
                or str(entry1.focus_get()) == '.!combobox2' \
                or str(entry1.focus_get()) == '.!combobox3' \
                and entry2.get() != check_combobox(entry1):

            entry2.delete(0, END)
            entry2.insert(0, check_combobox(entry1))

    except KeyError:
        pass



def swap_combobox():
    x1 = combobox_currency1.winfo_x()
    x2 = combobox_currency2.winfo_x()

    combobox_currency1.place_configure(x=x2)
    combobox_currency2.place_configure(x=x1)



def sorting_combobox():
    global list_currency
    a=copy.copy(list_currency)
    b = copy.copy(list_currency)
    a.remove(combobox_currency2.get())
    b.remove(combobox_currency1.get())
    combobox_currency1.configure(values=a)
    combobox_currency2.configure(values=b)

def clear_widget(widget):
    widget.destroy()
# design
# combobox
combobox_currency1 = ttk.Combobox(window, values=list_currency,
                                  state="readonly")
combobox_currency1.current(0)
combobox_currency1.place(x=50, y=50)
combobox_currency2 = ttk.Combobox(window, values=list_currency,
                                  state="readonly")
combobox_currency2.current(1)
combobox_currency2.place(x=300, y=50)

combobox_request = ttk.Combobox(window, values=list_course, state="readonly")
combobox_request.current(0)
combobox_request.place(x=180, y=10)

# entry
entry1 = Entry()
entry1.insert(0, '1')
entry1.focus_set()
entry1.place(x=50, y=90, width=143)

entry2 = Entry()
entry2.place(x=300, y=90, width=143)

# button
photo = ImageTk.PhotoImage(file="change.png")

btn_change = Button(text='change', command=swap_combobox, image=photo)
btn_change.place(x=217, y=50)



def loop():
    check_entry()
    sorting_combobox()
    window.after(500, loop)


if __name__ == "__main__":
    window.after(500, loop)
    window.mainloop()
