from math import *

print("1-вода")
print("2-масло")
print("3-сталь")

while True:
    sip = input()
    match sip:
        case "1": c = 4200; sred = "Вода"; break
        case "2": c = 2000; sred = "Масло"; break
        case "3": c = 500; sred = "Сталь"; break
        case _: print("Нет данных")  
        

while True: 
    m = input("Введите массу (от 0.1 до 1000 ):")
    try:
        m = float(m)
        if not 0.1 <= m <= 1000:
            print("Ошибка")
            continue
        break
    except ValueError:
        print("m - Не число")

while True:
    t1 = input("Введите 1 температуру (от -50 до 100 ):")
    try:
        t1 = float(t1)
        if not -50 <= t1 <= 100:
            print("Ошибка")
            continue
        break
    except ValueError:
        print("t1 - Не число")

while True:
    t2 = input("Введите 2 температуру(t2>t1) (от 0 до 1000 ):")
    try:
        t2 = float(t2)
        if not(0 <= t2 <= 1000) or not(t2>t1):
            print("Ошибка")
            continue
        break
    except ValueError:
        print("t2 - Не число") 

Q = m*c*(t2-t1)

det_t = t2-t1
if det_t<10: qwe = "малый нагрев"
if 10<=det_t<=100: qwe = "средний нагрев"
if det_t>100: qwe = "ужас сильный нагрев"
print(sred, Q, qwe)

