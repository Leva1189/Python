from colorama import Fore
class Hero:
    def __init__(self, name: str, weapon: str, hp: int, damage: int):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.damage = damage
        self.is_alive = True
    def info(self):
        print(f"{Fore.BLUE}{self.name}{Fore.RESET} який тримає в руці {Fore.CYAN}{self.weapon}{Fore.RESET}, має {Fore.GREEN}{self.hp} HP{Fore.RESET} та завдає {Fore.YELLOW}{self.damage} одиниць шкоди{Fore.RESET}.")
    def hit(self, target: Hero):
        #self - той хто атакує
        #target - той хто отримує атаку
        target.hp -= self.damage
        print(f"{Fore.BLUE}{self.name}{Fore.RESET} б'є {Fore.RED}{target.name} та завдає {Fore.YELLOW}{self.damage} одиниць шкоди{Fore.RESET} {Fore.RESET}.")
        print(f"У {Fore.RED}{target.name}{Fore.RESET} залишилось {Fore.GREEN}{target.hp} здоровʼя{Fore.RESET}.")
        
        hero1 = Hero("Артур", "Меч", 100, 20)
        hero2 = Hero("Ланселот", "Спис", 120, 15)
        
        print("Вітайте на арені:\n")
        hero1.info()
        print("\n та \n")
        hero2.info()