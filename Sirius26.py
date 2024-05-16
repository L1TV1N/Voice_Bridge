import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk
import speech_recognition as sr
import pyaudio
from deep_translator import GoogleTranslator
import pyttsx3

def translate_text():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    with sr.Microphone(device_index=int(d.get())) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('\nСлушаю...')
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language=a.get())
        text = query.lower()
        print(f'было сказано: {text}')
        txt = GoogleTranslator(source=a.get(), target=b.get()).translate(text)
        print(txt)
        engine.say(txt)
        engine.runAndWait()
        text_area.insert(tk.INSERT, txt + '\n')
    except:
        print('Error')

def save_settings():
    with open('file0.txt', 'w') as file0:
        file0.write(a.get())

    with open('file1.txt', 'w') as file1:
        file1.write(b.get())

    with open('file2.txt', 'w') as file2:
        file2.write(d.get())

def update_settings(*args):
    save_settings()
    default_Settings()

def default_Settings():
    with open('file0.txt') as file0:
        a.set(file0.read())

    with open('file1.txt') as file1:
        b.set(file1.read())

    with open('file2.txt') as file2:
        d.set(file2.read())

window = ThemedTk(theme="black")  # Используем тему "black"
window.title("Голосовой мост")
window.geometry('800x600')

style = ttk.Style()
style.configure('TButton', foreground='white', background='black')
style.configure('TLabel', foreground='white', background='black')

label1 = ttk.Label(window, text="Нажмите кнопку для начала распознавания:")
label1.grid(column=0, row=0)

translate_button = ttk.Button(window, text="Начать распознавание", command=translate_text)
translate_button.grid(column=1, row=0)

text_area = scrolledtext.ScrolledText(window, width=70, height=20, bg='black', fg='white')
text_area.grid(column=0, row=1, columnspan=2)

settings_label = ttk.Label(window, text="Настройки:")
settings_label.grid(column=0, row=2)

language_options = ['en', 'ru', 'fr', 'de', 'es']
a = tk.StringVar(window)
a.set('ru')
a.trace('w', update_settings)
language_dropdown = ttk.OptionMenu(window, a, *language_options)
language_dropdown.grid(column=1, row=2)

translate_options = ['en', 'ru', 'fr', 'de', 'es']
b = tk.StringVar(window)
b.set('en')
b.trace('w', update_settings)
translate_dropdown = ttk.OptionMenu(window, b, *translate_options)
translate_dropdown.grid(column=1, row=3)

mic_options = list(range(0, 10))
d = tk.StringVar(window)
d.set('0')
d.trace('w', update_settings)
mic_dropdown = ttk.OptionMenu(window, d, *mic_options)
mic_dropdown.grid(column=1, row=4)

default_Settings()  # Вызываем функцию после определения всех переменных

window.mainloop()
