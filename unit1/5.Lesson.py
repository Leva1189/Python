# tuple
# tuple_of_students = ("Dmytro", "Anna", "Olga", "Pavlo")
# print(tuple_of_students)
# print(type(tuple_of_students))
# print(tuple_of_students[0])

# tuple_of_subjects = ("Math", )
# print(type(tuple_of_subjects))

# name = "Levchenko Dmytro"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[1:12])
# # print(len(name))
# print(name[3:])
# print(name[:3])
# print(name[1:10:2])
# print(name[::2])
# print(name[::-1])

# list_names = ("Дмитро", "Ден", "Ігор", "Олег")
# name = input("Введіть ваше ім'я: ")

# if name in list_names:
#     print(f"Вітаю, {name}!")
# else: 
#     print("Вибачте, вас немає у списку.")  

# --------------------------------
# 2 варіанти розв'язку
# --------------------------------
# for n in list_names:
#     if name == n:
#         print(f"Вітаю, {name}!")
#         break
# else:
#     print("Вибачте, вас немає у списку.")


# tuple_of_students = ("Dmytro", "Anna", "Olga", "Pavlo")

# for idx, name in enumerate(tuple_of_students):
#     print(f'{idx + 1}. {name}')

# --------------------------------
#split
# --------------------------------

# string = "Hello world! Welcome to Python programming."
# words = string.split()
# print(words)
