# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать



number = int(input("Количество учеников: "))
listrost= []
for i in range(number):
    rost = int(input(f"Рост {i + 1} ученика: "))
    listrost.append(rost)
petya = int(input("Рост Пети: "))
listrost.append(petya)
listrost.sort(reverse=True)
print(listrost.index(petya) + 1)
