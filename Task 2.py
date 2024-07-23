#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

from tkinter import *

# Create the main window
window = Tk()
window.title("Arithmetic Calculator")
window.geometry('800x200')

def calculate():
    try:
        # Get the numbers from the entries
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    
    # Get the selected operation
    operation = operation_var.get()
    
    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        result_label.config(text="Please select an operation.")
        return
    
    # Update the result label
    result_label.config(text=f"Result: {result}")

# First number Label and entry
label1 = Label(window, text="Number 1:")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

# Second number Label and entry
label2 = Label(window, text="Number 2:")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Operation label and radio buttons
operation_var = StringVar()
operation_var.set("+")

label3 = Label(window, text="Operation:")
label3.grid(row=2, column=0, padx=10, pady=5)
operations_frame = Frame(window)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(operations_frame, text="+", variable=operation_var, value="+")
radio_add.pack(side=LEFT)
radio_subtract = Radiobutton(operations_frame, text="-", variable=operation_var, value="-")
radio_subtract.pack(side=LEFT)
radio_multiply = Radiobutton(operations_frame, text="*", variable=operation_var, value="*")
radio_multiply.pack(side=LEFT)
radio_divide = Radiobutton(operations_frame, text="/", variable=operation_var, value="/")
radio_divide.pack(side=LEFT)

# Submit button
submit_button = Button(window, text="Calculate", command=calculate)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show the result
result_label = Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()