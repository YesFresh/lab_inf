x = float(input("координата x: "))
y = float(input("координата y: "))
krug = (x + 7) ** 2 + (y - 3) ** 2 <= 9 
trey = (-5 <= x <= 0) and (0 <= y <= 1.2 * x + 6)
if krug or trey:
    print("Точка принадлежит области")
else:
    print("Точка не принадлежит области")