#-------------Exercise------------------

import tkinter as cal

def multi_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text="Zero be Zero")
        return

    output = ""
    for i in range (1,13):
        output += str(number) + ' x ' + str(i) + ' = ' + str(number * i) + '\n'
        #output += ' = ' + str(number * i) 

    output_label.configure(text=output)

window = cal.Tk()
window.title("Math Calculator")
window.minsize(800,800)

title_label = cal.Label(master=window, text="Multiple")
title_label.pack()

number_input = cal.Entry(master=window, width=30)
number_input.pack()

go_button = cal.Button(
    master=window, text="Equal to",
    command=multi_output, width=20, height=2
    )
go_button.pack()

output_label = cal.Label(master=window)
output_label.pack()

window.mainloop()