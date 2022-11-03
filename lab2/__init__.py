from MapClass import BasicMap
from UnitClass import Building, Person

if __name__ == '__main__':
    map = BasicMap(25)
    map.CreateMap()
    Base = Building(1000, 5)
    menu = -1
    while menu != 0:
        count_units = len(Base.current_units)
        line = "\nДерево: " + str(Base.current_wood) + ", камень: " + str(Base.current_stone) + ", золото: " + str(Base.current_gold)
        menu = input("В вашем расположении юнитов: " + str(count_units) + line + "\n Что выхотите сделать? \n 1 - Создать юинтов, 2 - Походить юинтами \nОтвет: ")
        if menu == "1":
            action = input("Ваша база создана. У вас есть ресурсы для создания юнитов. Кого вы хотите создать? \n 1 - Пехотинец, 2 - Лучник, 3 - Конный воин : ")
            if action == "0":
                exit()
            else:
                unit = Base.Create_unit(action)
                if not isinstance(unit, str):
                    map.AddUnit(unit, 1, "")
                    if unit.PrevSymbol >= 5 or unit.PrevSymbol <= 7:
                        value = map.AddResourses(unit)
                        if unit.PrevSymbol == 5:
                            Base.current_wood += value
                        elif unit.PrevSymbol == 6:
                            Base.current_stone += value
                        elif unit.PrevSymbol == 7:
                            Base.current_gold += value
                        unit.PrevSymbol = 1
                    map.ArrayToString()
                else:
                    print(unit)
        elif menu == "2":
            line = ""
            i = 1
            if len(Base.current_units) != 0:
                for unit in Base.current_units:
                    line += str(i) + ") " + str(type(unit)) + " Pos: [" + str(unit.Position[0]) + ", " + str(unit.Position[1]) + "]" + " HP: " + str(unit.health) + " ATT: " + str(unit.attack) + " SPD: " + str(unit.speed)
                    if i < len(Base.current_units):
                        line += "\n"
                    i += 1
                move = input("Напишите команду каким юнитом куда хотите походить? Шаблон: 11r \n" + line + "\n:")
                index = int(move[0]) - 1
                step = int(move[1])
                direction = move[2]
                unit = Base.current_units[index]
                if step <= unit.speed:
                    map.AddUnit(unit, step, direction)
                    if unit.PrevSymbol >= 5 or unit.PrevSymbol <= 7:
                        value = map.AddResourses(unit)
                        if unit.PrevSymbol == 5:
                            Base.current_wood += value
                        elif unit.PrevSymbol == 6:
                            Base.current_stone += value
                        elif unit.PrevSymbol == 7:
                            Base.current_gold += value
                        unit.PrevSymbol = 1
                    map.ArrayToString()
                else:
                    print("Юнит не может ходить на такое количество клеток!")
            else:
                print("У вас нет ни одного юнита!")
        else:
            print("Некорректный ответ")