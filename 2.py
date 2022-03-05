spisok = []
sum = 0
for i in range (1000):
    spisok.append(i**3)
while (spisok != 0):
    sum = sum + spisok % 10
    spisok = spisok // 10
print(sum)