# This program is a simple to do list task where you can input tasks to add to the list and then select tasks which are done to delte them from the list
# Talha Ashraf
# tash.dev@proton.me

import tkinter
from tkinter import *
from tkinter import messagebox

#-------------Starter code----------------------#
tk = tkinter
main = Tk()  # Name of main window
main.title("To Do")  # Title
main.geometry("245x380")  # Size of the window in pixels
main.configure(bg="white")  # Background colour
main.resizable(True, True) #Window can be resized

#----------------Frames--------------#
entry_frame = tk.LabelFrame(main, text="Enter Task")
entry_frame.grid(row=0, column=0, sticky="nsew")

add_button_frame = tk.LabelFrame(main)
add_button_frame.grid(row=1, column=0, sticky="nsew")

checklist_frame = tk.LabelFrame(main, text="List")
checklist_frame.grid(row=2, column=0, sticky="nsew")

done_button_frame = tk.LabelFrame(main)
done_button_frame.grid(row=3, column=0, sticky="nsew")

completed_tasks_counter_frame = tk.LabelFrame(main)
completed_tasks_counter_frame.grid(row=4, column=0, sticky="nsew")

undo_frame = tk.LabelFrame(main)
undo_frame.grid(row=5, column=0, sticky="nsew")

#------------------Dynamic sizing----------------#
Grid.rowconfigure(main, 0, weight=1)
Grid.rowconfigure(main, 1, weight=1)
Grid.rowconfigure(main, 2, weight=1)
Grid.rowconfigure(main, 3, weight=1)
Grid.rowconfigure(main, 4, weight=1)
Grid.rowconfigure(main, 5, weight=1)
Grid.columnconfigure(main, 0, weight = 1)

Grid.rowconfigure(entry_frame, 0, weight=1)
Grid.columnconfigure(entry_frame, 0, weight = 1)

# entry_frame.grid_propagate(False)

#------------------Entry widgets----------------#
widget_width = 27
button_width = 26

my_entry = tk.Entry(entry_frame, width=widget_width, font=(10))
my_entry.grid(row=0, column=0, sticky="nsew")

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

#Initialising to 0 every time the program starts
completed_tasks_counter = 0

#This function changes the number of the variable that counts completed tasks
def tasks_counter_updater():
    tasks_completed = tk.Label(completed_tasks_counter_frame, text = 'Completed Tasks : ' + str(completed_tasks_counter), width = button_width, font = (10))
    tasks_completed.grid(row = 0, column = 0, columnspan = 2, sticky="nsew")

#this function is called when the program starts to set the counter to the correct value
tasks_counter_updater()


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
last_action_was_done = False
# this function is the command for the delete button
# it uses the indicies of all selected items in the listbox with the curselection method. 
def delete_item():
    global completed_tasks_counter
    global listbox_list
    global deleted_tasks
    global last_action_was_done
    selected_indecies = list(reversed(list_box.curselection()))
    if(len(selected_indecies) == 0):    
        return
    last_action_was_done = False
    
    deleted_tasks = []
    #contains a reversed list of the currently selected indecies 
    
    for i in range(len(selected_indecies)):
        list_index = selected_indecies[i]
        #removing element from the listbox
        list_box.delete(list_index)
        #removing the string from the listbox_list so that input validation doesnt catch removed strings
        #debugging statement
        deleted_tasks.append(listbox_list.pop(list_index))
    #putting how many tasks have been "completed" or deleted using this function
    
    # completed_tasks_counter += len(selected_indecies)

    #overriting the file with the new listbox_list
    with open("tasks.txt", "w") as file:
        for i in range(len(listbox_list)):
            file.write(listbox_list[i] + "\n")
    
    return len(selected_indecies)

def done_function():
    global last_action_was_done
    global completed_tasks_counter
    completed_tasks_counter += delete_item()
    last_action_was_done = True
    tasks_counter_updater()


#this function reverses the last delete operation
#if only one task was deleted then it will only add that one task back
#if mutiple tasks were deleted then it will add all of them back
def undo():
    global deleted_tasks
    global completed_tasks_counter
    if(len(deleted_tasks) != 0):
        if(last_action_was_done):
            completed_tasks_counter -= len(deleted_tasks)
        tasks_counter_updater()
        for i in range(len(deleted_tasks)):
            add_task(deleted_tasks[i])
        deleted_tasks = []
    with open("tasks.txt", "w") as file:
        for i in range(len(listbox_list)):
            file.write(listbox_list[i] + "\n")
    




#-------------Buttons------------------#
add_button = tk.Button(add_button_frame, text = "Add", command = add_button_function, width= button_width, font=(10))
add_button.grid(row = 0,column = 0, sticky="nsew")

tk.Button(done_button_frame,text =  "Done", command= done_function, width= button_width, font=(10)).grid(row = 0, column= 1, sticky="nsew")
width = main.winfo_width()
print(width)

tk.Button(undo_frame, text = "Undo", command = undo, width= button_width - 10).grid(row = 0, column = 0, sticky="nsew")
tk.Button(undo_frame, text = "Delete", command = delete_item, width= button_width - 10).grid(row = 0, column = 1, sticky="nsew")


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

main.update()
width = main.winfo_width()




tk.mainloop()
