# Поняття файлів та потоків
# Файли - це спеціальні об'єкти, які дозволяють зберігати дані на диску та зчитувати їх пізніше.
# Потоки - це абстракції для роботи з послідовностями даних,

# file = open('unit3_OOP/Task3.6.txt', 'w')
# file.write('Hello, World!----\n')
# file.close()

# with open('unit3_OOP/Task3.6.txt', 'a') as file:
#     file.write('Hello \n')

import os
path_to_dir = os.path.abspath(__file__ + '/..')
PATH = os.path.join(path_to_dir, 'password.txt')

while True:
    print('1 - change password \n 2 - Get password')
    choice = int(input("Enter your choice: "))
    if choice == 1:
      new_password = input("Enter new password: ")
      with open(PATH, 'w') as file:
        file.write(new_password)
    elif choice == 2:
      with open(PATH, 'r') as file:
        password = file.read()
        print(password)
 