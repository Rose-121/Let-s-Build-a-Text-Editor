from tkinter import *
import tkinter as tk

def calculate_interest():
   
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())
    
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    label_result.config(text="Interest: " + str(interest) + "\nTotal: " + str(total_amount))

root = tk.Tk()
root.title("Interest Calculator")

label_principal = tk.Label(root, text="Enter Principal:")
label_principal.grid(row=0, column=0, padx=10, pady=5)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

label_rate = tk.Label(root, text="Enter Rate of Interest (%):")
label_rate.grid(row=1, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=5)

label_time = tk.Label(root, text="Enter Time (Years):")
label_time.grid(row=2, column=0, padx=10, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
