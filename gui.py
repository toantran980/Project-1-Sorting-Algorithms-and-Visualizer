from tkinter import *
import random
import time
from visualizer import visualize
import pygame

# Setup
root = Tk()
root.title("Sorting Algorithm Tester")
root.geometry('450x350')
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Testing tools
def on_left_click(event):
    print(bubble.get())
    print(merge.get())
    print(quick.get())
    print(radix.get())
    print(linear.get())
    print(maxscale.get())
    print(lengthscale.get())
    print(entryfield.get())

#root.bind("<Button-1>", on_left_click)

# Function to try to determine which options will be displayed
def selected():
    maxscale.grid_forget()
    lengthscale.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    bubbleb.grid_forget()
    mergeb.grid_forget()
    quickb.grid_forget()
    radixb.grid_forget()
    linearb.grid_forget()
    start_.grid_forget()
    stop.grid_forget()
    reset.grid_forget()
    
    
    bubbleb.grid(row=4, column=0, sticky=W)
    mergeb.grid(row=4, column=1, sticky=W)
    quickb.grid(row=4, column=2, sticky=W)
    radixb.grid(row=4, column=3, sticky=W)
    linearb.grid(row=4, column=4, sticky=W)
    stop.grid(row=7, column=0, columnspan=1)
    reset.grid(row=7, column=2, columnspan=1)
    start_.grid(row=7, column=4, columnspan=1)
    entryfield.grid(row=3, columnspan=5)
    l1.grid(row=2, columnspan=5)

def deselected():
    entryfield.grid_forget()
    l1.grid_forget()
    bubble_.grid_forget()
    merge_.grid_forget()
    quick_.grid_forget()
    radix_.grid_forget()
    linear_.grid_forget()
    start_.grid_forget()
    stop.grid_forget()
    reset.grid_forget()

    bubble_.grid(row=6, column=0, sticky=W)
    merge_.grid(row=6, column=1, sticky=W)
    quick_.grid(row=6, column=2, sticky=W)
    radix_.grid(row=6, column=3, sticky=W)
    linear_.grid(row=6, column=4, sticky=W)
    stop.grid(row=7, column=0, columnspan=1)
    reset.grid(row=7, column=2, columnspan=1)
    start_.grid(row=7, column=4, columnspan=1)
    l3.grid(row=2, columnspan=5)
    l2.grid(row=4, columnspan=5)
    maxscale.grid(row=5, column=0, columnspan=5)
    lengthscale.grid(row=3, column=0, columnspan=5)

# Function connected to start button
def start(max, length, entry, b, m, q, r, l):
    error_message_label.config(text="")  # Clear any previous error message
    if max == 0:
        lst = list(map(int, entry.split()))
    else:
        lst = [random.randint(0, max) for _ in range(length)]

    # Call imported output function here
    target = None
    if l:
        target_value = target_entry.get()
        if target_value.isdigit():
            target = int(target_value)
        else:
            error_message_label.config(text="Only integers are allowed for target value")
            return
        if target not in lst:
            error_message_label.config(text="Target value is not in the list")
            return
    
    execution_time = 0
    if b:
        execution_time = visualize(screen, ["b"], lst, target)
    if m:
        execution_time = visualize(screen, ["m"], lst, target)
    if q:
        execution_time = visualize(screen, ["q"], lst, target)
    if r:
        execution_time = visualize(screen, ["r"], lst, target)
    if l:
        execution_time = visualize(screen, ["l"], lst, target)
    if l and target is not None:
        execution_time_label.config(text=f"Execution time: {execution_time:.6f} nanoseconds")
    
    execution_time_label.config(text=f"Execution time: {execution_time:.6f} nanoseconds")

def startbutton():
    start(maxscale.get(), lengthscale.get(), entryfield.get(), bubble.get(), merge.get(), quick.get(), radix.get(), linear.get())

# Reset function
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
    target_entry.delete(0, END)
    execution_time_label.config(text="Execution time: N/A")
    error_message_label.config(text="") 

# Vars
bubble = BooleanVar()
merge = BooleanVar()
quick = BooleanVar()
radix = BooleanVar()
linear = BooleanVar()
select = BooleanVar()

# Radio button
Radiobutton(root, text="Random List", variable=select, value=False, command=deselected).grid(row=0)
Radiobutton(root, text="Defined List", variable=select, value=True, command=selected).grid(row=1)

# Stop button
stop = Button(root, text='Stop', width=10, command=root.destroy)
stop.grid(row=7, column=0, columnspan=1)

# Start button
start_ = Button(root, text='Start', width=10, command=startbutton)
start_.grid(row=7, column=4, columnspan=1)

# Reset button
reset = Button(root, text='Reset', width=10, command=reset)
reset.grid(row=7, column=2, columnspan=1)

# Entry for defined list
l1 = Label(root, text="Enter integers separated by spaces")
entryfield = Entry(root)

# Scale for choosing max value
l2 = Label(root, text="Select Maximum Value for Integers in the Random List")
l2.grid(row=4, columnspan=5)
maxscale = Scale(root, from_=0, to=999, length=300, orient=HORIZONTAL)
maxscale.grid(row=5, column=0, columnspan=5)

# Second scale for choosing the length of the list
l3 = Label(root, text="Select Length of List")
l3.grid(row=2, columnspan=5)
lengthscale = Scale(root, from_=0, to=999, length=300, orient=HORIZONTAL)
lengthscale.grid(row=3, column=0, columnspan=5)

# Checkboxes for algos
bubble_ = Checkbutton(root, text="Bubble Sort", variable=bubble, onvalue=True, offvalue=False).grid(row=6, column=0, sticky=W)
merge_ = Checkbutton(root, text="Merge Sort", variable=merge, onvalue=True, offvalue=False).grid(row=6, column=1, sticky=W)
quick_ = Checkbutton(root, text="Quick Sort", variable=quick, onvalue=True, offvalue=False).grid(row=6, column=2, sticky=W)
radix_ = Checkbutton(root, text="Radix Sort", variable=radix, onvalue=True, offvalue=False).grid(row=6, column=3, sticky=W)
linear_ = Checkbutton(root, text="Linear Search", variable=linear, onvalue=True, offvalue=False).grid(row=6, column=4, sticky=W)

# Entry for target value
target_label = Label(root, text="Enter target value for search")
target_label.grid(row=9, columnspan=5)
target_entry = Entry(root)
target_entry.grid(row=10, columnspan=5)

# Error message label
error_message_label = Label(root, text="", fg="red")
error_message_label.grid(row=13, column=0, columnspan=5)

# Label to display execution time
execution_time_label = Label(root, text="Execution time: N/A")
execution_time_label.grid(row=8, column=0, columnspan=5)

root.mainloop()
