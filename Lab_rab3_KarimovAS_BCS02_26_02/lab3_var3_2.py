n = int(input("Введите кол-во чисел:"))
k=0
sun = 0
while k != n and (e := int(input("Введите элемент последовательности:"))) % 2 ==0:
    sun += e
    k += 1
print(sun)