n = int(input("Введите кол-во символов:"))
D = list(range(n))
suw=0
for i in range(len(D)):
    if i % 2 != 0:
        suw += D[i]
        print(D[i])
print(D, suw)