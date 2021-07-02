from tkinter import *

App = Tk()

App.title('Length converter')
scale = ['Meter','inch','foot']
App.geometry('350x150')

var = StringVar()
drop_1 = OptionMenu(App,var,*scale)
drop_1.grid(row=0,column=0,pady=5)

lbl = Label(App, text='Conveter to')
lbl.grid(row=0,column = 1,pady=5)

var1 = StringVar()
drop_2 = OptionMenu(App,var1,*scale)
drop_2.grid(row=0,column=2,pady=5)

txt = Label(App,text='Enter a number')
txt.grid(row=1,column=0,columnspan=2,pady=5)

entry = Entry(App)
entry.grid(row=1,column=2,columnspan=2,pady=5)

def converter():

    entry_1 = var.get()
    entry_2 = var1.get()
    num = int(entry.get())

    if entry_1 == 'Meter' and entry_2 == 'inch':
        conv_num = num*39.37
    elif entry_1 == 'Meter' and entry_2 == 'foot':
        conv_num = num*3.28
    elif entry_1 == 'foot' and entry_2 == 'inch':
        conv_num = num*12
    elif entry_1 == 'foot' and entry_2 == 'Meter':
        conv_num = num/3.28
    elif entry_1 == 'inch' and entry_2 == 'Meter':
        conv_num = num/39.37
    elif entry_1 == 'inch' and entry_2 == 'foot':
        conv_num = num/12
    else:
        conv_num = num

    conv_numL = Label(App, text=round(conv_num, 2), width=10)
    conv_numL.grid(row=1, column=4, pady=5)

button = Button(App,text='Convert',command = converter)
button.grid(row=3,column=0)




App.mainloop()
