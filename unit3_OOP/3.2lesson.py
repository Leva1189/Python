#Методи OOP
#1.Спадкоємність

class Sport:
    def __init__(self,count_players:int, name:str, is_olympic:bool, is_contact:bool):
        self.count_players = count_players
        self.name = name
        self.is_olympic = is_olympic
        self.is_contact = is_contact
    
    def print_roles(self):
        print("основне правило будь-якого виду спорту  - це спортивна поведінка")
        
    def __str__(self)->str:
        return f"Sport: {self.name}, players: {self.count_players}, olympic: {self.is_olympic}, contact: {self.is_contact}"

class Basketball(Sport):
    def __init__(self,count_players:int, name:str, 
                 is_olympic:bool, is_contact:bool, 
                 height_of_basket:int):
        super().__init__(count_players, name, is_olympic, is_contact)
        self.height_of_basket = height_of_basket       
    
    def print_roles(self):
        super().print_roles()
        print("треба закинути м'яч у кошик суперника більше разів ніж він закине у ваш")
        
    def __str__(self)->str:
        return f"Basketball: {self.name}, players: {self.count_players}, olympic: {self.is_olympic}, contact: {self.is_contact}, height_of_basket: {self.height_of_basket}"    
        
class Footboll(Sport):
    def __init__(self,count_players:int, name:str, 
                 is_olympic:bool, is_contact:bool, 
                 use_hands:bool):
        super().__init__(count_players, name, is_olympic, is_contact)
        self.use_hands = use_hands
    
    def print_roles(self):
        super().print_roles()
        print("треба забити м'яч у ворота суперника більше разів ніж він заб'є у ваш")    

class MiniFootball(Footboll):
    def print_roles(self):
        super().print_roles()
        print("гра відбувається на меншому полі з меншою кількістю гравців")

class BeachFootball(Footboll):
    def print_roles(self):
        super().print_roles()
        print("гра відбувається на піску")
        
class MMA(Sport):
    def print_roles(self):
        print("треба перемогти суперника за допомогою ударів, кидків або болевих прийомів") #перезадавання батківського методу - ПОЛІМАРФІЗМ   
  
sport1 = Sport(10, "Sport", False, False)
basketball1 = Basketball(12, "Basketball", True, False, 10)
football1 = Footboll(11, "Football", True, True, False)
# minifootball1 = MiniFootball()
# mma = MMA()

sport1.print_roles()
print("-----\n")
basketball1.print_roles()
print("-----\n")

print(sport1)
print("\n")
print(basketball1)
print("\n")
print(football1)

# football1.print_roles()
# print("-----\n")
# minifootball1.print_roles()
# print("-----\n")
# mma.print_roles()