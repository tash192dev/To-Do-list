#daily task checklist

import tkinter
from tkinter import *
from tkinter import messagebox
#--------------ToDo-------------------#
#Add scroll bar to listbox
#Sort out frames and other geometry stuff 
#Colours/fonts all that jazz    
#Compile to .exe ?
# 



#-------------Boilerplate starter stuff----------------------#
tk = tkinter
main = Tk()  # Name of main window
main.title("Task Checklist ")  # Title
main.geometry("455x300")  # Size of the window in pixels
main.configure(bg="grey")  # Background colour
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
listbox_list = ["a", "b", "c", "d", "e"]
var = tk.Variable(value = listbox_list)
list_box = tk.Listbox(main, listvariable = var, selectmode = tk.MULTIPLE)
list_box.grid(row = 1, column = 1)
#-----------------------Logic--------------#

def select_item(event):
    selected_item = list_box.curselection()

    print(selected_item)

n = 0

list_box.bind('<<ListboxSelect>>', select_item)
#this function adds the text from the text entry box as an element in the listbox
#checks if the text is empty
def add_something():
    global listbox_list
    item = my_entry.get()
    #Input validation
    if (item in listbox_list) or (item == ""):
        messagebox.showerror("Entry Error", "Entery is duplicate or empty")
        return
    
    list_box.insert(END, item)
    #adding the item to listbox_list so I can use it for input validation
    listbox_list.append(item)
    print(listbox_list)
    
# this is a function that adds a radio button in a sort of list 
#not using this anymore because found ListBox 

def testing():  
    global n
    my_var = my_entry.get()
    tk.Radiobutton(checklist_frame, text = my_var).grid(row = n, column= 0)
    n += 1

# this function is the command for the delete button
# it uses the indicies of all selected items in the listbox with the    
# curselection method. 
# currently is buggy 
def delete_item():

    selected_item = list(list_box.curselection())
    print(selected_item)
    for index in range(len(selected_item)):
        list_box.delete(selected_item[index])


# tk.Label(entry_frame, text="testing stuff").grid()

tk.Button(entry_frame, text = "Add", command = add_something).grid(row = 0,column = 1)
# drop_stringvar.set(subjects[0])
delete_button = tk.Button(entry_frame,text =  "Delete", command= delete_item).grid(row = 1, column= 1)


# tkinter.OptionMenu(main, drop_stringvar, "something", *subjects).pack()
# event_name_list_dropdown = tkinter.OptionMenu(master = main, variable = drop_stringvar, value = "This is VALUE", *subjects,)

tk.mainloop()
