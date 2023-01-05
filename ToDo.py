# This program is a simple to do list task where you can input tasks to add to the list and then select tasks which are done to delte them from the list
# Talha Ashraf
# tash.dev@proton.me

import tkinter
from tkinter import *
from tkinter import messagebox
#--------------ToDo-------------------#
#Add scroll bar to listbox
#Sort out frames and other geometry stuff 
#Colours/fonts all that jazz    
#Compile to .exe ?
#link to external database ?????????????


#-------------Boilerplate starter stuff----------------------#
tk = tkinter
main = Tk()  # Name of main window
main.title("Task Checklist ")  # Title
main.geometry("455x300")  # Size of the window in pixels
main.configure(bg="grey")  # Background colour
main.resizable(True, True) #Window can be resized

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
    selected_indecies = list_box.curselection()

    print(selected_indecies)

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
    
# this function is the command for the delete button
# it uses the indicies of all selected items in the listbox with the    
# curselection method. 
# 

def delete_item():
    global listbox_list
    print(listbox_list)
    #contains a reversed list of the currently selected indecies 
    selected_indecies = list(reversed(list_box.curselection()))
    print(selected_indecies)
    for i in range(len(selected_indecies)):
        list_index = selected_indecies[i]
        #removing element from the listbox
        list_box.delete(list_index)
        #removing the string from the listbox_list so that input validation doesnt catch removed strings
        #debugging statement
        # print(listbox_list.pop(selected_indecies[index]))
        listbox_list.pop(list_index)
        print(listbox_list)



tk.Button(entry_frame, text = "Add", command = add_something).grid(row = 0,column = 1)

delete_button = tk.Button(entry_frame,text =  "Delete", command= delete_item).grid(row = 1, column= 1)

tk.mainloop()
