from tkinter import * 

window = Tk()

def kg_to_grams_pounds_ounces():
    kg = float(e_value.get())
    g = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    g_text.delete("1.0", END) 
    g_text.insert(END, g)
    pounds_text.delete("1.0", END) 
    pounds_text.insert(END, pounds)
    ounces_text.delete("1.0", END) 
    ounces_text.insert(END, ounces)

b1 = Button(window, text = "Convert", command = kg_to_grams_pounds_ounces, height = 1, width = 10)
b1.grid(row = 0, column = 2)

label = Label(window,text="Kg")
label.grid(row = 0, column = 0)

e_value = StringVar()
e = Entry(window, textvariable = e_value)
e.grid(row = 0, column = 1)

g_text = Text(window, height = 1, width = 20)
g_text.grid(row = 1, column = 0)

pounds_text = Text(window, height = 1, width = 20)
pounds_text.grid(row = 1, column = 1)

ounces_text = Text(window, height = 1, width = 20)
ounces_text.grid(row = 1, column = 2)

window.mainloop() 
