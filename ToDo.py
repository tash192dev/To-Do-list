# This program is a simple to do list task where you can input tasks to add to the list and then select tasks which are done to delte them from the list
# Talha Ashraf
# tash.dev@proton.me

import tkinter
from tkinter import *
from tkinter import messagebox

#--------------ToDo-------------------#
#Add scroll bar to listbox - decided not to add because just looks celeaner without it
#Sort out frames and other geometry stuff  
#Colours/fonts all that jazz    
#Compile to .exe ?
#link to external database ?????????????
#-------------Boilerplate starter stuff----------------------#
tk = tkinter
main = Tk()  # Name of main window
main.title("To Do")  # Title
main.geometry("250x352")  # Size of the window in pixels
main.configure(bg="pink")  # Background colour
main.resizable(True, True) #Window can be resized

#----------------Frames--------------#
entry_frame = LabelFrame(main, text = "Enter Task")
entry_frame.grid(row = 0, column= 0 )

button_frame = LabelFrame(main)
button_frame.grid(row= 1, column= 0)


checklist_frame = LabelFrame(main, text = "List")
checklist_frame.grid(row = 2, column= 0)


delete_frame = LabelFrame(main)
delete_frame.grid(row=3, column=0)

completed_frame = LabelFrame(main)
completed_frame.grid(row = 4, column = 0)
#------------------Entry stuff----------------#
widget_width = 27
button_width = 26

my_entry = tk.Entry(entry_frame, width=widget_width, font=(10))
my_entry.grid(row = 0,column = 0)

tasks_completed = tk.Label(completed_frame, text = 'Completed Tasks : ', width = button_width, font = (10))
tasks_completed.grid(row = 0, column = 0)
#-----------------------Listbox--------------#

# listbox_list = ["a", "b", "c", "d", "e"]
listbox_list = []
var = tk.Variable(value = listbox_list)
list_box = tk.Listbox(checklist_frame, listvariable = var, selectmode = tk.MULTIPLE, width= widget_width, font=(10))
list_box.grid(row = 1, column = 1)

#-----------------------Logic--------------#

def select_item(event):
    selected_indecies = list_box.curselection()

    # print(selected_indecies)

list_box.bind('<<ListboxSelect>>', select_item)

#this function command for the Add button. It adds the text from the text entry box as an element in the listbox
#checks if the text is empty and if the text is in the listbox_list if it is then it pops up a message box with an error 
def add_something():
    global listbox_list
    input_text = (my_entry.get()).rstrip()
    #Input validation
    if (input_text in listbox_list) or (input_text == ""):
        messagebox.showerror("Entry Error", "Entery is duplicate or empty")
        return
    #inserts the text from the entry as an item at the end of listbox
    list_box.insert(END, input_text)
    #adding the item to listbox_list so I can use it for input validation
    listbox_list.append(input_text)
    # print(listbox_list)
    my_entry.delete(0, END)
    my_entry.focus_set()
    
completed_tasks = 0    
# this function is the command for the delete button
# it uses the indicies of all selected items in the listbox with the curselection method. 
def delete_item():
    global completed_tasks
    global listbox_list
    # print(listbox_list)
    #contains a reversed list of the currently selected indecies 
    selected_indecies = list(reversed(list_box.curselection()))
    # print(selected_indecies)
    for i in range(len(selected_indecies)):
        list_index = selected_indecies[i]
        #removing element from the listbox
        list_box.delete(list_index)
        #removing the string from the listbox_list so that input validation doesnt catch removed strings
        #debugging statement
        # print(listbox_list.pop(selected_indecies[index]))
        listbox_list.pop(list_index)
        # print(listbox_list)
    completed_tasks += 1
    tasks_completed = tk.Label(completed_frame, text = 'Completed Tasks : ' + str(completed_tasks), width = button_width, font = (10))
    tasks_completed.grid(row = 0, column = 0)





#-------------Buttons------------------#
add_button = tk.Button(button_frame, text = "Add", command = add_something, width= button_width, font=(10))
add_button.grid(row = 0,column = 0)


#-----------Keyboard Stuff--------------#

#when the add button is focused we can press the "enter" key to add it
def on_focus_in(event):
    event.widget.bind('<Return>', lambda event: add_button.invoke())

def on_focus_out(event):
    event.widget.unbind('<Return>')


add_button.bind('<FocusIn>', on_focus_in)
add_button.bind('<FocusOut>', on_focus_out)

my_entry.bind('<FocusIn>', on_focus_in)
my_entry.bind('<FocusOut>', on_focus_out)


tk.Button(delete_frame,text =  "Delete", command= delete_item, width= button_width, font=(10)).grid(row = 0, column= 1)

tk.mainloop()
