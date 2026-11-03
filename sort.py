from random import randint as ri
sl = [] #создаем список из 100 элементов
for i in range(0, 100):
    sl.append(ri(0, 1_000_000))
print("Сортировка пузырьком ")
slb = sl.copy() #Делаем копию изначального списка
b = 0 # задаем счетчики сравнений
c= 0 
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(slb) - 1):
        b += 1
        if slb[i] < slb[i + 1]: #  меняем местами элементы , если левый меньше правого
            swap = slb[i]
            slb[i] = slb[i + 1]
            slb[i + 1] = swap
            stop_flag =True
    c += 1  
    print(f"Шаг {c}: {slb}") # Выводим промежуточный результат после каждой итерации
print("\nКонечный результат пузырьком:", slb)
print(f"Количество сравнений : {b}")
print("Сортировка выбором")
ul = sl.copy() # делаем копию исходнего листа
sls = []
d = 0 # снова задаем счетчики
e = 0
while len(ul) > 0:
    max= ul[0] # зададим переменную  т.к ищем максимум для сортировки
    for i in range(0, len(ul)):
        d += 1
        if ul[i] > max: # ищем самый большой элемент из оставшихся
            max= ul[i]         
    sls.append(max)
    ul.remove(max)
    e += 1
    print(f"Шаг {e}: {sls}") # опять выводим промежуточный результат
print("\nКонечный результат выбором:", sls)
print(f"Количество сравнений (выбор): {d}")
