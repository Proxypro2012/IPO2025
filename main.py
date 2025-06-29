import subprocess
import sys
import platform
import tkinter as tk
from tkinter import ttk
from setup_utils import install_package

# Please clone the ENTIRE REPOSITORY from github to run the calculator main script well! Faliure to do so may result in errors.




try:
    import sv_ttk
except ImportError:
    try:
        install_package("sv_ttk")
        import sv_ttk
    except ImportError:
        sv_ttk = None


root = tk.Tk()
root.title("Calculator App")
root.resizable(False, False)

if sv_ttk:
    sv_ttk.use_dark_theme()     
else:
    ttk.Style().theme_use("clam")         


class CalculatorApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.spawn_widgets()
        

    def spawn_widgets(self):
        row1 = [1, 2, 3]
        row2 = [4, 5, 6]
        row3 = [7, 8, 9]
        row4 = ["0","CE", "AC"]
        row5 = ['=', '.']
        col1 = ["+", "-", "x", "÷"]

        memory = []

        display_input = tk.StringVar(value="")
        display_output = ttk.Entry(self, font=("Arial", 24), textvariable=display_input, justify='right', state='readonly')
        
        display_output.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
            
        def is_operation(s):
            operations = ["+", "-", "x", "÷"]
            return s in operations



        def button_clicked(value):
            if len(memory) == 0 and is_number(value):
                if not value == "0":
                    memory.append(str(value).lstrip("0"))
                else:
                    memory.append(str(value))
                display_input.set(value)
            elif len(memory) == 0 and value == ".":
                memory.append("0.")
                display_input.set("0.")
            elif len(memory) == 0 and is_operation(value):
                return
            elif memory[-1] == "0." and value == ".":
                return
            elif memory[-1][-1] == "." and value == ".":
                return
            elif is_number(memory[-1]) and is_number(value) or value == ".":
                memory[-1] = str(memory[-1]) + str(value)
                display_input.set(memory[-1])
            elif is_number(memory[-1]) and is_operation(value):
                if not value == "0":
                    memory.append(str(value).lstrip("0"))
                else:
                    memory.append(str(value))
                display_input.set(value)
            elif is_operation(memory[-1]) and is_number(value):
                if not value == "0":
                    memory.append(str(value).lstrip("0"))
                else:
                    memory.append(str(value))
                display_input.set(value)
            elif is_operation(memory[-1]) and is_operation(value):
                return
            elif value == "CE":
                if len(memory[-1]) > 1:
                    memory[-1] = memory[-1][:-1]
                    display_input.set(memory[-1])
                else:
                    memory.pop()
                    display_input.set("")
            elif value == "AC":
                if len(memory) > 0:
                    memory.clear()
                else:
                    return
                display_input.set("")
            elif value == "=":
                try:
                    expression = "".join(memory).replace("x", "*").replace("÷", "/").strip()
                    expression = expression.lstrip("+-*/")
                    expression = expression.rstrip("+-*/")
                    print(expression)
                    display_input.set(str(eval(expression)))
                except ZeroDivisionError:
                    display_input.set("Undefined")
                except Exception:
                    display_input.set("Error")
            elif value == "x":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "÷":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "+":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "-":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "0":
                memory.append("0")
                display_input.set(value)
            elif value == "1":
                memory.append("1")
                display_input.set(value)
            elif value == "2":
                memory.append("2")
                display_input.set(value)
            elif value == "3":
                memory.append("3")
                display_input.set(value)
            elif value == "4":
                memory.append("4")
                display_input.set(value)
            elif value == "5":
                memory.append("5")
                display_input.set(value)
            elif value == "6":
                memory.append("6")
                display_input.set(value)
            elif value == "7":
                memory.append("7")
                display_input.set(value)
            elif value == "8":
                memory.append("8")
                display_input.set(value)
            elif value == "9":
                memory.append("9")
                display_input.set(value)
            elif value == "+":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "-":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "x":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            elif value == "÷":
                memory.append(str(value).lstrip("0"))
                display_input.set(value)
            

        
        for i, num in enumerate(row1):
            ttk.Button(self, text=str(num), command=lambda val=num: button_clicked(val)).grid(row=1, column=i, padx=5, pady=5)
        for i, num in enumerate(row2):
            ttk.Button(self, text=str(num), command=lambda val=num: button_clicked(val)).grid(row=2, column=i, padx=5, pady=5)
        for i, num in enumerate(row3):
            ttk.Button(self, text=str(num), command=lambda val=num: button_clicked(val)).grid(row=3, column=i, padx=5, pady=5)
        for i, num in enumerate(row4):
            ttk.Button(self, text=str(num), command=lambda val=num: button_clicked(val)).grid(row=4, column=i, padx=5, pady=5)
        for i, num in enumerate(row5):
            ttk.Button(self, text=str(num), command=lambda val=num: button_clicked(val)).grid(row=5, column=i, padx=5, pady=5)
        for i, operation in enumerate(col1):
            ttk.Button(self, text=str(operation), command=lambda val=operation: button_clicked(val), style="Accent.TButton").grid(row=i+1, column=3, padx=5, pady=5)


app = CalculatorApp(master=root)
app.grid(row=0, column=0)
root.mainloop()
