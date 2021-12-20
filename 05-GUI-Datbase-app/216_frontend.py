from tkinter import *
import backend_216

def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def view_command():
    list1.delete(0, END) # Clear listbox
    for row in backend_216.view():
        list1.insert(END,row) # Means we insert at the end of the listbox
    clear_entries()

def search_command():
    list1.delete(0, END)
    # Below we pass in the String Vars as input. Need to use the .get() method to get a string
    for row in backend_216.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend_216.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

# This function is bound to an event so gets some of that info
def get_selected_row(event):
    try:
        global selected_tuple # We make selected_tuple a global variable overall
        index = list1.curselection()[0] # We get first item in tuple - is listbox row index
        selected_tuple = list1.get(index) # This gets us the tuple we want
        clear_entries()
        e1.insert(END, selected_tuple[1])
        e2.insert(END, selected_tuple[2])
        e3.insert(END, selected_tuple[3])
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backend_216.delete(selected_tuple[0])
    view_command()

def update_command():
    backend_216.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # print(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END) # Clear listbox
    for row in backend_216.view():
        list1.insert(END,row) # Means we insert at the end of the listbox

window = Tk()

window.wm_title("BookStore")

# Labels
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

# Entries
title_text = StringVar() # This creates spatial object to assign to text variable in next line
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

# Listbox
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2) # Need span otherwise takes one row and column

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

# Connect Scrollbar and List
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

# Binding a method to the listbox
# 2 arguments: 1) event type, 2) function to bind to event
list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()