# -------------------------------------------------------------------------------
# Завдання 1
# Створіть клас, який описує книгу. 
# Він повинен містити інформацію про автора, назву, рік видання та жанр. 
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.


class Book:
    def __init__(self, author: str, title: str, year: int, genre: str):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        
    def __repr__(self)-> str:
        return f"Книга({self.title}, Автор: {self.author}, Рік: {self.year}, Жанр:  {self.genre})"

    def __str__(self)-> str:
        return f"'{self.title}' - це {self.genre} книга, написана {self.author} у {self.year} році."

book1 = Book("Дж. К. Ролінг", "Гаррі Поттер і філософський камінь", 1997, "фентезі")
book2 = Book("Дж. Р. Р. Толкін", "Володар перснів", 1954, "епічне фентезі")
book3 = Book("Габріель Гарсіа Маркес", "Сто років самотності", 1967, "магічний реалізм")

list_books = [book1, book2, book3]

print(list_books)

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# Завдання 2
# Створіть клас, який описує відгук до книги. 
# Додайте до класу книги поле – список відгуків. 
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї. 

# class Review:
#     def __init__(self, reviewer: str, rating: int, comment: str):
#         self.reviewer = reviewer
#         self.rating = rating
#         self.comment = comment
# class Book:
#     def __init__(self, author: str, title: str, year: int, genre: str):
#         self.author = author
#         self.title = title
#         self.year = year
#         self.genre = genre
#         self.reviews = []
        
#     def add_review(self, review: Review):
#         self.reviews.append(review)
        
#     def __str__(self):
#         reviews_str = "\n".join([f"{review.reviewer} - {review.rating}/5: {review.comment}" for review in self.reviews])
#         return f"'{self.title}' - це {self.genre} книга, написана {self.author} у {self.year} році.\nВідгуки:\n{reviews_str}"
      
# book1 = Book("Дж. К. Ролінг", "Гаррі Поттер і філософський камінь", 1997, "фентезі")
# review1 = Review("Анна", 5, "Неймовірна книга!")
# review2 = Review("Олег", 4, "Дуже цікава, але іноді затягнута.")
# book1.add_review(review1)
# book1.add_review(review2) 

# print(book1)        
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# Завдання 3
# Ознайомтеся зі спеціальними методами в Python, 
# використовуючи посилання в кінці уроку, і навчіться використовувати ті з них, 
# призначення яких ви можете зрозуміти. 
# Повертайтеся до цієї теми протягом усього курсу та вивчайте спеціальні методи, що відповідають темам кожного уроку.



# -------------------------------------------------------------------------------

# Завдання 4
# Створіть клас, який описує автомобіль. 
# Створіть клас автосалону, що містить в собі список автомобілів, 
# доступних для продажу, і функцію продажу заданого автомобіля.

# class Car:
#     def __init__(self, make: str, model: str, year: int):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def __str__(self):
#         return f"{self.year} {self.make} {self.model}"

# class CarDealership:
#     def __init__(self):
#         self.cars = []
        
#     def add_car(self, car: Car):
#         self.cars.append(car)
        
#     def sell_car(self, car: Car):
#         if car in self.cars:
#             self.cars.remove(car)
#             print(f"Продано: {car}")
#         else:
#             print(f"Автомобіль {car} не знайдено в автосалоні.")
            
# dealership = CarDealership()
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("Honda", "Civic", 2019)
# dealership.add_car(car1)
# dealership.add_car(car2)                        

# print("Автомобілі в автосалоні:")
# for car in dealership.cars:
#     print(car)

# dealership.sell_car(car1)
# print("Автомобілі в автосалоні після продажу:")
# for car in dealership.cars:
#     print(car)

