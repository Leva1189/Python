# Патерни
# Патерни — це шаблон рішень певних задач, які можна повторно використовувати в різних контекстах програмування. Вони допомагають структурувати код, робити його більш читабельним і підтримуваним.
# Ітератор (Iterator) — це патерн, який дозволяє послідовно обходити елементи складної структури даних (наприклад, списку, множини або словника) без необхідності розкривати внутрішню структуру цієї колекції.

# import time
# start_time = time.time()
# перший варіант з генератором списку 
# list_number = [number for number in range(1, 200)]
# print(time.time() - start_time)
# print(list_number)


# другий варіант з циклом - 
# list_number = []

# for number in range(1, 200):
#     list_number.append(number)
# print(time.time() - start_time)
# print(list_number)

class MyIterator:
    def __init__(self, end_namber:int):
        self.end_namber = end_namber
    
    def __iter__(self):
        self.current = 0
        return self
      
    def __next__(self):
        if self.current == self.end_namber:
            raise StopIteration
        
        result = self.current
        self.current += 1
        return result
      
for number in MyIterator(10):
    print(number)
    
                
