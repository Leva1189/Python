# Завдання 1 
# Створіть список та введіть його значення. 
# Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень. 

# numbers = []
# while True:
#     number =  input("Введіть число або '-' для завершення: ")
#     if number == '-':
#       print("Введення чисел завершено.")
#       break
#     else:
#       number = int(number)
#       numbers += (number, )
# print("Створений список:", numbers)  
# print("Найбільший елемент:", max(numbers))  
# print("Найменший елемент:", min(numbers))  

# Завдання 2 
# Є два списки, які наповнюються користувачем з клавіатури. 
# Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку та навпаки без повторень. 
# Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.

# num1 = []
# num2 = []
# while True:
#     number1 =  input("Введіть число для першого списку або '-' для завершення: ")
#     if number1 == '-':
#       print("Введення чисел до першого списку завершено.")
#       break
#     else:
#       number1 = int(number1)
#       num1.append(number1)

# while True:
#     number2 =  input("Введіть число для другого списку або '-' для завершення: ")
#     if number2 == '-':
#       print("Введення чисел до другого списку завершено.")
#       break
#     else:
#       number2 = int(number2)
#       num2.append(number2)
# unique_num1 = set(num1) - set(num2)
# unique_num2 = set(num2) - set(num1)
# result = list(unique_num1.union(unique_num2))
# print("Підсумковий список у прямій послідовності:", result)  
# print("Підсумковий список у зворотній послідовності:", result[::-1])  
# print("Підсумковий список відсортований за зростанням:", sorted(result))  
# print("Підсумковий список відсортований за спаданням:", sorted(result, reverse=True))


# Завдання 3
# Простим називається число, яке ділиться на ціле лише на одиницю і на саме себе. 
# Число 1 не вважається простим. 
# Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран, а потім на вимогу користувача виводить їхню суму або добуток.
# start = int(input("Введіть початок проміжку: "))
# end = int(input("Введіть кінець проміжку: "))
# primes = []
# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
# print("Прості числа в заданому проміжку:", primes)
# while True:
#     choice = input("Введіть 'суму' для обчислення суми простих чисел або 'добуток' для обчислення добутку (або '-' для виходу): ")
#     if choice == 'суму':
#         print("Сума простих чисел:", sum(primes))
#     elif choice == 'добуток':
#         product = 1
#         for p in primes:
#             product *= p
#         print("Добуток простих чисел:", product)
#     elif choice == '-':
#         print("Вихід з програми.")
#         break
#     else:
#         print("Невірний вибір. Спробуйте ще раз.")

# Завдання 4
# Створіть цілочисельний список, 
# введіть кількість його елементів і самі значення. 
# Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням.

# numbers = []
# n = int(input("Введіть кількість елементів списку: "))
# for i in range(n):
#     number = int(input(f"Введіть елемент {i + 1}: "))
#     numbers.append(number)
    

# while True:
#     choice = input("Введіть '1' для виведення у зворотному порядку, '2' для сортування за зростанням або '-' для завершення: ")
#     if choice == '-':
#        print("Введення чисел завершено.")
#        break
#     elif choice == '1':
#        print("Список у зворотному порядку:", numbers[::-1])
#     elif choice == '2':
#        print("Список відсортований за зростанням:", sorted(numbers))
#     else:
#        print("Невірний вибір. Спробуйте ще раз.")
#     continue


# Завдання 5
# Створіть список натуральних чисел int_list. 
# Кожне непарне значення списку додайте до нового списку new_list. 
# Користувач вводить з клавіатури кількість повторів списку repeat. 
# Здійсніть дублювання списку new_list, repeat кількість разів. Очистіть список int_list. 

# int_list = []
# n = int(input("Введіть кількість елементів списку: "))
# for i in range(n):
#     number = int(input(f"Введіть елемент {i + 1}: "))
#     int_list.append(number)

# new_list = [num for num in int_list if num % 2 != 0]
# repeat = int(input("Введіть кількість повторів списку: "))
# new_list *= repeat
# int_list.clear()
# print("Новий список після дублювання:", new_list)
# print("Очищений список int_list:", int_list)


# Завдання 6
# Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5. 
# Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.

# int_list = []
# n = int(input("Введіть кількість елементів списку: "))
# for i in range(n):
#     number = int(input(f"Введіть елемент {i + 1}: "))
#     int_list.append(number)
# new_list = [num for num in int_list if num % 2 != 0]
# repeat = int(input("Введіть кількість повторів списку: "))
# new_list *= repeat
# search_value = int(input("Введіть значення для пошуку у списку: "))
# if search_value in new_list:
#     count = new_list.count(search_value)
#     positions = [index for index, value in enumerate(new_list) if value == search_value]
#     print(f"Значення {search_value} зустрічається {count} раз(и) у списку.")
#     print(f"Позиції значення {search_value} у списку: {positions}")
# else:
#     print(f"Значення {search_value} не знайдено у списку.")
#     print(f"Список значень: {new_list}")
#     print(f"Кількість елементів у списку: {len(new_list)}")
    