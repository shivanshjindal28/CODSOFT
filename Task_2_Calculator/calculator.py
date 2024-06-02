import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid Operation")
        
        result_var.set(f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.configure(bg="#f2f2f2")

# Create StringVar for operations and result
operation_var = tk.StringVar()
result_var = tk.StringVar()

# Title Label
title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333333")
title_label.pack(pady=10)

# Number 1 Entry
entry1 = tk.Entry(root, width=10, font=("Arial", 14))
entry1.pack(pady=5)

# Number 2 Entry
entry2 = tk.Entry(root, width=10, font=("Arial", 14))
entry2.pack(pady=5)

# Operation Dropdown
operations = ['+', '-', '*', '/']
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_var.set(operations[0])  # default value
operation_menu.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 14))
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="#f2f2f2", fg="#333333")
result_label.pack(pady=10)

# Run the application
root.mainloop()
