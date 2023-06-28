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
main.geometry("250x355")  # Size of the window in pixels
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

#-----------------------Listbox--------------#
try:
    #try to read the tasks file if it exists and put the contents into the listbox_list 
    with open("tasks.txt", "r") as file:
        listbox_list = file.read().splitlines()

except:
    #if the file cannot be read then create a file called tasks.txt
    with open("tasks.txt", "w") as file:
        file.write("")
    listbox_list = []

# listbox_list = []
var = tk.Variable(value = listbox_list)
list_box = tk.Listbox(checklist_frame, listvariable = var, selectmode = tk.MULTIPLE, width= widget_width, font=(10))
list_box.grid(row = 1, column = 1)

#-----------------------Logic--------------#

#this variable will be used by functions to track ammount of completed tasks
completed_tasks = len(listbox_list)

#This helper function will update how many tasks have been completed
def completed_updater(tasks):
    tasks_completed = tk.Label(completed_frame, text = 'Completed Tasks : ' + str(completed_tasks), width = button_width - 5, font = (10))
    tasks_completed.grid(row = 0, column = 2, columnspan = 2)
completed_updater(completed_tasks)
#this function command for the Add button. It adds the text from the text entry box as an element in the listbox
#checks if the text is empty and if the text is in the listbox_list if it is then it pops up a message box with an error 

def add_task(task):
    list_box.insert(END, task)
    #adding the item to listbox_list so I can use it for input validation
    listbox_list.append(task)

def add_button_function():
    global listbox_list
    input_text = (my_entry.get()).rstrip()
    #Input validation
    if (input_text in listbox_list) or (input_text == ""):
        messagebox.showerror("Entry Error", "Entry is duplicate or empty")
        return
    #inserts the text from the entry as an item at the end of listbox
    add_task(input_text)
    # print(listbox_list)
    my_entry.delete(0, END)
    my_entry.focus_set()
    
    #appending file with the new task
    with open("tasks.txt", "a") as file:
        file.write(input_text + "\n")

    

deleted_tasks = []
# this function is the command for the delete button
# it uses the indicies of all selected items in the listbox with the curselection method. 
def delete_item():
    global completed_tasks
    global listbox_list
    global deleted_tasks
    deleted_tasks = []
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
        deleted_tasks.append(listbox_list.pop(list_index))
    #putting how many tasks have been "completed" or deleted using this function
    
    completed_tasks += len(selected_indecies)
    completed_updater(completed_tasks)

    #overriting the file with the new listbox_list
    with open("tasks.txt", "w") as file:
        for i in range(len(listbox_list)):
            file.write(listbox_list[i] + "\n")


#this function reverses the last delete operation
#if only one task was deleted then it will only add that one task back
#if mutiple tasks were deleted then it will add all of them back
def undo():
    global deleted_tasks
    global completed_tasks
    if(len(deleted_tasks) != 0):
        completed_tasks -= len(deleted_tasks)
        completed_updater(completed_tasks)
        for i in range(len(deleted_tasks)):
            add_task(deleted_tasks[i])
        deleted_tasks = []
    with open("tasks.txt", "w") as file:
        for i in range(len(listbox_list)):
            file.write(listbox_list[i] + "\n")


#if the file does not exist then create a file called tasks.txt and write the listbox_list to it
# #if it already exists then read it in and put it in the listbox_list
# try:
#     with open("tasks.txt", "r") as file:
#         listbox_list = file.read().splitlines()

#         print(listbox_list)
#         for i in range(len(listbox_list)):
#             add_task(listbox_list[i])
#         print(listbox_list)
# except:
#     with open("tasks.txt", "w") as file:
#         for i in range(len(listbox_list)):
#             file.write(listbox_list[i] + "\n")
            
# # #this function is called when the window is closed. It writes the listbox_list to the file
# # def on_closing():
# #     with open("tasks.txt", "w") as file:
# #         for i in range(len(listbox_list)):
#             file.write(listbox_list[i] + "\n")
#     main.destroy()





#-------------Buttons------------------#
add_button = tk.Button(button_frame, text = "Add", command = add_button_function, width= button_width, font=(10))
add_button.grid(row = 0,column = 0)


#-----------Keyboard Navigation--------------#

#when the add button is focused we can press the "enter" key to press the add button
def on_focus_in(event):
    event.widget.bind('<Return>', lambda event: add_button.invoke())

def on_focus_out(event):
    event.widget.unbind('<Return>')


add_button.bind('<FocusIn>', on_focus_in)
add_button.bind('<FocusOut>', on_focus_out)

my_entry.bind('<FocusIn>', on_focus_in)
my_entry.bind('<FocusOut>', on_focus_out)


tk.Button(delete_frame,text =  "Done", command= delete_item, width= button_width, font=(10)).grid(row = 0, column= 1)
tk.Button(completed_frame, text = "  Undo  ", command = undo).grid(row = 0, column = 0)
tk.mainloop()
