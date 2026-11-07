D = []
k = 0
while True:
    z = input('Введите числ:')
    try:
        z = int(z)
        D.append(z)
        k += 1
        if k == 8:
            break
        continue
    except ValueError:
        print("это не число")
a = []
for i in range(len(D)):
    if D[i]<15:
        a.append(D[i]*2)
    else:
        a.append(D[i])
print(a)
