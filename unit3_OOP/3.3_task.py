# Завдання 1
# Створіть клас, який описує автомобіль. 
# Які атрибути та методи мають бути повністю інкапсульовані? 
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

# class Car:
#     def __init__(self, name: str, max_speed: int):
#         self.__name = name            # приватний атрибут
#         self.__max_speed = max_speed  # приватний атрибут

#     def set_name(self, new_name: str):
#         if len(new_name) < 2:
#             print("ім'я занадто коротке")
#         else:
#             self.__name = new_name

#     def get_name(self) -> str:
#         return self.__name

#     def set_max_speed(self, new_speed: int):
#         if new_speed < 0:
#             print("максимальна швидкість не може бути від'ємною")
#         else:
#             self.__max_speed = new_speed

#     def get_max_speed(self) -> int:
#         return self.__max_speed
      
# car1 = Car("BMW", 240)
# car1.set_name("Audi")  # зміна імені через метод класу
# car1.set_max_speed(260)  # зміна максимальної швидкості через метод класу
# print(car1.get_name())        # тепер ім'я змінилося через метод класу
# print(car1.get_max_speed())   # тепер максимальна швидкість змінилася через метод класу 


