# Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).
# 
# method 1
# number = 100
# i = 0
# while i < number:
#     print(i)
#     i += 2
#
# method 2
# print(list(range(1,100,2)))
# for value in range(100):
#     if value%2==0:
#         print(value)

# Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
# method 1
# print(list(range(1,100,2)))
# for value in range(100):
#     if value%2==1:
#         print(value)

# method 2
# for value in range(100):
#     if value%2==0:
#         continue
#     print(value)

# Перевірити чи список містить непарні числа.
# method 1
# list_number = [5, 47, 88, 96]
# for value in list_number:
#    if value%2==1:
#        print("Yes, there are odd numbers")
#        break

# method 2
# list_number=[2,4,6,8,10]
# contain_odd=False
# for item in list_number:
#    if not item % 2 == 0:
#        contain_odd=True
#        break
# if contain_odd:
#    print("There is odd number in the list")
# else:
#    print("There's only even numbers in the list")

# Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
#(Підказка: використати вбудовану функцію float ()).

#set_numbers = [55,78,854,84,65,33]
#for item in set_numbers:
#   print(float(item))

# Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# a = 0
# b = 1
# last = int(input ("Enter your number "))
# print(a)
# print(b)
# for value in range(last):
#     c = a + b
#     a = b 
#     b = c 
#     print(c)

# 6.  Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.
# some_list = input ('Input something: ').split()
# for word in some_list:
#     print(word)

# 7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
#           (Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).
# some_list = input ('Input something: ')
# for word in some_list:
#     for letter in word:
#         print(letter, end='#')

# # 8.  Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.
