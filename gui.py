from tkinter import *

#Setup
root = Tk()
root.title("Sorting Algorithm Tester")
root.geometry('430x500')



#functions
def selected():
    pass

#vars
bubble = BooleanVar()
merge = BooleanVar()
quick = BooleanVar()
radix = BooleanVar()
linear = BooleanVar()
select = BooleanVar()
lst = []
max = 0
entry = ""

Radiobutton(root, text = "Random List", variable = select, value = False, command = selected).grid(row = 0)
Radiobutton(root, text = "Defined List", variable = select, value = True).grid(row = 1)

#start button
Button(root, text='Start', width = 10, command=selected).grid(row=10, column = 0, columnspan = 5)

#Pause button
Button(root, text='Pause', width = 10, command=selected).grid(row=10, column = 4, columnspan = 5)

#Reset button
Button(root, text='Reset', width = 10, command=selected).grid(row=10, column = 10,  columnspan = 10)

#stop button
Button(root, text='Stop', width = 10, command=root.destroy).grid(row=10, column = 2, columnspan = 5)

#Entry for defined list
Label(root, text="Enter integers separated by commas").grid(row=2,columnspan=5)
entry = Entry(root).grid(row = 3, columnspan = 5)

#scale for choosing max value
Label(root, text="Select Maximum Value for Random List").grid(row=4,columnspan=5)
Scale(root, from_=0, to=9999, length = 300, orient=HORIZONTAL).grid(row=5, column = 0, columnspan = 5)

# Checkboxes for algos
Checkbutton(root, text="Bubble Sort", variable = bubble, onvalue = True, offvalue = False).grid(row=9, column=0, sticky=W)
Checkbutton(root, text="Merge Sort", variable = merge, onvalue = True, offvalue = False).grid(row=9, column=1, sticky=W)
Checkbutton(root, text="Quick Sort", variable = quick, onvalue = True, offvalue = False).grid(row=9, column=2, sticky=W)
Checkbutton(root, text="Radix Sort", variable = radix, onvalue = True, offvalue = False).grid(row=9, column=3, sticky=W)
Checkbutton(root, text="Linear Sort", variable = linear, onvalue = True, offvalue = False).grid(row=9, column=4, sticky=W)




root.mainloop()

