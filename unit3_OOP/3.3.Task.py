# Завдання 1
# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? 
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

# class Car:
#     def __init__(self, name: str, max_speed: int):
#         self.__name = name
#         self.__max_speed = max_speed

#     def get_name(self):
#         return self.__name

#     def set_name(self, name: str):
#         self.__name = name

#     def get_max_speed(self):
#         return self.__max_speed

#     def set_max_speed(self, max_speed: int):
#         self.__max_speed = max_speed
        
# car1 = Car("BMW", 240)

# car1.set_name("Audi")  # зміна імені через метод класу
# car1.set_max_speed(260)  # зміна максимальної швидкості через метод класу

# print(car1.get_name())        # тепер ім'я змінилося через метод класу
# print(car1.get_max_speed())   # тепер максимальна швидкістьзмінилася через метод класу          

# //--------------------------------------------------
# Завдання 2
# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). 
# Обидва створюють різні привітання. 
# Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).

# class English:
#     def greeting(self):
#         print("Hello, friend!")

# class Spanish:
#     def greeting(self):
#         print ("¡Hola, amigo!")

# def hello_friend(lang1: English, lang2: Spanish):
#     lang1.greeting()
#     lang2.greeting()
        
# english = English()
# spanish = Spanish()    
# hello_friend(english, spanish)  



# //--------------------------------------------------
# Завдання 3
# Використовуючи посилання наприкінці цього уроку, 
# ознайомтеся з таким засобом інкапсуляції, як властивості. 
# Ознайомтеся з декоратором property у Python. 
# Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, 
# причому дані можуть бути задані в одній шкалі, а отримані в іншій.

# class Temperature:
#     def __init__(self, celsius: float = 0.0):
#         self._celsius = celsius

#     @property
#     def celsius(self) -> float:
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value: float):
#         self._celsius = value

#     @property
#     def fahrenheit(self) -> float:
#         return (self._celsius * 9/5) + 32

#     @fahrenheit.setter
#     def fahrenheit(self, value: float):
#         self._celsius = (value - 32) * 5/9
        
# temp = Temperature()
# temp.celsius = 25

# print(f"Температура в Цельсіях: {temp.celsius}°C")  # Виведе: Температура в Цельсіях: 25.0
# print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")  # Виведе: Температура в Фаренгейтах: 77.0
# temp.fahrenheit = 212
# print(f"Температура в Цельсіях після зміни через Фаренгейти: {temp.celsius}°C")  # Виведе: Температура в Цельсіях після зміни через Фаренгейти: 100.0        
      
        