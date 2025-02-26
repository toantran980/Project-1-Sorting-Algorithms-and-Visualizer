from tkinter import *
import random

#Setup
root = Tk()
root.title("Sorting Algorithm Tester")
root.geometry('430x500')

#functions

#testing tools
def on_left_click(event):
    print(bubble.get())
    print(maxscale.get())
    print(lengthscale.get())
    print(entryfield.get())

root.bind("<Button-1>", on_left_click)

#Function to try to determine which options will be displayed
def selected():
    max = 0
    maxscale.grid_forget()
    lengthscale.grid_forget()
    entryfield.grid(row = 3, columnspan = 5)
    l1.grid(row = 2, columnspan = 5)

def deselected():
    entryfield.grid_forget()
    l3.grid(row=2,columnspan=5)
    l2.grid(row=4,columnspan=5)
    maxscale.grid(row=5, column = 0, columnspan = 5)
    lengthscale.grid(row=7, column = 0, columnspan = 5)

#function connected to start button
def start(max, length, entry, b, m, q, r, l):
    if max == 0:
        lst = list(map(int, entry.split()))
    else:
        lst = [random.randint(0,max) for _ in range(length)]
        
    #call imported output function here

def startbutton():
    start(maxscale.get(), lengthscale.get(), entryfield.get(), bubble.get(), merge.get(), quick.get(), radix.get(), linear.get())

def pausebutton():
    pass

def pause():
    pass

#Reset function
def reset():
    bubble.set(False)
    merge.set(False)
    quick.set(False)
    radix.set(False)
    linear.set(False)
    select.set(False)
    maxscale.set(0)
    lengthscale.set(0)
    entryfield.delete(0, END)

#vars
bubble = BooleanVar()
merge = BooleanVar()
quick = BooleanVar()
radix = BooleanVar()
linear = BooleanVar()
select = BooleanVar()

#radio button
Radiobutton(root, text = "Random List", variable = select, value = False, command = deselected).grid(row = 0)
Radiobutton(root, text = "Defined List", variable = select, value = True, command = selected).grid(row = 1)

#stop button
Button(root, text='Stop', width = 10, command=root.destroy).grid(row=10, column = 0, columnspan = 1)

#start button
Button(root, text='Start', width = 10, command=startbutton).grid(row=10, column = 4, columnspan = 1)

#Reset button
Button(root, text='Reset', width = 10, command=reset).grid(row=10, column = 2,  columnspan = 1)

#Entry for defined list
l1 = Label(root, text="Enter integers separated by spaces")
entryfield = Entry(root)

#scale for choosing max value
l2 = Label(root, text="Select Maximum Value for Integers in the Random List")
l2.grid(row=4,columnspan=5)
maxscale = Scale(root, from_=0, to=9999, length = 300, orient=HORIZONTAL)
maxscale.grid(row=5, column = 0, columnspan = 5)

#second scale for choosing the length of the list
l3 = Label(root, text="Select Length of List")
l3.grid(row=6,columnspan=5)
lengthscale = Scale(root, from_=0, to=9999, length = 300, orient=HORIZONTAL)
lengthscale.grid(row=7, column = 0, columnspan = 5)

# Checkboxes for algos
Checkbutton(root, text="Bubble Sort", variable = bubble, onvalue = True, offvalue = False).grid(row=9, column=0, sticky=W)
Checkbutton(root, text="Merge Sort", variable = merge, onvalue = True, offvalue = False).grid(row=9, column=1, sticky=W)
Checkbutton(root, text="Quick Sort", variable = quick, onvalue = True, offvalue = False).grid(row=9, column=2, sticky=W)
Checkbutton(root, text="Radix Sort", variable = radix, onvalue = True, offvalue = False).grid(row=9, column=3, sticky=W)
Checkbutton(root, text="Linear Sort", variable = linear, onvalue = True, offvalue = False).grid(row=9, column=4, sticky=W)



root.mainloop()


