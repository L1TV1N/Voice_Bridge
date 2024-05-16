import speech_recognition as sr  # импорт библиотек
import pyaudio
from googletrans import Translator
import pyttsx3

def Settings(): # создаём функцию с настройками
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    vvod = int(input("\n1 назад\n2 просмотреть список доступных языков\n3 текущие языки\n4 выбрать языки\n5 список портов\n6 выбрать порт микрофона\nваш выбор: "))

    if vvod == 1:  # создаём кнопку для выхода назад

        start_code()

    if vvod == 2: # создаём кнопку для просмотра списка воспринимаемых языков
        with open('list_lang.txt') as file3:
            list = file3.read()
            print(list)

    if vvod == 3: # создаём кнопку для просмотра тех, языков которые используются для анализа и перевода в данный момент
        with open('file0.txt') as file01:
            a1 = file01.read()
            print("язык распознования", a1)
        with open('file1.txt') as file10:
            b1 = file10.read()
            print("язык перевода", b1)

    if vvod == 4:  # создаём кнопку для выбора языка
        with open('file0.txt', 'w') as file0:
            file0.truncate(0)
            a = input("какой язык распозновать ")
            file0.write(str(a))

        with open('file1.txt', 'w') as file1:
            file1.truncate(0)
            b = input("на какой переводить ")
            file1.write(str(b))

    if vvod == 5:  # создаём кнопку для просмотра портов
        list_mic = sr.Microphone.list_microphone_names()
        for i in range(0, len(list_mic)):
            print(i, list_mic[i])

    if vvod == 6:  # создаём копку  для выбора порта
        with open('file2.txt', 'w') as file2:
            file2.truncate(0)
            d = int(input("\nвведите порт микрофона "))
            file2.write(str(d))

    return Settings()  # возвращаем функцию настроек

def default_Settings():  # создаём функцию с текущими настройками
    global a, b, d

    with open('file0.txt') as file0:
        a = str(file0.read())

    with open('file1.txt') as file1:
        b = str(file1.read())

    with open('file2.txt') as file2:
        d = str(file2.read())


def record_microphone():  # создаём функцию по распознованию речи её переводу и озвучке
    r = sr.Recognizer()  # обозначаем r как переводчик аудио в текст

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    with sr.Microphone(device_index=int(d)) as source:  # обозначаем что выбраный нами порт микрофона является индексом записывающего устрйоства
        r.adjust_for_ambient_noise(source, duration=0.5)  # избавляемся от посторонних шумов

        print('\nСлушаю...')
        audio = r.listen(source)  # записываем данные с микрофона напрямую, в переменную audio

    try:
        query = r.recognize_google(audio, language=a)  # подключаемся к модели при наличии интернета, и переводим вводные данные в текст
        text = query.lower()  # обрабатываем текст

        print(f'было сказано: {text}')
        txt = Translator().translate(text, src=a, dest=b)
        print(txt.text)
        engine.say(txt.text)
        engine.runAndWait()
    except:  # выводим ошибку, если не удалось распознать реч или нет подключения к интернету
        print('Error')

    return record_microphone()

def start_code(): # запускаем код
    default_Settings()
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    vvod = int(input("1 - начать распознание\n2 - настройки\nваш выбор: "))
    if int(vvod) == 1:  # создаём кнопку на распознование перевод и озвучки речи
        record_microphone()
    if int(vvod) == 2: # создаём кнопку для изменения настроек
        Settings()
    else:
        exit()

start_code()