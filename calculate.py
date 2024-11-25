import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    result_entry.delete(0, 'end')
    result_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def umn():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def delet():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('250x250')
window.resizable(False, False)
button_add = tk.Button(window, text = '+', width = 2, height = 1, command = add)
button_add.place(x=35, y=140)
button_sub = tk.Button(window, text = '-', width = 2, height = 1, command = sub)
button_sub.place(x=85, y=140)
button_umn = tk.Button(window, text = '*', width = 2, height = 1, command = umn)
button_umn.place(x=135, y=140)
button_delet = tk.Button(window, text = '/', width = 2, height = 1, command = delet)
button_delet.place(x=185, y=140)
number1_entry = tk.Entry(window, width = 28)
number1_entry.place(x=35, y=30)
number2_entry = tk.Entry(window, width = 28)
number2_entry.place(x=35, y=85)
result_entry = tk.Entry(window, width = 28)
result_entry.place(x=35, y=200)
number1 = tk.Label(window, text = 'Введите первое число')
number1.place(x=35, y=5)
number2 = tk.Label(window, text = 'Введите второе число')
number2.place(x=35, y=60)
result = tk.Label(window, text = 'Ответ:')
result.place(x=35, y=175)
window.mainloop()