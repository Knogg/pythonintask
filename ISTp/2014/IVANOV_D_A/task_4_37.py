# Задача 4. Вариант 37
# Напишите программу, которая выводит имя, под которым скрывается Александр
# Михайлович Гликберг. Дополнительно необходимо вывести область
# интересов указанной личности, место рождения, годы рождения и смерти (если человек
# умер), вычислить возраст на данный момент (или момент смерти). Для хранения
# всех необходимых данных требуется использовать переменные. После вывода
# информации программа должна дожидаться пока пользователь нажмет Enter для
# выхода.

# Ivanov. D. A.
# 06.06.2016

Name="Александр Михайлович Гликберг"
Nickname="Саша Черный"
FamousJob="русский поэт"
Place_of_birth="Одесса, Российская Империя"
Year_of_bitrh=1880
Year_of_death=1932
Hobby="поэзия, публицистика, журналистика"

print(Name+" более известен, как",FamousJob,Nickname)
print("Место рождения:",Place_of_birth,
    "\nГод рождения:",Year_of_bitrh,
    "\nГод смерти:",Year_of_death,
    "\nВозраст на момент смерти:",Year_of_death-Year_of_bitrh-1,
      #Он не умер в свой день рождения или далее, он до него не дожил, а следовательно на год меньше ему лет
    "\nОбласть интересов:",Hobby)
input ('\nНажмите Enter для выхода.')
