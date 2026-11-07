import math
A = int(input("Введите A1:"))
B = int(input("Введите Б:"))
s = 0
if A>=B:
    print("A и Б поменялись местами")
    for i in range(B, A+1):
        s = i**2 + s
    print(s)
else:
    for i in range(A, B+1):
        s = i**2 + s
    print(s)

