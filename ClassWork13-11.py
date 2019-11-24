# import pyowm

# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# city = input ('Enter a city: ')
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# print(w.get_wind()['deg'])                  # {'speed': 4.6, 'deg': 330}
# print(w.get_humidity())              # 87
# print(w.get_temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа,
#  які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач
#  не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
# 
# from random import randint
# def game (comp_number = randint(1,100), user_number = int(input('Guess a number: '))):
#     while user_number != comp_number:
#         if user_number < comp_number:
#             print("Too small")
#             user_number = int(input('Guess a number: '))
#         else:
#             print("Too big") 
#             user_number = int(input('Guess a number: '))
#     print('You guessed!') 
# game()

#2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).

# import math
# def rectangle (a = int(input("Enter side A: ")), b = int(input("Enter side B: "))):
#     print("area is: ", a * b)
# rectangle()

# def triangle (h = float(input("Enter height: ")), a = float(input("Enter base: "))):
#     print("area is: ", 0.5 * h *a)
# triangle()

# def circle (r = float(input("Enter radius: "))):
#     print("area is: ", math.pi*r*r)
# circle()
