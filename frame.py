from tkinter import *
import requests

number = None

def raise_frame(frame):
    frame.tkraise()

def number_e():
    global number
    num = number.get()
    number.set(num)
    para={'action': 'saveUserData', 'MOB': num, 'MCID': '002000244', 'BTNO': '10'}
    r=requests.post("http://clickcash.in/apisave/apiDataSavever2.php", data=para)
    print(r.text)
    raise_frame(PageTwo)

def loop():
    inp = input("Enter your answer: ")
    if inp == 'y':
         raise_frame(PageOne)
    else:
        pass
    root.after(500, loop)

root = Tk()
root.geometry('300x300')

Home = Frame(root)
PageOne = Frame(root)
PageTwo = Frame(root)

for frame in (Home, PageOne, PageTwo):
    frame.grid(row=0, column=0, sticky='news')

number = IntVar()

Label(Home, text='Home').pack()
#Button(Home, text='Go to Page1', command=lambda:raise_frame(PageOne)).pack()

Label(PageOne, text='Enter the number').grid(row=0, column=0, padx=5, pady=5)
Entry(PageOne, textvariable=number, width=30).grid(row=0, column=1, padx=2, pady=2)
Button(PageOne, text='Test', command=number_e).grid(row=1, column=2, padx=40, pady=40)

Label(PageTwo, text='Test Successful').pack()
Button(PageTwo, text='Goto Home', command=lambda:raise_frame(Home)).pack()

root.after(500, loop)
raise_frame(Home)
root.mainloop()
