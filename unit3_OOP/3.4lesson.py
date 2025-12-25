  # Виключення
  
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# try:
#     result = num1 / num2
# except:
#     print("не використовуй 0 в другому числі!")
# print(f"Результат: {(int(result))}")

# Альтернативний спосіб без використання try-except 
# if num2 != 0:
#     result = num1 / num2
#     print(f"Результат: {result}")
# else:
#     print("не використовуй 0 в другому числі!") 


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("не використовуй 0 в другому числі!") 
except ValueError:
    print("будь ласка, вводь лише числа!") 
except:
    print("щось пішло не так!")