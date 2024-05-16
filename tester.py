import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def start_recognition():
    # Здесь добавьте код для начала распознавания голоса
    pass

window = ThemedTk(theme="equilux")  # Используем тему "equilux"
window.title("Голосовой мост")
window.geometry('400x600')

# Градиентный прямоугольник
gradient_rectangle = tk.Frame(window, width=352, height=283, bg='#804AD7')
gradient_rectangle.grid(column=0, row=0, pady=(20, 10))

# Выпадающий список для выбора языка распознавания
recognition_label = ttk.Label(window, text="Язык распознавания:", foreground='white', background='#804AD7')
recognition_label.grid(column=0, row=1, padx=10, pady=(0, 5))

recognition_language = ttk.Combobox(window, values=["Ru", "En"], state="readonly", width=10)
recognition_language.set("Ru")
recognition_language.grid(column=0, row=2, padx=10)

# Выпадающий список для выбора языка перевода
translation_label = ttk.Label(window, text="Язык перевода:", foreground='white', background='#804AD7')
translation_label.grid(column=0, row=3, padx=10, pady=(10, 5))

translation_language = ttk.Combobox(window, values=["En", "Ru"], state="readonly", width=10)
translation_language.set("En")
translation_language.grid(column=0, row=4, padx=10)

# Надпись о начале распознавания
start_label = ttk.Label(window, text="Нажмите кнопку для начала распознавания:", foreground='white', background='#804AD7')
start_label.grid(column=0, row=5, pady=(20, 5))

# # Иконка микрофона
# microphone_icon = tk.PhotoImage(file="microphone-icon.jpg")

microphone_button = ttk.Button(window,  command=start_recognition, style='Microphone.TButton')
microphone_button.grid(column=0, row=6, pady=(0, 20))

window.mainloop()
