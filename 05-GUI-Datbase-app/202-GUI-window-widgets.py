from tkinter import * # We do this to import all subcomponents

window = Tk() # Creates an empty window

# Creating a button
b1 = Button(window, text = "Execute")

# Specify where to put button - few methods. grid method more control than pack
# b1.pack()
b1.grid(row = 0, column = 0) # Another option is rowspan = 2

e1 = Entry(window)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop() # All widgets come between the first window set up and here
