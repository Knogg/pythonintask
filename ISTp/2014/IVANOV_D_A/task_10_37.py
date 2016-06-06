# Задача 10. Вариант 37
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть
# предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из
# характеристик, которым он решил присвоить другие значения.

# Ivanov. D. A.
# 29.03.2016
import os,sys
AttributeW=["Сила","Здоровье","Мудрость","Ловкость"]
Attribute=[0,0,0,0]
ScoreA=30
print("Генератор персонажа")
print("\nДля выхода в поле выбора введите любую иную команду")
while (ScoreA!=0):
    print("\nДоступно очков для распределения:",ScoreA)
    print("\nВыберите умение"
      "\n\t\tСила[",Attribute[0],"] {ВЫБРАТЬ: 1}"
      "\n\t\tЗдоровье[",Attribute[1],"] {ВЫБРАТЬ: 2}"
      "\n\t\tМудрость[",Attribute[2],"] {ВЫБРАТЬ: 3}"
      "\n\t\tЛовкость[",Attribute[3],"] {ВЫБРАТЬ: 4}")
    print("...Если останется 0 очков для характеристик, программа выдаст финальный результат!...")
    x=input("\nВаш выбор: ")
    if x=="1":
        command=input("\nПрибавить или убавить?(+/-):")
        if command==("+"):
            Attribute[0]+=1
            ScoreA-=1
        elif (command==("-")) & (Attribute[0]!=0):
            Attribute[0]-=1
            ScoreA+=1
        else:
            print("\nНевозможно!")
    elif x=="2":
        command=input("\nПрибавить или убавить?(+/-):")
        if command==("+"):
            Attribute[1]+=1
            ScoreA -= 1
        elif (command==("-")) & (Attribute[1]!=0):
            Attribute[1]-=1
            ScoreA += 1
        else:
            print("\nНевозможно!")
    elif x=="3":
        command=input("\nПрибавить или убавить?(+/-):")
        if command==("+"):
            Attribute[2]+=1
            ScoreA -= 1
        elif (command==("-")) & (Attribute[2]!=0):
            Attribute[2]-=1
            ScoreA += 1
        else:
            print("\nНевозможно!")
    elif x=="4":
        command=input("Прибавить или убавить?(+/-):")
        if command==("+"):
            Attribute[3]+=1
            ScoreA -= 1
        elif (command==("-")) & (Attribute[3]!=0):
            Attribute[3]-=1
            ScoreA += 1
        else:
            print("\nНевозможно!")
    else:
        print("\nНевозможно!")
    if sys.platform=='win32':os.system('cls')
    else:os.system('clear')
print("Поздравляю! Вы создали своего персонажа со следующими характеристиками:"
      "\n\t\tСила[",Attribute[0],"]"
      "\n\t\tЗдоровье[",Attribute[1],"]"
      "\n\t\tМудрость[",Attribute[2],"]"
      "\n\t\tЛовкость[",Attribute[3],"]")
input("\n\nНажмите Enter, чтобы выйти.")
