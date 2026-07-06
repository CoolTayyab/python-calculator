import tkinter as tk
#from tkinter import Button
root = tk.Tk()
root.title("calculator")
root.geometry("300x300")

screen = tk.Entry(root, width=20, font=("Arial", 20))
screen.grid(row=0, column=0, columnspan=4)


def click(value):
    screen.insert(tk.END, value)

def equal():
    text = screen.get()
    result = eval(text)
    screen.delete(0, tk.END)
    screen.insert(tk.END, result)

def clear():
    screen.delete(0, tk.END)

def backspace():
    text = screen.get()
    if len(text) > 0:
        screen.delete(0, tk.END)
        screen.insert(0, text[:-1])


btn_back = tk.Button(root, text="⌫", command=backspace)
btn_back.grid(row=1,column=3,padx=5, pady=5)
btn_7 = tk.Button(root, text="7", command=lambda: click("7"))
btn_8 = tk.Button(root, text="8", command=lambda: click("8"))
btn_9 = tk.Button(root, text="9", command=lambda: click("9"))
btn_div = tk.Button(root, text="/", command=lambda: click("/"))

btn_7.grid(row=2,column=0,padx=5, pady=5)
btn_8.grid(row=2,column=1,padx=5, pady=5)
btn_9.grid(row=2,column=2,padx=5, pady=5)
btn_div.grid(row=2,column=3,padx=5, pady=5)

btn_6 = tk.Button(root, text="6", command=lambda: click("6"))
btn_5 = tk.Button(root, text="5", command=lambda: click("5"))
btn_4 = tk.Button(root, text="4", command=lambda: click("4"))
btn_mul = tk.Button(root, text="*", command=lambda: click("*"))

btn_4.grid(row=3, column=0,padx=5, pady=5)
btn_5.grid(row=3, column=1,padx=5, pady=5)
btn_6.grid(row=3, column=2,padx=5, pady=5)
btn_mul.grid(row=3, column=3,padx=5, pady=5)

btn_3 = tk.Button(root, text="3", command=lambda: click("3"))
btn_2 = tk.Button(root, text="2", command=lambda: click("2"))
btn_1 = tk.Button(root, text="1", command=lambda: click("1"))
btn_minus = tk.Button(root, text="-", command=lambda: click("-"))

btn_1.grid(row=4, column=0,padx=5, pady=5)
btn_2.grid(row=4, column=1,padx=5, pady=5)
btn_3.grid(row=4, column=2,padx=5, pady=5)
btn_minus.grid(row=4, column=3,padx=5, pady=5)

btn_clear = tk.Button(root, text="C", command=clear)
btn_0 = tk.Button(root, text="0", command=lambda: click("0"))
btn_plus = tk.Button(root, text="+", command=lambda: click("+"))
btn_equal = tk.Button(root, text="=", command=equal)


btn_clear.grid(row=5, column=0,padx=5, pady=5)
btn_0.grid(row=5, column=1,padx=5, pady=5)
btn_plus.grid(row=5, column=2,padx=5, pady=5)
btn_equal.grid(row=5, column=3,padx=5, pady=5)

root.mainloop()
