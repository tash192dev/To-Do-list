#daily task checklist

import tkinter
from tkinter import *
from tkinter import messagebox


#-------------Boilerplate starter stuff----------------------#
tk = tkinter
main = Tk()  # Name of main window
main.title("Task Checklist ")  # Title
main.geometry("455x300")  # Size of the window in pixels
main.configure(bg="white")  # Background colour
main.resizable(True, True) #Window can be resized

radio_stringvar = tk.StringVar
drop_stringvar = tk.StringVar
selected_event = tkinter.StringVar()


#----------------Frames--------------#
entry_frame = LabelFrame(main, text = "Entry")
entry_frame.grid(row = 0, column= 0, sticky = NW )

checklist_frame = LabelFrame(main, text = "Checklist")
checklist_frame.grid(row = 0, column= 1)

#------------------Entry stuff----------------#
my_entry = tk.Entry(entry_frame)
my_entry.grid(row = 0,column = 0)
#-----------------------Listbox--------------#
listbox_list = ["Deez", "Nuts", "something", "another thing", "nice"]

var = tk.Variable(value = listbox_list)

list_box = tk.Listbox(main, listvariable = var, selectmode = tk.MULTIPLE)

list_box.grid(row = 1, column = 1)
#-----------------------Logic--------------#

def select_item(event):
    selected_item = list_box.curselection()

    print(selected_item)

n = 0

list_box.bind('<<ListboxSelect>>', select_item)

def add_something():
    global listbox_list
    item = my_entry.get()
    list_box.insert(END, item)
    print(listbox_list)

def testing():  
    global n
    my_var = my_entry.get()
    tk.Radiobutton(checklist_frame, text = my_var).grid(row = n, column= 0)
    n += 1
    
def delete_item():

    selected_item = list(list_box.curselection())
    print(selected_item)
    for index in range(len(selected_item)):
        list_box.delete(selected_item[index])


subjects = ["115", "121", "140", "111"]
# tk.Label(entry_frame, text="testing stuff").grid()

tk.Button(entry_frame, text = "Add", command = add_something).grid(row = 0,column = 1)
# drop_stringvar.set(subjects[0])
delete_button = tk.Button(entry_frame,text =  "Delete", command= delete_item).grid(row = 1, column= 1)


# tkinter.OptionMenu(main, drop_stringvar, "something", *subjects).pack()
# event_name_list_dropdown = tkinter.OptionMenu(master = main, variable = drop_stringvar, value = "This is VALUE", *subjects,)

tk.mainloop()
