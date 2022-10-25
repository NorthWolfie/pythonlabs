from MapClass import BasicMap
from UnitClass import Building

if __name__ == '__main__':
    #answer = input("Хотите создать карту для игры? Да/Нет ")
    #if answer == "Да" or answer == "да":
        # size = input("Укажите размер карты: ")
    map = BasicMap(25)
    map.Create()
    Base = Building()
    action = input("Ваша база создана. У вас есть ресурсы для создания юнитов. Кого вы хотите создать? \n 1 - Пехотинец, 2 - Лучник, 3 - Конный воин : ")
    if action == 0:
        exit()
    else:
        Base.Create_unit(action)


    #elif answer == "Нет" or answer == "нет":
        #pass
    #else:
        #print("Некорректный ответ")